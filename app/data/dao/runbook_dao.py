from app import db
from app.core.models.runbook import Runbook

class RunbookDAO:
    @staticmethod
    def get_runbook_by_id(runbook_id):
        return Runbook.query.get(runbook_id)

    @staticmethod
    def create_runbook(runbook_data):
        new_runbook = Runbook(**runbook_data)
        db.session.add(new_runbook)
        db.session.commit()
        return new_runbook

    @staticmethod
    def update_runbook(runbook_id, update_data):
        runbook = Runbook.query.get(runbook_id)
        if runbook:
            for key, value in update_data.items():
                setattr(runbook, key, value)
            db.session.commit()
            return runbook
        return None

    @staticmethod
    def delete_runbook(runbook_id):
        runbook = Runbook.query.get(runbook_id)
        if runbook:
            db.session.delete(runbook)
            db.session.commit()
            return True
        return False
