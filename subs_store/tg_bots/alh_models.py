import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

engine = create_engine(
    url=os.environ.get("POSTGRES_URL"),
    echo=True
)


class Base(DeclarativeBase):
    pass

class CustomUser(Base):
    __tablename__ = "subscriptions_customuser"

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str]
    last_login: Mapped[datetime]
    is_superuser: Mapped[bool]
    username: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    is_staff: Mapped[bool]
    is_active: Mapped[bool]
    date_joined: Mapped[datetime]
    phone: Mapped[str]
    tg_id: Mapped[int]

    def __str__(self):
        return (f'{self.__class__.__name__}(username={self.username}')

    def __repr__(self):
        return str(self)