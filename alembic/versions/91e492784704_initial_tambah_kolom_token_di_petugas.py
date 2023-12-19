"""initial tambah kolom token di petugas

Revision ID: 91e492784704
Revises: be9edb766cec
Create Date: 2023-12-12 03:43:21.677859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "91e492784704"
down_revision: Union[str, None] = "be9edb766cec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("petugas", sa.Column("token", sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column("petugas", "token")
