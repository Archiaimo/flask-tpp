"""empty message

Revision ID: 9f31a9def5fc
Revises: a7a8bbc4c56e
Create Date: 2019-12-17 15:36:17.858556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f31a9def5fc'
down_revision = 'a7a8bbc4c56e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('is_verify', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('p_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('p_name')
    )
    op.create_table('cinema_user_permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_user_id', sa.Integer(), nullable=True),
    sa.Column('c_permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['c_user_id'], ['cinema_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_user_permission')
    op.drop_table('permissions')
    op.drop_table('cinema_user')
    # ### end Alembic commands ###
