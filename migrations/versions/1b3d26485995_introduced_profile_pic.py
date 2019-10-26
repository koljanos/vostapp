"""introduced profile pic

Revision ID: 1b3d26485995
Revises: f92d1fe9ceef
Create Date: 2019-10-27 00:42:32.271970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b3d26485995'
down_revision = 'f92d1fe9ceef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('picture', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'picture')
    # ### end Alembic commands ###
