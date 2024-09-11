from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.utils.database import Base
from enum import Enum as PyEnum

class PaymentStatus(PyEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer)
    status = Column(Enum(PaymentStatus))
    method = Column(String(50))
    
    user = relationship('User')

    def __repr__(self):
        return f"<Payment(amount={self.amount}, status={self.status})>"
