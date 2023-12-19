from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

#    op.create_table(
#         "kategori",
#         sa.Column(
#             "id", sa.Integer, primary_key=True, autoincrement=True, nullable=False
#         ),
#         sa.Column("kategori", sa.String(255), nullable=False),
#     )


class Kategori(Base):
    __tablename__ = "kategori"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    kategori: Mapped[str] = mapped_column(nullable=False)
