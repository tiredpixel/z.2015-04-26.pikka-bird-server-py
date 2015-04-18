from flask import Blueprint, jsonify, request

from pikka_bird_receiver.models.collection import Collection
from pikka_bird_receiver.models.machine import Machine
from pikka_bird_receiver.models.report import Report
from pikka_bird_receiver.models.service import Service


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
            
            for data_report in data['reports']:
                service = Service.find(True, code=data_report['service'])
                
                Report(
                    collection=collection,
                    service=service,
                    data=data_report['data']) # attaches to collection
        except KeyError:
            return jsonify(), 422
        
        Collection.query.session.add(collection) # includes reports
        Collection.query.session.commit()
        
        return jsonify(), 201
    else:
        return jsonify(), 415
