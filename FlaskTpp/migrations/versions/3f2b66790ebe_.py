"""empty message

Revision ID: 3f2b66790ebe
Revises: 37bf0186a14f
Create Date: 2019-12-17 19:45:52.209977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f2b66790ebe'
down_revision = '37bf0186a14f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_cinema_id', sa.Integer(), nullable=True),
    sa.Column('c_movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_cinema_id'], ['cinema_user.id'], ),
    sa.ForeignKeyConstraint(['c_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_movie')
    # ### end Alembic commands ###