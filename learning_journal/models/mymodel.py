from sqlalchemy import (
    Column,
    Integer,
    Unicode
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(Unicode)

