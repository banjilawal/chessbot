from abc import ABC, abstractmethod
from typing import List

from travel.board_direction import BoardDirection
from src.model.cell.cell import Cell

class Traveller(ABC):
    """Interface for obstacles that can be moved."""

    @abstractmethod
    def leave_cells(self) -> List[Cell]:
        """Returns a list of cells being vacated."""
        pass

    @abstractmethod
    def enter_cells(self, cells: List[Cell]) -> None:
        """Updates internal state to reflect the new cell occupancy."""
        pass

    # Added BoardDirection parameter to occupant.Movable.can_move_to() abstract method.
    # If moving left-right then travelling on length.
    # If Moving up-down then travelling on height."
    @abstractmethod
    def can_move_to(self, cells: List[Cell], direction: BoardDirection) -> bool:
        """Returns True if the obstacle is allowed to travel to the given cells."""
        pass
