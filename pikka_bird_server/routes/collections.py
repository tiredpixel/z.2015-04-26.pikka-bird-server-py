from flask import Blueprint, jsonify, request

from pikka_bird_server.models.collection import Collection
from pikka_bird_server.models.machine import Machine
from pikka_bird_server.models.report import Report
from pikka_bird_server.models.service import Service


collections = Blueprint('collections', __name__)


@collections.route('/collections', methods=['POST'])
def create():
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        
        machine = Machine.find(address=request.remote_addr)
        
        try:
            collection = Collection(
                machine=machine,
                collecting_at=data['collecting_at'],
                collected_at=data['collected_at'],
                hostname=data['hostname'],
                pid=data['pid'])
            
            for data_service, data_report in data['reports'].items():
                service = Service.find(True, code=data_service)
                
                Report(
                    collection=collection,
                    service=service,
                    data=data_report) # attaches to collection
        except KeyError:
            return jsonify(), 422
        
        Collection.query.session.add(collection) # includes reports
        Collection.query.session.commit()
        
        return jsonify(), 201
    else:
        return jsonify(), 415
