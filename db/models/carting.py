from sqlalchemy import Column, Integer, String

from db.config import Base


class Carting(Base):
    __tablename__ = 'cartings'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    session_price = Column(Integer, nullable=False)
