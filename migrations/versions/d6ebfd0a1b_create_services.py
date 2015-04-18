"""create_services

Revision ID: d6ebfd0a1b
Revises: 37440ef063
Create Date: 2015-04-04 16:57:34.406021

"""

# revision identifiers, used by Alembic.
revision = 'd6ebfd0a1b'
down_revision = '37440ef063'

from alembic import op
import sqlalchemy as sa


def upgrade():
    sql_now = sa.text("timezone('utc'::text, now())")
    
    op.create_table(
      'services',
      sa.Column('id', sa.Integer,
        primary_key=True),
      sa.Column('created_at', sa.DateTime,
        nullable=False, server_default=sql_now),
      sa.Column('code', sa.String,
        nullable=False, index=True, unique=True))

def downgrade():
    op.drop_table('services')
