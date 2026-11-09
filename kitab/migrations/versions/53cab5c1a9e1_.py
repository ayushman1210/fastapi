"""empty message

Revision ID: 53cab5c1a9e1
Revises: c6acfce0284e
Create Date: 2026-11-05 17:19:12.271189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '53cab5c1a9e1'
down_revision: Union[str, Sequence[str], None] = 'c6acfce0284e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
