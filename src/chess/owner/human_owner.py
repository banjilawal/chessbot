from typing import Optional

from chess.owner.owner import Owner
from chess.team.element.team import Team


class HumanPlayer(Owner):

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None):
        super().__init__(owner_id, name, team)




