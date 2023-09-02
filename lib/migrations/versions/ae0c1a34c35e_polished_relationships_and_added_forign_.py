"""Polished relationships and added forign keys to Freebie model

Revision ID: ae0c1a34c35e
Revises: dd36c80e9ece
Create Date: 2023-09-02 22:27:33.695026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae0c1a34c35e'
down_revision = 'dd36c80e9ece'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('dev_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_freebies_dev_id_devs'), 'devs', ['dev_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_freebies_company_id_companies'), 'companies', ['company_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_freebies_company_id_companies'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_freebies_dev_id_devs'), type_='foreignkey')
        batch_op.drop_column('dev_id')
        batch_op.drop_column('company_id')

    # ### end Alembic commands ###
