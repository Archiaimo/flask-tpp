"""empty message

Revision ID: a3e2c8514545
Revises: 3f2b66790ebe
Create Date: 2019-12-18 08:52:30.023889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3e2c8514545'
down_revision = '3f2b66790ebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hall',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('h_address_id', sa.Integer(), nullable=True),
    sa.Column('h_num', sa.Integer(), nullable=True),
    sa.Column('h_seats', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['h_address_id'], ['cinema_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hall_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('h_movie_id', sa.Integer(), nullable=True),
    sa.Column('h_hall_id', sa.Integer(), nullable=True),
    sa.Column('h_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['h_hall_id'], ['hall.id'], ),
    sa.ForeignKeyConstraint(['h_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hall_movie')
    op.drop_table('hall')
    # ### end Alembic commands ###
