"""add content column to posts table

Revision ID: 9da373266a81
Revises: 365c7b207e6b
Create Date: 2024-02-15 13:51:54.659248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9da373266a81'
down_revision: Union[str, None] = '365c7b207e6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
