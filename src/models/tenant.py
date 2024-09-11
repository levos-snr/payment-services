from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class Tenant(Base):
    __tablename__ = 'tenants'
    
    id = Column(Integer, primary_key=True, index=True)
    tenant_name = Column(String(100))
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    owner = relationship('User')

    def __repr__(self):
        return f"<Tenant(name={self.tenant_name})>"
