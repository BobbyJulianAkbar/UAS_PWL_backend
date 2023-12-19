"""initial migrate

Revision ID: be9edb766cec
Revises: 
Create Date: 2023-12-10 21:09:10.969824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "be9edb766cec"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "kategori",
        sa.Column(
            "id", sa.Integer, primary_key=True, autoincrement=True, nullable=False
        ),
        sa.Column("kategori", sa.String(255), nullable=False),
    )
    op.create_table(
        "buku",
        sa.Column(
            "id", sa.Integer, primary_key=True, autoincrement=True, nullable=False
        ),
        sa.Column("judul", sa.String(255), nullable=False),
        sa.Column("pengarang", sa.String(255), nullable=False),
        sa.Column("penerbit", sa.String(255), nullable=False),
        sa.Column("tahun_terbit", sa.String(255), nullable=False),
        sa.Column("kategori_id", sa.Integer, nullable=False),
        sa.Column("isbn", sa.String(255), nullable=False),
        sa.Column("jumlah_buku", sa.Integer, nullable=True),
        sa.Column("deskripsi", sa.String(255), nullable=True),
        # crete foreign key
        sa.ForeignKeyConstraint(
            ["kategori_id"],
            ["kategori.id"],
            name="fk_kategori_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )
    op.create_table(
        "petugas",
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("fnama", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("status", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    #     int32 id = 1;
    # string nama = 2;
    # string email = 3;
    # string nis = 4;
    # string password = 5;
    # string token = 6;
    op.create_table(
        "anggota",
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("nama", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("nis", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("token", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    # int32 id = 1;
    # int32 id_buku = 2;
    # int32 id_anggota = 3;
    # string tanggal_peminjaman = 4;
    # string tanggal_pengembalian = 5;
    # string status = 6;

    op.create_table(
        "peminjaman",
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("id_buku", sa.Integer(), nullable=False),
        sa.Column("id_anggota", sa.Integer(), nullable=False),
        sa.Column("tanggal_peminjaman", sa.String(length=255), nullable=False),
        sa.Column("tanggal_pengembalian", sa.String(length=255), nullable=False),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["id_buku"],
            ["buku.id"],
            name="fk_buku_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["id_anggota"],
            ["anggota.id"],
            name="fk_anggota_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )

    # seed data kategori
    op.bulk_insert(
        sa.table(
            "kategori",
            sa.Column(
                "id", sa.Integer, primary_key=True, autoincrement=True, nullable=False
            ),
            sa.Column("kategori", sa.String(255), nullable=False),
        ),
        [
            {"id": 1, "kategori": "Pemrograman"},
            {"id": 2, "kategori": "Sains"},
            {"id": 3, "kategori": "Teknologi"},
            {"id": 4, "kategori": "Komputer"},
            {"id": 5, "kategori": "Fiksi"},
            {"id": 6, "kategori": "Non Fiksi"},
        ],
    )

    # seed data buku
    op.bulk_insert(
        sa.table(
            "buku",
            sa.Column(
                "id",
                sa.Integer,
                primary_key=True,
                autoincrement=True,
            ),
            sa.Column("judul", sa.String(255), nullable=False),
            sa.Column("pengarang", sa.String(255), nullable=False),
            sa.Column("penerbit", sa.String(255), nullable=False),
            sa.Column("tahun_terbit", sa.String(255), nullable=False),
            sa.Column("kategori_id", sa.Integer, nullable=False),
            sa.Column("isbn", sa.String(255), nullable=False),
            sa.Column("jumlah_buku", sa.Integer, nullable=True),
            sa.Column("deskripsi", sa.String(255), nullable=True),
        ),
        [
            {
                "id": 1,
                "judul": "Pemrograman Python",
                "pengarang": "Budi Raharjo",
                "penerbit": "Informatika",
                "tahun_terbit": "2019",
                "kategori_id": 1,
                "isbn": "123456789",
                "jumlah_buku": 10,
                "deskripsi": "Pemrograman Python",
            },
            {
                "id": 2,
                "judul": "Pemrograman Java",
                "pengarang": "Budi Raharjo",
                "penerbit": "Informatika",
                "tahun_terbit": "2019",
                "kategori_id": 1,
                "isbn": "123456789",
                "jumlah_buku": 10,
                "deskripsi": "Pemrograman Java",
            },
            {
                "id": 3,
                "judul": "Pemrograman C++",
                "pengarang": "Budi Raharjo",
                "penerbit": "Informatika",
                "tahun_terbit": "2019",
                "kategori_id": 1,
                "isbn": "123456789",
                "jumlah_buku": 10,
                "deskripsi": "Pemrograman C++",
            },
            {
                "id": 4,
                "judul": "Pemrograman C#",
                "pengarang": "Budi Raharjo",
                "penerbit": "Informatika",
                "tahun_terbit": "2019",
                "kategori_id": 1,
                "isbn": "123456789",
                "jumlah_buku": 10,
                "deskripsi": "Pemrogram C#",
            },
        ],
    )

    # seed data petugas
    op.bulk_insert(
        sa.table(
            "petugas",
            sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
            sa.Column("fnama", sa.String(length=255), nullable=False),
            sa.Column("email", sa.String(length=255), nullable=False),
            sa.Column("password", sa.String(length=255), nullable=False),
            sa.Column("username", sa.String(length=255), nullable=False),
            sa.Column("status", sa.String(length=255), nullable=False),
        ),
        [
            {
                "fnama": "Petugas 1",
                "email": "admin@admin.com",
                "password": "admin",
                "username": "admin",
                "status": "aktif",
            },
        ],
    )

    # seed data 1 anggota
    op.bulk_insert(
        sa.table(
            "anggota",
            sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
            sa.Column("nama", sa.String(length=255), nullable=False),
            sa.Column("email", sa.String(length=255), nullable=False),
            sa.Column("nis", sa.String(length=255), nullable=False),
            sa.Column("password", sa.String(length=255), nullable=False),
            sa.Column("token", sa.String(length=255), nullable=True),
        ),
        [
            {
                "nama": "Anggota 1",
                "email": "anggota@anggota.com",
                "nis": "123456789",
                "password": "123456789",
                "token": "",
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("kategori")
    op.drop_table("buku")
    op.drop_table("petugas")
    op.drop_table("anggota")
    op.drop_table("peminjaman")
