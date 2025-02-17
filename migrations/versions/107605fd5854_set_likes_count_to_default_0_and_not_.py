"""Set likes_count to default 0 and not nullable

Revision ID: 107605fd5854
Revises: ac5d29414ba5
Create Date: 2025-01-03 13:19:54.957279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107605fd5854'
down_revision = 'ac5d29414ba5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('likes_count',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('likes_count',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
