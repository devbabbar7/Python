from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    # What does index do?
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)