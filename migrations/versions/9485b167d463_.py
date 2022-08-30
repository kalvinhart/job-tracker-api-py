"""empty message

Revision ID: 9485b167d463
Revises: a8ef55ebbb0f
Create Date: 2022-08-26 17:07:16.624891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9485b167d463'
down_revision = 'a8ef55ebbb0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_job_date_applied'), 'job', ['date_applied'], unique=False)
    op.create_index(op.f('ix_job_interview_date'), 'job', ['interview_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_job_interview_date'), table_name='job')
    op.drop_index(op.f('ix_job_date_applied'), table_name='job')
    # ### end Alembic commands ###