import random
from dataclasses import dataclass, field

from typing import Tuple, List, Optional, cast, Dict

from common.direction import Direction
from common.id_generator import global_id_generator
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.crate import Crate
from common.dimension import Dimension
from model.grid_entity import GridEntity
from model.portal.door import Door
from model.bin import Bin
from model.vault import VerticalMover, HorizontalMover
from model.portal.portal import Portal
from src.common.game_default import GameDefault
from model.cell import Cell


@dataclass
class Grid:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    horizontal_movers: List[HorizontalMover] = field(default_factory=list)

    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def __post_init__(self):
        if not all([
            self.dimension.height >= self.MIN_ROW_COUNT,
            self.dimension.length >= self.MIN_COLUMN_COUNT
        ]):
            raise ValueError("Grid dimensions below minimum values")

        cells = tuple(
            tuple(
                Cell(
                    cell_id=row * self.dimension.length + col + 1,
                    coordinate=GridCoordinate(row=row, column=col)
                )
                for col in range(self.dimension.length)
            )
            for row in range(self.dimension.height)
        )
        self._set_crate_coordinates()
        object.__setattr__(self, 'cells', cells)


    def empty_cells(self) -> List[Cell]:
        empty_cells: List[Cell] = []
        for row in self.cells:
            for cell in row:
                if cell.occupant is None:
                    empty_cells.append(cell)
        return empty_cells

    def occupied_cells(self) -> List[Cell]:
        occupied_cells: List[Cell] = []
        for row in self.cells:
            for cell in row:
                if cell.occupant is not None:
                    occupied_cells.append(cell)
        return occupied_cells

    def find_cell_by_coordinate(self, coordinate: GridCoordinate) -> Optional[Cell]:
        if coordinate.row < 0 or coordinate.row >= self.dimension.height:
            return None
        if coordinate.column < 0 or coordinate.column >= self.dimension.length:
            return None
        return self.cells[coordinate.row][coordinate.column]

    def find_cell_by_id(self, cell_id: int) -> Optional[Cell]:
        for row in self.cells:
            for cell in row:
                if cell.cell_id == cell_id:
                    return cell
        return None

    def random_empty_cell(self) -> Optional[Cell]:
        return random.choice(self.empty_cells())

    def are_cells_available(self, cells: List[Cell], grid_entity: GridEntity) -> bool:
        if not cells:
            return False
        return all(cell.is_empty() or cell.is_occupied_by(grid_entity) for cell in cells)

    def get_cells_in_entity_area(self, upper_left_coordinate: GridCoordinate, grid_entity: GridEntity) -> Optional[List[Cell]]:
        if upper_left_coordinate is None:
            raise ValueError("Coordinate cannot be None")
        if grid_entity is None:
            raise ValueError("Entity cannot be None")

        if upper_left_coordinate.column + grid_entity.dimension.length > self.dimension.length:
            return None
        if upper_left_coordinate.row + grid_entity.dimension.height > self.dimension.height:
            return None

        cells = []
        for row in range(upper_left_coordinate.row, upper_left_coordinate.row + grid_entity.dimension.height):
            for col in range(upper_left_coordinate.column, upper_left_coordinate.column + grid_entity.dimension.length):
                cell = self.find_cell_by_coordinate(GridCoordinate(row=row, column=col))
                cells.append(cell)

        return cells

