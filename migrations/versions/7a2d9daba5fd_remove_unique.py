"""remove unique

Revision ID: 7a2d9daba5fd
Revises: 0332a497fd84
Create Date: 2022-11-10 17:31:26.839638

"""
from alembic import op
# import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a2d9daba5fd'
down_revision = '0332a497fd84'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint(
        'users_email_key', 'users', type_='unique')
    op.drop_contraint(
        'bookshelves_shelf_name_key', 'bookshelves', type_='unique')


def downgrade():
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.create_unique_contstraint(
        'bookshelves_shelf_name_key', 'bookshelves', ['shelf_name'])
