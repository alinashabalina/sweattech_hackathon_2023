"""empty message

Revision ID: 55c0987a8779
Revises: 
Create Date: 2023-11-18 15:24:07.035251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55c0987a8779'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('day_view',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('day_energy', sa.String(length=255), nullable=True),
    sa.Column('period_day_correct', sa.Boolean(), nullable=True),
    sa.Column('training_type', sa.String(length=255), nullable=True),
    sa.Column('feedback', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questionnaire',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('date_of_birth', sa.String(), nullable=False),
    sa.Column('hormone_state', sa.String(length=255), nullable=False),
    sa.Column('day_of_cycle', sa.Integer(), nullable=False),
    sa.Column('goal_list', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('training_recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('training_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trainings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('energy_level', sa.String(length=255), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trainings')
    op.drop_table('training_recommendations')
    op.drop_table('questionnaire')
    op.drop_table('day_view')
    # ### end Alembic commands ###