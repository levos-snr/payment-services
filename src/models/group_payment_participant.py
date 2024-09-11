from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class GroupPaymentParticipant(Base):
    __tablename__ = 'group_payment_participants'
    
    id = Column(Integer, primary_key=True, index=True)
    group_payment_id = Column(Integer, ForeignKey('group_payments.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    amount_contributed = Column(Integer)
    
    group_payment = relationship('GroupPayment', back_populates='participants')
    user = relationship('User')

    def __repr__(self):
        return f"<GroupPaymentParticipant(user_id={self.user_id}, amount={self.amount_contributed})>"
