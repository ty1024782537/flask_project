"""add table

Revision ID: 7804c02be6e3
Revises: 0dcb877a429c
Create Date: 2018-09-12 11:23:51.422250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7804c02be6e3'
down_revision = '0dcb877a429c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buyer_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('tel', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tel'),
    sa.UniqueConstraint('username')
    )
    op.create_table('buyer_address_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('provence', sa.String(length=8), nullable=True),
    sa.Column('city', sa.String(length=16), nullable=True),
    sa.Column('area', sa.String(length=16), nullable=True),
    sa.Column('detail_address', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('tel', sa.String(length=16), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['buyer_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('buyer_address_model')
    op.drop_table('buyer_user')
    # ### end Alembic commands ###
