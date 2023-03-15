"""Adicionado o campo currency em person

Revision ID: 96634f9af540
Revises: 8f1739ea63d8
Create Date: 2023-03-15 16:55:19.597927

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '96634f9af540'
down_revision = '8f1739ea63d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column(
        'currency', sqlmodel.sql.sqltypes.AutoString(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'currency')
    # ### end Alembic commands ###