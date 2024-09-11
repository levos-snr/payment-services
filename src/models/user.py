from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from src.utils.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(150), unique=True, index=True)
    password_hash = Column(String(255))
    is_biometrics_enabled = Column(Boolean, default=False)
    is_ai_payments_enabled = Column(Boolean, default=False)
    
    payment_methods = relationship('PaymentMethod', back_populates='user')
    subscriptions = relationship('Subscription', back_populates='user')
    transactions = relationship('Transaction', back_populates='user')
    
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
