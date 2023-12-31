from __base_table import *

class Person(Base):
    __tablename__ = 'persons'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    name = Column(VARCHAR(25), nullable=False)
    last_name = Column(VARCHAR(25), nullable=False)
    middle_name = Column(VARCHAR(25), nullable=True)

    date_of_birth = Column(TIMESTAMP, nullable=False)

    number = Column(VARCHAR(10), nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.utcnow)