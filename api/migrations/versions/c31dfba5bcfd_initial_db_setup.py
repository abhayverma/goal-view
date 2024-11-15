"""Initial DB Setup

Revision ID: c31dfba5bcfd
Revises: 
Create Date: 2024-11-10 23:04:54.534507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31dfba5bcfd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('areas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('logo_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('home_team_id', sa.Integer(), nullable=False),
    sa.Column('away_team_id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['areas.id'], ),
    sa.ForeignKeyConstraint(['away_team_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['home_team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('position', sa.Enum('FORWARD', 'MIDFIELDER', 'DEFENDER', 'GOALKEEPER', name='playerposition'), nullable=False),
    sa.Column('birthdate', sa.String(length=50), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    op.drop_table('matches')
    op.drop_table('teams')
    op.drop_table('areas')
    # ### end Alembic commands ###
