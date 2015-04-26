"""add_collections_platform

Revision ID: 55900322541
Revises: 26f5d92723d
Create Date: 2015-04-19 14:29:38.031544

"""

# revision identifiers, used by Alembic.
revision = '55900322541'
down_revision = '26f5d92723d'

from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg


def upgrade():
    op.add_column('collections', sa.Column('platform', pg.JSON,
        nullable=False))

def downgrade():
    op.drop_column('collections', 'platform')
