from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING

from model.cell import Cell
from src.common.dimension import Dimension
from model.grid_coordinate import GridCoordinate

if TYPE_CHECKING:
    from model.cell import Cell

@dataclass
class GridEntity:
    id: int
    dimension: Dimension
    coordinate: GridCoordinate = None

@dataclass
class ImmovableGridEntity(GridEntity):

@dataclass
class BrikPallet(ImmovableGridEntity):

@dataclass
class MovableGridEntity(GridEntity):


