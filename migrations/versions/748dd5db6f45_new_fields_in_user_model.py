"""new fields in user model

Revision ID: 748dd5db6f45
Revises: 79217e2a243a
Create Date: 2019-10-23 20:06:06.521595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '748dd5db6f45'
down_revision = '79217e2a243a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
