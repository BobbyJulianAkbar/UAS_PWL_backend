from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Buku(Base):
    __tablename__ = "buku"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    judul: Mapped[str] = mapped_column(nullable=False)
    pengarang: Mapped[str] = mapped_column(nullable=False)
    penerbit: Mapped[str] = mapped_column(nullable=False)
    tahun_terbit: Mapped[str] = mapped_column(nullable=False)
    kategori_id: Mapped[int] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(nullable=False)
    jumlah_buku: Mapped[int] = mapped_column(nullable=True)
    deskripsi: Mapped[str] = mapped_column(nullable=True)
