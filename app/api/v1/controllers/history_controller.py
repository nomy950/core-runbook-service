from flask import Blueprint, request, jsonify
from app.data.dao.history_dao import RunbookExecHistoryDAO

bp = Blueprint('history', __name__)

@bp.route('/histories', methods=['POST'])
def add_execution_history():
    execution_data = request.json
    execution_history = RunbookExecHistoryDAO.add_execution_history(execution_data)
    return jsonify(execution_history.execution_id), 201

@bp.route('/histories/runbook/<int:runbook_id>', methods=['GET'])
def get_execution_histories(runbook_id):
    histories = RunbookExecHistoryDAO.get_execution_histories_by_runbook_id(runbook_id)
    return jsonify([{
        'execution_id': history.execution_id,
        'execution_type': history.execution_type,
        'execution_json': history.execution_json,
        'execution_date': history.execution_date,
        'execution_by': history.execution_by,
        'reference': history.reference,
        'status': history.status,
        'execution_completion_ts': history.execution_completion_ts
    } for history in histories]), 200
