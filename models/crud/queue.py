from __base_table import *

class Queue(Base):
    __tablename__ = 'queue'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    person = Column(UUID(as_uuid=True), ForeignKey('persons.id'), nullable=False)
    group_session = Column(UUID(as_uuid=True), ForeignKey('group_sessions.id'), nullable=False)

    lessons = Column(Integer, ForeignKey('lessons.id'), nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    is_active = Column(Boolean, nullable=False, default=True)