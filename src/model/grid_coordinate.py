from dataclasses import dataclass

"""
Encapsulated Grid.row and Grid.height into GridCoordinate. model.cell.Cell, and model.occupant.* use GridCoordinate 
instead of row, and height. This gives a GridCoordinate as a single-source-of-truth. We can do validate row and height
 in GridCoordinate and avoid mixing ids with rows or columns
"""


@dataclass(frozen=True)
class GridCoordinate:
    row: int
    column: int

    def __post_init__(self):
        if self.row < 0:
            raise ValueError("Row cannot be negative")
        if self.column < 0:
            raise ValueError("Column cannot be negative")


@dataclass(frozen=True)
class CoordinateRange:
    first_coordinate: GridCoordinate
    last_coordinate: GridCoordinate
