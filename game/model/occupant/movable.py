from abc import ABC, abstractmethod
from typing import List
from game.model.cell.cell import Cell

class Movable(ABC):
    """Interface for obstacles that can be moved."""

    @abstractmethod
    def leave_cells(self) -> List[Cell]:
        """Returns a list of cells being vacated."""
        pass

    @abstractmethod
    def enter_cells(self, cells: List[Cell]) -> None:
        """Updates internal state to reflect the new cell occupancy."""
        pass

    @abstractmethod
    def can_move_to(self, cells: List[Cell]) -> bool:
        """Returns True if the obstacle is allowed to move to the given cells."""
        pass
