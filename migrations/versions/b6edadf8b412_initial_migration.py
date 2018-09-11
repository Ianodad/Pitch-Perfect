"""Initial Migration

Revision ID: b6edadf8b412
Revises: f423656f6941
Create Date: 2018-09-11 20:18:47.848379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6edadf8b412'
down_revision = 'f423656f6941'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('category_id', sa.Integer(), nullable=True))
    op.drop_constraint('pitchs_catergory_id_fkey', 'pitchs', type_='foreignkey')
    op.create_foreign_key(None, 'pitchs', 'categories', ['category_id'], ['id'])
    op.drop_column('pitchs', 'catergory_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('catergory_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitchs', type_='foreignkey')
    op.create_foreign_key('pitchs_catergory_id_fkey', 'pitchs', 'categories', ['catergory_id'], ['id'])
    op.drop_column('pitchs', 'category_id')
    # ### end Alembic commands ###
