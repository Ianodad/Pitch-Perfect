"""Initial Migration

Revision ID: f0fe93b6755c
Revises: 5154ca314efb
Create Date: 2018-09-11 17:59:36.563457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0fe93b6755c'
down_revision = '5154ca314efb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('catergory', sa.String(length=255), nullable=True))
    op.drop_column('categories', 'cat_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('cat_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('categories', 'catergory')
    # ### end Alembic commands ###
