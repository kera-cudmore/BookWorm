"""Initial migration

Revision ID: 0332a497fd84
Revises:
Create Date: 2022-07-27 19:05:04.010838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0332a497fd84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('bookshelves', sa.Column('created_by', sa.String(length=50)))
