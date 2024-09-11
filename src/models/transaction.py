from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    payment_id = Column(Integer, ForeignKey('payments.id'))
    reference = Column(String(100))
    status = Column(String(50))
    
    user = relationship('User')
    payment = relationship('Payment')

    def __repr__(self):
        return f"<Transaction(reference={self.reference}, status={self.status})>"
