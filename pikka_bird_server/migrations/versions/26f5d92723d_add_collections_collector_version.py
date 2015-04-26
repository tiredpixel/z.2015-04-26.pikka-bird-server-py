"""add_collections_collector_version

Revision ID: 26f5d92723d
Revises: 44c401df80b
Create Date: 2015-04-18 20:05:57.811435

"""

# revision identifiers, used by Alembic.
revision = '26f5d92723d'
down_revision = '44c401df80b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('collections', sa.Column('version_server', sa.String,
        nullable=False, index=True))
    op.add_column('collections', sa.Column('version_collector', sa.String,
        nullable=False, index=True))

def downgrade():
    op.drop_column('collections', 'version_server')
    op.drop_column('collections', 'version_collector')
