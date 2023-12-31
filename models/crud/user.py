from __base_table import *

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    person = Column(UUID(as_uuid=True), ForeignKey('persons.id'), nullable=False)
    
    group_number = Column(Integer, ForeignKey('group_numbers.id'), nullable=False)
    access_levels = Column(Integer, ForeignKey('access_levels.id'), nullable=False)
    group_sessions = Column(UUID(as_uuid=True), ForeignKey('group_sessions.id'), nullable=False)