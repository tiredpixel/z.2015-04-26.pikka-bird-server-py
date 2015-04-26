"""create_collections

Revision ID: 562ba8022d3
Revises: d6ebfd0a1b
Create Date: 2015-04-04 17:01:52.479022

"""

# revision identifiers, used by Alembic.
revision = '562ba8022d3'
down_revision = 'd6ebfd0a1b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    sql_now = sa.text("timezone('utc'::text, now())")
    
    op.create_table(
      'collections',
      sa.Column('id', sa.BigInteger,
        primary_key=True),
      sa.Column('created_at', sa.DateTime,
        nullable=False, index=True, server_default=sql_now),
      sa.Column('machine_id', sa.Integer, sa.ForeignKey(
        'machines.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False),
      sa.Column('collecting_at', sa.DateTime,
        nullable=False),
      sa.Column('collected_at', sa.DateTime,
        nullable=False),
      sa.Column('hostname', sa.String,
        nullable=False),
      sa.Column('pid', sa.Integer,
        nullable=False))

def downgrade():
    op.drop_table('collections')
