"""Add date column

Revision ID: 67fa5c84f59d
Revises: dcbc15551976
Create Date: 2019-06-14 16:42:48.214955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67fa5c84f59d'
down_revision = 'dcbc15551976'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date')
    # ### end Alembic commands ###
