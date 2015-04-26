"""create_reports

Revision ID: 3cc3e86a2e6
Revises: 562ba8022d3
Create Date: 2015-04-04 17:25:15.417610

"""

# revision identifiers, used by Alembic.
revision = '3cc3e86a2e6'
down_revision = '562ba8022d3'

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import *


def upgrade():
    op.create_table(
      'reports',
      sa.Column('id', sa.BigInteger,
        primary_key=True),
      sa.Column('collection_id', sa.BigInteger, sa.ForeignKey(
        'collections.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False),
      sa.Column('service_id', sa.Integer, sa.ForeignKey(
        'services.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False),
      sa.Column('data', JSON,
        nullable=False))

def downgrade():
    op.drop_table('reports')
