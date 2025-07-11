from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict, TYPE_CHECKING

from common.dimension import Dimension
from common.direction import Direction
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.grid_entity import GridEntity
from strategy.horizontal_movement_strategy import HorizontalMovementStrategy

if TYPE_CHECKING:
    from model.board import Board






