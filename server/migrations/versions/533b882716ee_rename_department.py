"""rename department

Revision ID: 533b882716ee
Revises: 2150231cb160
Create Date: 2024-03-30 23:42:48.088361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '533b882716ee'
down_revision = '2150231cb160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
