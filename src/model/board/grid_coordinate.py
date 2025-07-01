from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    row: int
    column: int
