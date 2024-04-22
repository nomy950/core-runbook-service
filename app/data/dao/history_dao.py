from app import db
from app.core.models.runbook_execution_history import RunbookExecHistory

class RunbookExecHistoryDAO:
    @staticmethod
    def add_execution_history(execution_data):
        new_execution = RunbookExecHistory(**execution_data)
        db.session.add(new_execution)
        db.session.commit()
        return new_execution

    @staticmethod
    def get_execution_histories_by_runbook_id(runbook_id):
        return RunbookExecHistory.query.filter_by(runbook_id=runbook_id).all()

    @staticmethod
    def get_execution_history_by_id(execution_id):
        return RunbookExecHistory.query.get(execution_id)
