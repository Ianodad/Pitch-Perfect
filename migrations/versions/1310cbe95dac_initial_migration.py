"""Initial Migration

Revision ID: 1310cbe95dac
Revises: b6edadf8b412
Create Date: 2018-09-12 17:09:09.643404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1310cbe95dac'
down_revision = 'b6edadf8b412'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###