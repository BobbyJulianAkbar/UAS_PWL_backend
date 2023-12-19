from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Petugas(Base):
    __tablename__ = "petugas"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fnama: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    token: Mapped[str] = mapped_column()
