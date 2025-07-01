from dataclasses import dataclass
from typing import List

from model.occupant.obstacle import Obstacle
from src.exception.exception import OccupiedSquareEntryError
from src.model.cell.cell import Cell
from src.model.occupant.traveler import Movable
from src.model.occupant.occupant import Occupant


@dataclass
class Crate(Obstacle, Movable):
    def __init__(self, _id: int, color: str, length: int, height: int):
        super().__init__(_id, color, length, height)
        self._type = "Crate"

    @property
    def type(self) -> str:
        return self._type

    def leave_cells(self) -> List[Cell]:
        if not self._squares:
            return []
        cells = self._squares
        for cell in cells:
            cell.occupant = None
        self._squares = []
        return cells

    def enter_cells(self, cells: List[Cell]) -> None:
        for cell in cells:
            if cell.occupant is not None:
                raise OccupiedSquareEntryError("Cannot enter a cell that's already occupied.")
            cell.occupant = self
        self._squares = cells

    def can_move_to(self, cells: List[Cell]) -> bool:
        return all(cell.occupant is None for cell in cells)