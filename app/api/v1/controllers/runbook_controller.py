from flask import Blueprint, request, jsonify
from app.data.dao.runbook_dao import RunbookDAO

bp = Blueprint('runbook', __name__)

@bp.route('/runbooks', methods=['POST'])
def create_runbook():
    runbook_data = request.json
    runbook = RunbookDAO.create_runbook(runbook_data)
    return jsonify(runbook.id), 201

@bp.route('/runbooks/<int:runbook_id>', methods=['GET'])
def get_runbook(runbook_id):
    runbook = RunbookDAO.get_runbook_by_id(runbook_id)
    if runbook:
        return jsonify({
            'id': runbook.id,
            'runbook_name': runbook.runbook_name,
            'runbook_desc': runbook.runbook_desc,
            'runbook_url': runbook.runbook_url,
            'runbook_params': runbook.runbook_params,
            'created_date': runbook.created_date,
            'version': runbook.version
        })
    return jsonify({'error': 'Runbook not found'}), 404

@bp.route('/runbooks/<int:runbook_id>', methods=['PUT'])
def update_runbook(runbook_id):
    update_data = request.json
    runbook = RunbookDAO.update_runbook(runbook_id, update_data)
    if runbook:
        return jsonify({'message': 'Runbook updated successfully'}), 200
    return jsonify({'error': 'Runbook not found'}), 404

@bp.route('/runbooks/<int:runbook_id>', methods=['DELETE'])
def delete_runbook(runbook_id):
    if RunbookDAO.delete_runbook(runbook_id):
        return jsonify({'message': 'Runbook deleted successfully'}), 200
    return jsonify({'error': 'Runbook not found'}), 404
