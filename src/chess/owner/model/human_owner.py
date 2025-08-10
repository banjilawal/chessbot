from typing import Optional

from chess.owner.model.owner import Owner
from chess.team.team import Team


class HumanOwner(Owner):

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None):
        super().__init__(owner_id, name, team)
        d




