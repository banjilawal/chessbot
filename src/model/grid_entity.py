from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING

from model.cell import Cell
from src.common.dimension import Dimension
from model.grid_coordinate import GridCoordinate
from strategy.horizontal_movement_strategy import HorizontalMovementStrategy

if TYPE_CHECKING:
    from model.cell import Cell

@dataclass
class GridEntity:
    dimension: Dimension
    top_left_coordinate: Optional[GridCoordinate] = None

@dataclass
class BrikPallet(GridEntity):
    pass

@dataclass(kw_only=True)
class Mover(GridEntity, ABC):
    id: int

    @abstractmethod
    def move(self, board: 'Board', destination_coordinate: GridCoordinate) -> None:
        pass

@dataclass
class VerticalMover(Mover):

    def __init__(self, mover_id: int, length: int, top_left_coordinate: Optional[GridCoordinate] = None):
        super().__init__(
            id=mover_id,
            dimension=Dimension(length=length, height=1),
            top_left_coordinate=top_left_coordinate
        )

    def move(self, board: 'Board', destination_coordinate: GridCoordinate):
        pass


@dataclass
class HorizontalMover(Mover):
    movement_strategy: HorizontalMovementStrategy = field(default_factory=HorizontalMovementStrategy)

    def __init__(self, mover_id: int, height: int, top_left_coordinate: Optional[GridCoordinate] = None):
        super().__init__(
            id=mover_id,
            dimension=Dimension(length=1, height=height),
            top_left_coordinate=top_left_coordinate
         )
        self.movement_strategy = HorizontalMovementStrategy()

    def move(self, board: 'Board', destination_coordinate: GridCoordinate):
        if not self.movement_strategy.move(self, board, destination_coordinate):
            print(f"Failed to move {self.id} to {destination_coordinate}.")
        else :
            print(f"Moved {self.id} to {destination_coordinate}.")

@dataclass
class UniversalMover(Mover):

    def __init__(self, mover_id: int, dimension: Dimension, top_left_coordinate: Optional[GridCoordinate] = None):
        super().__init__(
            id=mover_id,
            dimension=Dimension(length=dimension.length, height=dimension.height),
            top_left_coordinate=top_left_coordinate
        )

    def move(self, board: 'Board', destination_coordinate: GridCoordinate):
        pass