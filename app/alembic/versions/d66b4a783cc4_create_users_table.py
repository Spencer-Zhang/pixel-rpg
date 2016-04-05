"""create users table

Revision ID: d66b4a783cc4
Revises:
Create Date: 2016-03-17 17:00:34.776101

"""

# revision identifiers, used by Alembic.
revision = 'd66b4a783cc4'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(20), nullable=False, unique=True),
        sa.Column('pwhash', sa.String(60), nullable=False),
        sa.Column('email', sa.String(140), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('users')
