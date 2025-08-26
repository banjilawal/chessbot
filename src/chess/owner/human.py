from typing import Optional

from chess.owner.base import Owner
from chess.team.model import Team


class HumanOwner(Owner):

    def __init__(self, owner_id: int, name: str):
        super().__init__(owner_id, name)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, HumanOwner):
            return self.id == other.id
        return False



