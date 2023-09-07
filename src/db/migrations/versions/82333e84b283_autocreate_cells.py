"""autocreate cells

Revision ID: 82333e84b283
Revises: fd33eb950525
Create Date: 2023-09-07 09:18:42.338295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from db.models import Cell


# revision identifiers, used by Alembic.
revision: str = '82333e84b283'
down_revision: Union[str, None] = 'fd33eb950525'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

cells = {
    1: 20,
    2: 100,
    3: 45,
    4: 70,
    5: 15,
    6: 140,
    7: 20,
    8: 20,
    9: 140,
    10: 45,
}


def upgrade() -> None:
    op.execute(sa.insert(Cell).values(id=1, number=11, weight=0, is_jackpot=True))
    for id_, (number, weight) in enumerate(cells.items(), 2):
        op.execute(
            sa.insert(Cell).values(
                id=id_, number=number, weight=weight, is_jackpot=False
            )
        )


def downgrade() -> None:
    op.execute(sa.delete(Cell))
