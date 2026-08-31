import datetime
import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Priority(enum.Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text)
    is_done = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Integer, nullable=False, default=Priority.MEDIUM.value)
    due_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"

    @property
    def priority_name(self):
        return Priority(self.priority).name
