"""empty message

Revision ID: ac5d29414ba5
Revises: 68c642d23e7c
Create Date: 2024-12-20 15:02:20.366325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac5d29414ba5'
down_revision = '68c642d23e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.add_column(sa.Column('board_id', sa.Integer(), nullable=True))
        batch_op.alter_column('likes_count',
        existing_type=sa.INTEGER(),
        nullable=True)
        batch_op.create_foreign_key(None, 'board', ['board_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('likes_count',
        existing_type=sa.INTEGER(),
        nullable=False)
        batch_op.drop_column('board_id')

    # ### end Alembic commands ###
