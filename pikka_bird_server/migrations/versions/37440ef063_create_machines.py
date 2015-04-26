"""create_machines

Revision ID: 37440ef063
Revises: None
Create Date: 2015-04-04 16:30:30.822979

"""

# revision identifiers, used by Alembic.
revision = '37440ef063'
down_revision = None

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import *


def upgrade():
    sql_now = sa.text("timezone('utc'::text, now())")
    
    op.create_table(
      'machines',
      sa.Column('id', sa.Integer,
        primary_key=True),
      sa.Column('created_at', sa.DateTime,
        nullable=False, server_default=sql_now),
      sa.Column('updated_at', sa.DateTime,
        nullable=False, index=True, server_default=sql_now),
      sa.Column('address', INET,
        nullable=False, index=True, unique=True),
      sa.Column('hostname', sa.String,
        index=True))

def downgrade():
    op.drop_table('machines')
