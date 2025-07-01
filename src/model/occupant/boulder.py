from dataclasses import dataclass

from model.occupant.obstacle import Obstacle
from src.model.occupant.occupant import Occupant

# Added model.occupant.EscapePortal which extends Occupant class. Added list of walls to the Board. Renamed
# model.occupant.Wall to model.occupant.Boulder. The Board has 4 walls so the old name was ambigous and not
# communicating the item's intent."

@dataclass
class Boulder(Obstacle):
    def __init__(self, _id: int, color: str, length: int, height: int):
        super().__init__(_id, color, length, height)
        self._type = "Boulder"

    @property
    def type(self) -> str:
        return self._type