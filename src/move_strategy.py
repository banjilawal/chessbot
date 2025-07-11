from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from geometry import GridCoordinate
from grid_entity import Mover, HorizontalMover

if TYPE_CHECKING:
    from board import Board
