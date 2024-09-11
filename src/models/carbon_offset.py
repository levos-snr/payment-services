from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class CarbonOffset(Base):
    __tablename__ = 'carbon_offsets'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    carbon_credits = Column(Integer)
    
    user = relationship('User')
    transaction = relationship('Transaction')

    def __repr__(self):
        return f"<CarbonOffset(user={self.user_id}, credits={self.carbon_credits})>"
