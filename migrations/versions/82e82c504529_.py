"""empty message

Revision ID: 82e82c504529
Revises: f61ec522d535
Create Date: 2020-06-13 22:12:27.230603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82e82c504529'
down_revision = 'f61ec522d535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('picture', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'picture')
    # ### end Alembic commands ###
