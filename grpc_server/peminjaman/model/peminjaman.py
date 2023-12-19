from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

# op.create_table(
#         "peminjaman",
#         sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
#         sa.Column("id_buku", sa.Integer(), nullable=False),
#         sa.Column("id_anggota", sa.Integer(), nullable=False),
#         sa.Column("tanggal_peminjaman", sa.String(length=255), nullable=False),
#         sa.Column("tanggal_pengembalian", sa.String(length=255), nullable=False),
#         sa.Column("status", sa.String(length=255), nullable=True),
#         sa.PrimaryKeyConstraint("id"),
#         sa.ForeignKeyConstraint(
#             ["id_buku"],
#             ["buku.id"],
#             name="fk_buku_id",
#             ondelete="CASCADE",
#             onupdate="CASCADE",
#         ),
#         sa.ForeignKeyConstraint(
#             ["id_anggota"],
#             ["anggota.id"],
#             name="fk_anggota_id",
#             ondelete="CASCADE",
#             onupdate="CASCADE",
#         ),
#     )


class Peminjaman(Base):
    __tablename__ = "peminjaman"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_buku: Mapped[int] = mapped_column(nullable=False)
    id_anggota: Mapped[int] = mapped_column(nullable=False)
    tanggal_peminjaman: Mapped[str] = mapped_column(nullable=False)
    tanggal_pengembalian: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=True)
