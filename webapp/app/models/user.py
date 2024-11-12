from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import db, Base


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    fullname = mapped_column(String)
    password_hash: Mapped[str]