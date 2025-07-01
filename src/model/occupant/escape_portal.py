from dataclasses import dataclass

from common.game_color import GameColor
from common.game_default import GameDefault
from model.occupant.occupant import Occupant

@dataclass
class EscapePortal(Occupant):
    """
    Represents an escape portal in the game, which is an obstacle that allows occupants to escape.
    It inherits from the Obstacle class.
    """
    def __init__(self, color: GameColor = GameDefault.PORTAL_COLOR):
        super().__init__(id=1, color=color, length=Occupant.MIN_LENGTH, height=Occupant.MIN_HEIGHT)
        self._is_escape_portal = True

    @property
    def is_escape_portal(self) -> bool:
        return self._is_escape_portal