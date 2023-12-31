from __base_table import *

class GroupSession(Base):
    __tablename__ = 'group_sessions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    is_open = Column(Boolean, nullable=False, default=True)