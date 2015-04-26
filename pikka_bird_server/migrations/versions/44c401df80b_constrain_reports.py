"""constrain_reports

Revision ID: 44c401df80b
Revises: 3cc3e86a2e6
Create Date: 2015-04-18 19:55:23.107690

"""

# revision identifiers, used by Alembic.
revision = '44c401df80b'
down_revision = '3cc3e86a2e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_unique_constraint('ix_reports_collection_id_service_id', 'reports', [
      'collection_id',
      'service_id'])


def downgrade():
    op.drop_constraint('ix_reports_collection_id_service_id', 'reports')
