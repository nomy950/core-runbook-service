from app import db
from datetime import datetime

class Runbook(db.Model):
    __tablename__ = 'runbooks'

    id = db.Column(db.Integer, primary_key=True)
    runbook_name = db.Column(db.String(255), nullable=False)
    runbook_desc = db.Column(db.Text, nullable=True)
    runbook_url = db.Column(db.String(255), nullable=False)
    runbook_params = db.Column(db.Text, nullable=True)  # JSON string of parameters
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    version = db.Column(db.String(50), nullable=False)

    # Relationship to execution history (one-to-many)
    execution_histories = db.relationship('RunbookExecHistory', backref='runbook', lazy=True)

    def __repr__(self):
        return f'<Runbook {self.runbook_name}, Version: {self.version}>'
