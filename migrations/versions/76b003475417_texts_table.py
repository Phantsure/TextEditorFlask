"""texts table

Revision ID: 76b003475417
Revises: a321d163e550
Create Date: 2020-03-25 17:11:07.887600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76b003475417'
down_revision = 'a321d163e550'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('textfile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('extension', sa.String(length=5), nullable=True),
    sa.Column('body', sa.String(length=2500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_textfile_timestamp'), 'textfile', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_textfile_timestamp'), table_name='textfile')
    op.drop_table('textfile')
    # ### end Alembic commands ###