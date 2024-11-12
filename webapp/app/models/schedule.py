from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import db, Base
from datetime import datetime

class DeviceSchedule(Base):
    __tablename__ = 'device_schedule'
    
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), nullable=False)  # Unique identifier for the device
    action = db.Column(db.Enum('on', 'off', 'toggle', 'custom', name='action_types'), nullable=False)
    schedule_type = db.Column(db.Enum('one-time', 'daily', 'weekly', 'custom', name='schedule_types'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=True)
    duration = db.Column(db.Integer, nullable=True)  # Duration in seconds/minutes
    repeat_interval = db.Column(db.Integer, nullable=True)  # Repeat interval in hours or days
    days_of_week = db.Column(db.String(100), nullable=True)  # List of days (e.g., ['Monday', 'Friday'])
    
    # Conditional triggers, using JSON for flexibility to store various conditions
    conditional_triggers = db.Column(db.JSON, nullable=True)
    
    priority = db.Column(db.Integer, nullable=True, default=1)  # Priority of the schedule
    status = db.Column(db.Enum('active', 'inactive', 'paused', name='status_types'), default='active')
    last_run_timestamp = db.Column(db.DateTime, nullable=True)  # Timestamp of the last run
    error_handling = db.Column(db.Enum('retry', 'skip', 'alert', name='error_handling_types'), default='retry')
    created_by = db.Column(db.String(50), nullable=True)  # User who created the schedule
    notes = db.Column(db.Text, nullable=True)  # Additional notes or comments about the schedule

    def __repr__(self):
        return f"<DeviceSchedule(device_id='{self.device_id}', action='{self.action}', schedule_type='{self.schedule_type}', start_time='{self.start_time}')>"

