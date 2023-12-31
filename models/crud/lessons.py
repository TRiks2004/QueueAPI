from __base_table import *

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(10), nullable=False)

    group_sessions = Column(UUID(as_uuid=True), ForeignKey('group_sessions.id'), nullable=False)