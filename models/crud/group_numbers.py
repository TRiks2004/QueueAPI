from __base_table import *

class GroupNumber(Base):
    __tablename__ = 'group_numbers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(10), nullable=False)