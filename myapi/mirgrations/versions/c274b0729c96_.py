"""empty message

Revision ID: c274b0729c96
Revises: d7f1779d7abd
Create Date: 2024-03-31 19:47:24.084972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c274b0729c96'
down_revision: Union[str, None] = 'd7f1779d7abd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
