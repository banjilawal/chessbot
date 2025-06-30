from dataclasses import dataclass

from game.model.occupant.occupier import Occupier


@dataclass
class Crate(Occupier):
    def __init__(self, _id: int, color: str, length: int, height: int):
        super().__init__(_id, color, length, height)
        self._type = "Crate"

    @property
    def type(self) -> str:
        return self._type