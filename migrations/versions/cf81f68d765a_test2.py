"""test2

Revision ID: cf81f68d765a
Revises: 5801a9bf5a6f
Create Date: 2021-06-28 12:02:22.986827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf81f68d765a'
down_revision = '5801a9bf5a6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_constraint('fk_message_send_user_id_user', type_='foreignkey')
        batch_op.drop_column('send_user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('send_user_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_message_send_user_id_user', 'user', ['send_user_id'], ['id'])

    # ### end Alembic commands ###