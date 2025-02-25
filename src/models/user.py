from . import Base
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from typing import List

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(30))
    password_hash: Mapped[str] = mapped_column(String(300))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now())
    tasks: Mapped[List["Task"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )