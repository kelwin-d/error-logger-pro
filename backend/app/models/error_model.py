from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ErrorLog(Base):
    __tablename__ = "error_logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    source = Column(String, nullable=True)
    stack_trace = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    request_url = Column(String, nullable=True)
    request_method = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
