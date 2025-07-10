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

    def add_entity_to_grid(self, upper_left_coordinate: GridCoordinate, grid_entity: GridEntity) -> Optional[GridEntity]:
        if upper_left_coordinate is None:
            raise ValueError("Coordinate cannot be None")
        if grid_entity is None:
            raise ValueError("Entity cannot be None")
        if grid_entity.coordinate is not None:
            raise Exception("Entity already has a coordinate")
        cell = self.cells[upper_left_coordinate.row][upper_left_coordinate.column]
        if cell.occupant is not None:
            raise Exception("Cell already occupied")

        cell.enter_cell(grid_entity)

        return grid_entity


@dataclass
class Grid:
    MIN_ROW_COUNT = 6
    MIN_COLUMN_COUNT = 6

    entities: List[GridEntity] = field(default_factory=list)

    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def __post_init__(self):
        if not all([
            self.dimension.height > self.MIN_ROW_COUNT,
            self.dimension.length > self.MIN_COLUMN_COUNT
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

    def find_entity_by_id(self, entity_id: int) -> Optional[GridEntity]:
        for entity in self.entities:
            if entity.id == entity_id:
                return entity
        return None



    def add_new_entity(self, top_left_coordinate: GridCoordinate, entity: GridEntity) -> Optional[GridEntity]:
        if top_left_coordinate is None or entity is None:
            raise ValueError("Top-left coordinate and entity must not be None.")

        # Bounds check
        if top_left_coordinate.row + entity.dimension.height > self.dimension.height:
            raise Exception("Entity does not fit within grid bounds at the specified coordinate.")

        if top_left_coordinate.column + entity.dimension.length > self.dimension.length:
            raise Exception("Entity does not fit within grid bounds at the specified coordinate.")

        if not self.can_entity_move_to_cells(entity, top_left_coordinate):
            raise Exception("Entity cannot move to the specified coordinate.")

        self.add_entity_to_area(entity, top_left_coordinate)
        self.register_entity(entity)
        return entity

    def can_entity_move_to_cells(self, entity: GridEntity, new_top_left_coordinate: GridCoordinate) -> bool:
        if entity is None or new_top_left_coordinate is None:
            raise ValueError("Entity and coordinate must not be None.")

        entity_length = entity.dimension.length
        entity_height = entity.dimension.height

        new_bottom_row = new_top_left_coordinate.row + entity_height - 1
        new_right_column = new_top_left_coordinate.column + entity_length - 1

        if new_bottom_row >= self.dimension.height:
            return False
        if new_right_column >= self.dimension.length:
            return False

        for r in range(new_top_left_coordinate.row, new_bottom_row + 1):
            for c in range(new_top_left_coordinate.column, new_right_column + 1):
                cell = self.cells[r][c]
                if cell.occupant is not None and cell.occupant != entity:
                    print(f"Cell at {r}, {c} is occupied by {cell.occupant}")
                    return False
        return True

    def get_cells_by_area(self, top_left_coordinate: GridCoordinate, dimension: Dimension) -> List[Cell]:
        if top_left_coordinate is None or dimension is None:
            raise ValueError("Coordinate and dimension must not be None.")

        start_row = top_left_coordinate.row
        start_col = top_left_coordinate.column

        end_row = start_row + dimension.height - 1
        end_col = start_col + dimension.length - 1

        cells_in_area = []
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                cells_in_area.append(self.cells[r][c])
        return cells_in_area

    def get_cells_occupied_by_entity(self, entity_id: int) -> List[Cell]:
        entity = self.find_entity_by_id(entity_id)
        if entity is None:
            return []

        occupied_cells = []
        for row in self.cells:
            for cell in row:
                if cell.occupant == entity:
                    occupied_cells.append(cell)
        return occupied_cells

    def remove_entity_from_cells(self, entity: GridEntity) -> None:
        if entity is None or entity.coordinate is None:
            raise ValueError("Entity or its coordinate is None.")

        target_cells = self.get_cells_occupied_by_entity()
        for cell in target_cells:
            if cell.occupant == entity:
                cell.occupant = None

    def add_entity_to_area(self, entity: GridEntity, top_left: GridCoordinate) -> None:
        if entity is None or top_left is None:
            raise ValueError("Entity and coordinate must not be None.")

        target_cells = self.get_cells_by_area(top_left, entity.dimension)

        for cell in target_cells:
            cell.occupant = entity

        entity.coordinate = top_left

    def register_entity(self, entity: GridEntity) -> None:
        if entity is None:
            raise ValueError("Entity must not be None.")
        if entity not in self.entities:
            self.entities.append(entity)
# @dataclass
# class Grid:
#     MIN_ROW_COUNT = 6
#     MIN_COLUMN_COUNT = 6
#
#     horizontal_movers: List[HorizontalMover] = field(default_factory=list)
#
#     cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
#     dimension: Dimension = field(
#         default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))
#
#     def __post_init__(self):
#         if not all([
#             self.dimension.height > self.MIN_ROW_COUNT,
#             self.dimension.length >        self.MIN_COLUMN_COUNT
#         ]):
#             raise ValueError("Grid dimensions below minimum values")
#
#         cells = tuple(
#             tuple(
#                 Cell(
#                     cell_id=row * self.dimension.length + col + 1,
#                     coordinate=GridCoordinate(row=row, column=col)
#                 )
#                 for col in range(self.dimension.length)
#             )
#             for row in range(self.dimension.height)
#         )
#         object.__setattr__(self, 'cells', cells)
#

    # def empty_cells(self) -> List[Cell]:
    #     empty_cells: List[Cell] = []
    #     for row in self.cells:
    #         for cell in row:
    #             if cell.occupant is None:
    #                 empty_cells.append(cell)
    #     return empty_cells
    #
    # def occupied_cells(self) -> List[Cell]:
    #     occupied_cells: List[Cell] = []
    #     for row in self.cells:
    #         for cell in row:
    #             if cell.occupant is not None:
    #                 occupied_cells.append(cell)
    #     return occupied_cells
    #
    # def find_cell_by_coordinate(self, coordinate: GridCoordinate) -> Optional[Cell]:
    #     if coordinate.row < 0 or coordinate.row >= self.dimension.height:
    #         return None
    #     if coordinate.column < 0 or coordinate.column >= self.dimension.length:
    #         return None
    #     return self.cells[coordinate.row][coordinate.column]
    #
    # def find_cell_by_id(self, cell_id: int) -> Optional[Cell]:
    #     for row in self.cells:
    #         for cell in row:
    #             if cell.cell_id == cell_id:
    #                 return cell
    #     return None
    #
    # def add_entity_to_grid(self, upper_left_coordinate: GridCoordinate, entity: GridEntity) -> Optional[GridEntity]:
    #     if upper_left_coordinate is None:
    #         raise ValueError("Coordinate cannot be None")
    #     if entity is None:
    #         raise ValueError("Entity cannot be None")
    #
    #     cells = self.get_cells_in_entity_area(upper_left_coordinate, entity)
    #     if cells is None:
    #         print("the cells is null")
    #     if len(cells) == 0:
    #         print("There are no cells available in the entity's area")
    #         return None
    #     if not self.are_destination_cells_empty(cells, entity):
    #         print("There are occupied cells in the destination area")
    #         return None
    #
    #     for cell in cells:
    #         cell.enter_cell(entity)
    #     entity.coordinate = upper_left_coordinate
    #     return entity
    #
    # def move_entity(self, destination_coordinate: GridCoordinate, entity: GridEntity) -> Optional[GridEntity]:
    #     if destination_coordinate is None:
    #         raise ValueError("Coordinate cannot be None")
    #     if entity is None:
    #         raise ValueError("Entity cannot be None")
    #
    #     destination_cells = self.get_cells_in_entity_area(destination_coordinate, entity)
    #     if len(destination_cells) == 0:
    #         print("There is no cells for moving into.")
    #         return None
    #     print("DESTINATION CELLS\n", destination_cells)
    #
    #     result = self.are_destination_cells_empty(destination_cells, entity)
    #     print("result", result)
    #     if not result:
    #         print("There are occupied cells in the destination area")
    #         return None
    #
    #     if result:
    #         print("the destination cells are unoccupied", entity, "is leaving its cells")
    #         for cell in list(entity.cells):
    #             print(cell.occupant, "is leaving", cell.coordinate)
    #             cell.leave_cell()
    #             if cell.occupant is None:
    #                 print("cell", cell.cell_id, "cell has no occupant")
    #             else :
    #                 print("cell", cell.cell_id, "cell still has occupant is", cell.occupant)
    #                 return None
    #
    #         print("moving", entity, "to", destination_coordinate)
    #         for cell in destination_cells:
    #             if cell.occupant is None:
    #                 cell.enter_cell(entity)
    #                 print("cell", cell.cell_id, "has occupant", entity)
    #             if (cell.occupant is not None) and (cell.occupant != entity):
    #                 print("cell", cell.cell_id, "already occupied by", cell.occupant)
    #                 return None
    #         entity.coordinate = destination_coordinate
    #         return entity
    #
    #
    # def random_empty_cell(self) -> Optional[Cell]:
    #     return random.choice(self.empty_cells())
    #
    # def are_destination_cells_empty(self, destination_cells: List[Cell], entity: GridEntity) -> bool:
    #     if destination_cells is None:
    #         raise Exception("the array of destination cells is null")
    #
    #     for cell in destination_cells:
    #         if cell.occupant is not None:
    #             print("destination cell:", cell, "is not empty. cannot move here" )
    #             return False
    #     print("the destination cells are empty. can move here")
    #     return True
    #
    # def get_cells_in_entity_area(self, upper_left_coordinate: GridCoordinate, entity: GridEntity) -> List[Cell]:
    #     if upper_left_coordinate is None:
    #         raise ValueError("Coordinate cannot be None")
    #     if entity is None:
    #         raise ValueError("Entity cannot be None")
    #
    #     cells = []
    #     if upper_left_coordinate.column + entity.dimension.length > self.dimension.length:
    #         print("Cannot traverse left beyond the grid")
    #         return cells
    #     if upper_left_coordinate.row + entity.dimension.height > self.dimension.height:
    #         print("Cannot traverse up beyond the grid")
    #         return cells
    #
    #     for row in range(upper_left_coordinate.row, upper_left_coordinate.row + entity.dimension.height):
    #         for col in range(upper_left_coordinate.column, upper_left_coordinate.column + entity.dimension.length):
    #             cell = self.find_cell_by_coordinate(GridCoordinate(row=row, column=col))
    #             if cell is not None:
    #                 print(cell.__str__(), " is in destination area", entity.dimension.area())
    #                 cells.append(cell)
    #             else:
    #                 print("no cell exists at this location")
    #     return cells
    #
    # def add_horizontal_mover(self, mover: HorizontalMover) -> Optional[HorizontalMover]:
    #     cell = self.random_empty_cell()
    #     print("randomly selected cell", cell)
    #     print("horizontal mover dimension", mover.dimension, " mover area=", mover.dimension.area())
    #     if cell is None:
    #         print("No place for mover")
    #         return None
    #
    #     entity = self.add_entity_to_grid(self.random_empty_cell().coordinate, mover)
    #     if entity is None:
    #         print("No place for mover")
    #         return None
    #     if not isinstance(entity, HorizontalMover):
    #         print("Mover is not horizontal")
    #         return None
    #     if isinstance(entity, HorizontalMover):
    #         placed_mover = cast(HorizontalMover, entity)
    #         self.horizontal_movers.append(placed_mover)
    #         return placed_mover
    #     return None
    #
    # def random_mover(self) -> Optional[HorizontalMover]:
    #     if len(self.horizontal_movers) == 0:
    #         return None
    #     return random.choice(self.horizontal_movers)
