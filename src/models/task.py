from .base import Base
from .user import User
from sqlalchemy import Boolean, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(30))
    priority: Mapped[str] = mapped_column(String(30))
    due_date: Mapped[datetime] = mapped_column(DateTime, index=True)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    user: Mapped['User'] = relationship(back_populates='tasks')

    __table_args__ = (
        Index("unique_task_name_per_user", name, user_id, unique=True),
        Index("done_equals_false", done, postgresql_where=done == False),
    )