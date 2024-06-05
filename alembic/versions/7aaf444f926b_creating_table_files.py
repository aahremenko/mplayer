"""Creating table 'files'

Revision ID: 7aaf444f926b
Revises: 33999ab35328
Create Date: 2023-12-10 23:28:25.669538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7aaf444f926b'
down_revision: Union[str, None] = '6bf3f59ecfb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('file_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_path', sa.String(length=1000), nullable=True),
    sa.Column('load_date', sa.Date(), server_default=sa.text('now()'), nullable=True),
    sa.Column('file_type', sa.String(length=10), nullable=True),
    sa.Column('file_name', sa.String(length=250), nullable=True),
    sa.Column('processed_date', sa.Date(), nullable=True),
    sa.Column('processed_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('file_id'),
    sa.UniqueConstraint('file_path')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###
