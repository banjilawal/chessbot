from typing import Optional

from chess.owner.owner import Owner
from chess.team.team import Team


class HumanOwner(Owner):

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None):
        super().__init__(owner_id, name, team)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, HumanOwner):
            return self._id == other.id
        return False



