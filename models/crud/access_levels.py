from __base_table import *

class AccessLevel(Base):
    __tablename__ = 'access_levels'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(10), nullable=False)
