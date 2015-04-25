from flask import Blueprint, jsonify, request, abort
import msgpack

import pikka_bird_server
from pikka_bird_server.models.collection import Collection
from pikka_bird_server.models.machine import Machine
from pikka_bird_server.models.report import Report
from pikka_bird_server.models.service import Service


collections = Blueprint('collections', __name__)


@collections.route('/collections', methods=['POST'])
def create():
    """
        POST /collections
        Route to which a collector sends metrics.
        """
    
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
    elif request.headers['Content-Type'] == 'application/octet-stream':
        data = msgpack.unpackb(request.data, encoding='utf-8')
    else:
        abort(415)
    
    machine = Machine.find(address=request.remote_addr)
    
    try:
        collection = Collection(
            machine=machine,
            collecting_at=data['collecting_at'],
            collected_at=data['collected_at'],
            hostname=data['environment']['hostname'],
            pid=data['environment']['pid'],
            platform=data['environment']['platform'],
            version_server=pikka_bird_server.__version__,
            version_collector=data['environment']['version'])
        
        machine.update_hostname(data['environment']['hostname'])
        
        for data_service, data_report in data['reports'].items():
            service = Service.find(True, code=data_service)
            
            Report(
                collection=collection,
                service=service,
                data=data_report) # attaches to collection
    except KeyError:
        abort(422)
    
    Collection.query.session.add(collection) # includes reports
    Collection.query.session.commit()
    
    return jsonify(), 201
