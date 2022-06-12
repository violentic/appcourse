"""create user table

Revision ID: 29b1f4d97941
Revises: 
Create Date: 2022-05-22 11:42:13.996549

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = '29b1f4d97941'
down_revision = None
branch_labels = None
depends_on = None

 



def upgrade():
    op.create_table('admin', sa.Column('id', sa.Integer(), nullable = False, primary_key = True), sa.Column('email', sa.String(), nullable=False, unique = True, ), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')))
    pass


def downgrade():
    op.drop_table('admin')
    pass
