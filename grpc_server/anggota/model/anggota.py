from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

# op.create_table(
#         "anggota",
#         sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
#         sa.Column("nama", sa.String(length=255), nullable=False),
#         sa.Column("email", sa.String(length=255), nullable=False),
#         sa.Column("nis", sa.String(length=255), nullable=False),
#         sa.Column("password", sa.String(length=255), nullable=False),
#         sa.Column("token", sa.String(length=255), nullable=True),
#         sa.PrimaryKeyConstraint("id"),
#     )


class Anggota(Base):
    __tablename__ = "anggota"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    nis: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    token: Mapped[str] = mapped_column(nullable=True)
