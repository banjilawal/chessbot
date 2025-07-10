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
    MIN_ROW_COUNT = 6
    MIN_COLUMN_COUNT = 6

    horizontal_movers: List[HorizontalMover] = field(default_factory=list)

    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def __post_init__(self):
        if not all([
            self.dimension.height > self.MIN_ROW_COUNT,
            self.dimension.length >        self.MIN_COLUMN_COUNT
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

    def place_on_grid(self, upper_left_coordinate: GridCoordinate, grid_entity: GridEntity) -> Optional[GridEntity]:
        if upper_left_coordinate is None:
            raise ValueError("Coordinate cannot be None")
        if grid_entity is None:
            raise ValueError("Entity cannot be None")

        cells = self.get_cells_in_entity_area(upper_left_coordinate, grid_entity)
        if cells is None:
            print("the cells is null")
        if len(cells) == 0:
            print("There are no cells available in the entity's area")
            return None
        if not self.are_destination_cells_empty(cells, grid_entity):
            print("There are occupied cells in the destination area")
            return None

        for cell in cells:
            cell.enter_cell(grid_entity)
        grid_entity.coordinate = upper_left_coordinate
        return grid_entity

    def move_entity(self, destination_coordinate: GridCoordinate, grid_entity: GridEntity) -> Optional[GridEntity]:
        if destination_coordinate is None:
            raise ValueError("Coordinate cannot be None")
        if grid_entity is None:
            raise ValueError("Entity cannot be None")

        destination_cells = self.get_cells_in_entity_area(destination_coordinate, grid_entity)
        if len(destination_cells) == 0:
            print("There is no cells for moving into.")
            return None

        if not self.are_destination_cells_empty(destination_cells, grid_entity):
            print("There are occupied cells in the destination area")
            return None


        for cell in grid_entity.cells:
            cell.leave_cell()

        for cell in destination_cells:
            cell.enter_cell(grid_entity)
        grid_entity.coordinate = destination_coordinate
        return grid_entity


    def random_empty_cell(self) -> Optional[Cell]:
        return random.choice(self.empty_cells())

    def are_destination_cells_empty(self, cells: List[Cell], grid_entity: GridEntity) -> bool:
        if not cells:
            return False
        return all(cell.occupant is None or cell.occupnat is not None and cell.occupant == grid_entity for cell in cells)

    def get_cells_in_entity_area(self, upper_left_coordinate: GridCoordinate, grid_entity: GridEntity) -> List[Cell]:
        if upper_left_coordinate is None:
            raise ValueError("Coordinate cannot be None")
        if grid_entity is None:
            raise ValueError("Entity cannot be None")

        cells = []
        if upper_left_coordinate.column + grid_entity.dimension.length > self.dimension.length:
            return cells
        if upper_left_coordinate.row + grid_entity.dimension.height > self.dimension.height:
            return cells


        for row in range(upper_left_coordinate.row, upper_left_coordinate.row + grid_entity.dimension.height):
            for col in range(upper_left_coordinate.column, upper_left_coordinate.column + grid_entity.dimension.length):
                cell = self.find_cell_by_coordinate(GridCoordinate(row=row, column=col))
                if cell is not None:
                    print(cell.__str__(), " in area", grid_entity.dimension.area())
                    cells.append(cell)
        return cells

    def add_horizontal_mover(self, mover: HorizontalMover) -> Optional[HorizontalMover]:
        cell = self.random_empty_cell()
        print("randomly selected cell", cell)
        print("horizontal mover dimension", mover.dimension, " mover area=", mover.dimension.area())
        if cell is None:
            print("No place for mover")
            return None

        entity = self.place_on_grid(self.random_empty_cell().coordinate, mover)
        if entity is None:
            print("No place for mover")
            return None
        if not isinstance(entity, HorizontalMover):
            print("Mover is not horizontal")
            return None
        if isinstance(entity, HorizontalMover):
            placed_mover = cast(HorizontalMover, entity)
            self.horizontal_movers.append(placed_mover)
            return placed_mover
        return None

    def random_mover(self) -> Optional[HorizontalMover]:
        if len(self.horizontal_movers) == 0:
            return None
        return random.choice(self.horizontal_movers)
