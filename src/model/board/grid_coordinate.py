from dataclasses import dataclass


@dataclass(frozen=True)
class GridCoordinate:
    row: int
    column: int
