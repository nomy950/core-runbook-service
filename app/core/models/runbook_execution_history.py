from app import db
from datetime import datetime

class RunbookExecHistory(db.Model):
    __tablename__ = 'runbooks_exec_history'

    execution_id = db.Column(db.Integer, primary_key=True)
    runbook_id = db.Column(db.Integer, db.ForeignKey('runbooks.id'), nullable=False)
    execution_type = db.Column(db.String(255), nullable=False)
    execution_json = db.Column(db.Text, nullable=True)  # JSON string with execution details
    execution_date = db.Column(db.DateTime, default=datetime.utcnow)
    execution_by = db.Column(db.String(255), nullable=False)
    reference = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(100), nullable=False)
    execution_completion_ts = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<RunbookExecHistory {self.execution_id} - Status: {self.status}>'
