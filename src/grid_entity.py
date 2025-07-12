from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from geometry import Dimension, GridCoordinate

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
    movement_strategy: 'HorizontalMoveStrategy' = field(default_factory=lambda: HorizontalMoveStrategy())

    def __init__(self, mover_id: int, height: int, top_left_coordinate: Optional[GridCoordinate] = None):
        super().__init__(
            id=mover_id,
            dimension=Dimension(length=1, height=height),
            top_left_coordinate=top_left_coordinate
         )
        self.movement_strategy = HorizontalMoveStrategy()

    def move(self, board: 'Board', destination_coordinate: GridCoordinate):
        if not self.movement_strategy.move(self, board, destination_coordinate):
            print(f"Failed to move {self.id} to {destination_coordinate}.")
        else:
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


class MoveStrategy(ABC):
    @abstractmethod
    def move(self, mover: Mover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        pass

class HorizontalMoveStrategy(MoveStrategy):
    def move(self, mover: HorizontalMover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        if mover is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] Board cannot be None. Cannot move.")
            return False
        if mover.top_left_coordinate is None:
            print("[Warning] Mover has no top_left_coordinate. Cannot move.")
            return False
        if destination_coordinate is None:
            print("[Warning] Destination top_left_coordinate cannot be None. Cannot move.")
            return False

        if destination_coordinate.column < 0 or destination_coordinate.column >= board.dimension.length:
            print(f"[Warning] Horizontal move out of bounds: {destination_coordinate.column}")
            return False

        if destination_coordinate == mover.top_left_coordinate:
            print("[Warning] Mover is already at destination top_left_coordinate. Cannot move.")
            return False

        if destination_coordinate.row != mover.top_left_coordinate.row:
            print("[Warning] Destination top_left_coordinate is not on the same row as the mover. Cannot move.")
            return False

        destination_column = mover.top_left_coordinate.column
        print("strategy calculated destination column:", destination_column)
        return board.move_entity(destination_coordinate, mover) is not None

class VerticalMoveStrategy(MoveStrategy):
    def move(self, mover: VerticalMover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        if mover is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] Board cannot be None. Cannot move.")
            return False
        if mover.top_left_coordinate is None:
            print("[Warning] Mover has no top_left_coordinate. Cannot move.")
            return False
        if destination_coordinate is None:
            print("[Warning] Destination top_left_coordinate cannot be None. Cannot move.")
            return False

        if destination_coordinate.row < 0 or destination_coordinate.row >= board.dimension.length:
            print(f"[Warning] Vertical move out of bounds: {destination_coordinate.row}")
            return False

        if destination_coordinate == mover.top_left_coordinate:
            print("[Warning] Mover is already at destination top_left_coordinate. Cannot move.")
            return False

        if destination_coordinate.column != mover.top_left_coordinate.column:
            print("[Warning] Destination top_left_coordinate is not on the same column as the mover. Cannot move.")
            return False

        destination_row = mover.top_left_coordinate.row
        print("strategy calculated destination row:", destination_row)
        return board.move_entity(destination_coordinate, mover) is not None

class DragStrategy(ABC):
    def move(self, mover: Mover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        pass