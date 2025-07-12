from dataclasses import dataclass, field

from typing import Tuple, List, Optional

from exception import InvalidIdError
from geometry import Dimension, GridCoordinate
from grid_entity import GridEntity, Mover

from constants import Config
from id_factory import global_id_generator


@dataclass
class Cell:
    id: int
    coordinate: GridCoordinate
    occupant: Optional['GridEntity'] = field(default=None)

    def __post_init__(self):
        object.__setattr__(self, 'mover_id', self.id)
        object.__setattr__(self, 'top_left_coordinate', self.coordinate)
        object.__setattr__(self, 'occupant', self.occupant)

@dataclass
class Board:
    MIN_ROW_COUNT = 6
    MIN_COLUMN_COUNT = 6

    entities: List[Mover] = field(default_factory=list)
    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=Config.COLUMN_COUNT, height=Config.ROW_COUNT)
    )

    def __post_init__(self):
        if not all([
            self.dimension.height > self.MIN_ROW_COUNT,
            self.dimension.length > self.MIN_COLUMN_COUNT
        ]):
            raise ValueError("Board dimensions below minimum values")

        cells = tuple(
            tuple(
                Cell(
                    id=row * self.dimension.length + col + 1,
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
        if grid_entity.top_left_coordinate is not None:
            raise Exception("Entity already has a top_left_coordinate")
        cell = self.cells[upper_left_coordinate.row][upper_left_coordinate.column]
        if cell.occupant is not None:
            raise Exception("Cell already occupied")

        cell.enter_cell(grid_entity)

        return grid_entity


@dataclass
class Board:
    MIN_ROW_COUNT = 6
    MIN_COLUMN_COUNT = 6

    entities: List[GridEntity] = field(default_factory=list)

    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=Config.COLUMN_COUNT, height=Config.ROW_COUNT))

    def __post_init__(self):
        if not all([
            self.dimension.height > self.MIN_ROW_COUNT,
            self.dimension.length > self.MIN_COLUMN_COUNT
        ]):
            raise ValueError("Board dimensions below minimum values")

        cells = tuple(
            tuple(
                Cell(
                    id=global_id_generator.next_cell_id(),
                    coordinate=GridCoordinate(row=row, column=col)
                )
                for col in range(self.dimension.length)
            )
            for row in range(self.dimension.height)
        )
        object.__setattr__(self, 'cells', cells)

    def get_mover_by_id(self, mover_id: int) -> Optional[GridEntity]:
        for entity in self.entities:
            print(entity)
            if entity.id == mover_id:
                return entity
        return None

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

    def get_cells_occupied_by_entity(self, entity: GridEntity) -> List[Cell]:
        if entity is None:
            return []

        occupied_cells = []
        for row in self.cells:
            for cell in row:
                if cell.occupant == entity:
                    occupied_cells.append(cell)
        return occupied_cells

    def remove_entity_from_cells(self, entity: GridEntity) -> None:
        if entity is None:
            raise ValueError("Entity not found on the board. cannot remove a non-existent mover.")

        target_cells = self.get_cells_occupied_by_entity(entity)
        for cell in target_cells:
            if cell.occupant == entity:
                cell.occupant = None

    def add_entity_to_area(self, entity: GridEntity, top_left_coordinate: GridCoordinate) -> None:

        if top_left_coordinate is None:
            raise ValueError("Cannot add mover to an area without a top-left top_left_coordinate.")

        if entity is None:
            raise ValueError("Entity not found on the board. cannot add a non-existent mover.")

        if entity is None or top_left_coordinate is None:
            raise ValueError("Entity and top_left_coordinate must not be None.")

        target_cells = self.get_cells_by_area(top_left_coordinate, entity.dimension)

        for cell in target_cells:
            cell.occupant = entity
        entity.top_left_coordinate = top_left_coordinate

    def add_new_entity(self, top_left_coordinate: GridCoordinate, entity: GridEntity) -> Optional[GridEntity]:
        if top_left_coordinate is None or entity is None:
            raise ValueError("Top-left top_left_coordinate and mover must not be None.")

        # Bounds check
        if top_left_coordinate.row + entity.dimension.height > self.dimension.height:
            raise Exception("Entity does not fit within board bounds at the specified top_left_coordinate.")

        if top_left_coordinate.column + entity.dimension.length > self.dimension.length:
            raise Exception("Entity does not fit within board bounds at the specified top_left_coordinate.")

        if not self.can_entity_move_to_cells(entity, top_left_coordinate):
            raise Exception("Entity cannot move to the specified top_left_coordinate.")

        self.register_new_entity(entity)
        self.add_entity_to_area(entity, top_left_coordinate)


        return entity

    def move_entity(self, upper_left_destination: GridCoordinate, entity: GridEntity) -> Optional[GridEntity]:
        if upper_left_destination is None:
            raise ValueError("Destination top_left_coordinate must not be None.")

        if entity is None:
            raise ValueError("Entity does not exist. in the board. cannot move a non-existent mover.")

        if not self.can_entity_move_to_cells(entity, upper_left_destination):
            print("Entity", entity.id,  "cannot move to", upper_left_destination)
            return None

        self.remove_entity_from_cells(entity)
        self.add_entity_to_area(entity, upper_left_destination)
        return entity

    def remove_entity(self, entity: GridEntity) -> None:
        if entity is None:
            raise ValueError("Entity does not exist. in the board. cannot remove a non-existent mover.")
        self.remove_entity_from_cells(entity)
        self.entities.remove(entity)

    def can_entity_move_to_cells(self, entity: GridEntity, new_top_left_coordinate: GridCoordinate) -> bool:
        if entity is None or new_top_left_coordinate is None:
            raise ValueError("Entity and coordinate must not be None.")

        if (new_top_left_coordinate.row < 0 or new_top_left_coordinate.column < 0 or
                new_top_left_coordinate.row + entity.dimension.height > self.dimension.height or
                new_top_left_coordinate.column + entity.dimension.length > self.dimension.length):
            return False


        entity_height = entity.dimension.height
        entity_length = entity.dimension.length

        # Top-left (already have this as new_top_left_coordinate)
        top = new_top_left_coordinate.row
        left = new_top_left_coordinate.column

        # Bottom-right
        bottom = top + entity_height - 1
        right = left + entity_length - 1

        # Boundary checks (all must be True)
        if not (0 <= top < self.dimension.height and
                0 <= left < self.dimension.length and
                0 <= bottom < self.dimension.height and
                0 <= right < self.dimension.length):
            return False

        # Collision detection (now using proper boundaries)
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                cell = self.cells[r][c]
                if cell.occupant is not None and cell.occupant != entity:
                    return False
        return True

    def register_new_entity(self, entity: GridEntity) -> None:
        if entity is None:
            raise ValueError("Entity must not be None.")

        if entity not in self.entities:
            self.entities.append(entity)
# @dataclass
# class Board:
#     MIN_ROW_COUNT = 6
#     MIN_COLUMN_COUNT = 6
#
#     entities: List[HorizontalMover] = field(default_factory=list)
#
#     cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
#     dimension: Dimension = field(
#         default_factory=lambda: Dimension(length=Config.COLUMN_COUNT, height=Config.ROW_COUNT))
#
#     def __post_init__(self):
#         if not all([
#             self.dimension.height > self.MIN_ROW_COUNT,
#             self.dimension.length >        self.MIN_COLUMN_COUNT
#         ]):
#             raise ValueError("Board dimensions below minimum values")
#
#         cells = tuple(
#             tuple(
#                 Cell(
#                     mover_id=row * self.dimension.length + col + 1,
#                     top_left_coordinate=GridCoordinate(row=row, column=col)
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
    # def find_cell_by_coordinate(self, top_left_coordinate: GridCoordinate) -> Optional[Cell]:
    #     if top_left_coordinate.row < 0 or top_left_coordinate.row >= self.dimension.height:
    #         return None
    #     if top_left_coordinate.column < 0 or top_left_coordinate.column >= self.dimension.length:
    #         return None
    #     return self.cells[top_left_coordinate.row][top_left_coordinate.column]
    #
    # def find_cell_by_id(self, mover_id: int) -> Optional[Cell]:
    #     for row in self.cells:
    #         for cell in row:
    #             if cell.mover_id == mover_id:
    #                 return cell
    #     return None
    #
    # def add_entity_to_grid(self, upper_left_coordinate: GridCoordinate, mover: GridEntity) -> Optional[GridEntity]:
    #     if upper_left_coordinate is None:
    #         raise ValueError("Coordinate cannot be None")
    #     if mover is None:
    #         raise ValueError("Entity cannot be None")
    #
    #     cells = self.get_cells_in_entity_area(upper_left_coordinate, mover)
    #     if cells is None:
    #         print("the cells is null")
    #     if len(cells) == 0:
    #         print("There are no cells available in the mover's area")
    #         return None
    #     if not self.are_destination_cells_empty(cells, mover):
    #         print("There are occupied cells in the destination area")
    #         return None
    #
    #     for cell in cells:
    #         cell.enter_cell(mover)
    #     mover.top_left_coordinate = upper_left_coordinate
    #     return mover
    #
    # def move_entity(self, destination_coordinate: GridCoordinate, mover: GridEntity) -> Optional[GridEntity]:
    #     if destination_coordinate is None:
    #         raise ValueError("Coordinate cannot be None")
    #     if mover is None:
    #         raise ValueError("Entity cannot be None")
    #
    #     destination_cells = self.get_cells_in_entity_area(destination_coordinate, mover)
    #     if len(destination_cells) == 0:
    #         print("There is no cells for moving into.")
    #         return None
    #     print("DESTINATION CELLS\n", destination_cells)
    #
    #     result = self.are_destination_cells_empty(destination_cells, mover)
    #     print("result", result)
    #     if not result:
    #         print("There are occupied cells in the destination area")
    #         return None
    #
    #     if result:
    #         print("the destination cells are unoccupied", mover, "is leaving its cells")
    #         for cell in list(mover.cells):
    #             print(cell.occupant, "is leaving", cell.top_left_coordinate)
    #             cell.leave_cell()
    #             if cell.occupant is None:
    #                 print("cell", cell.mover_id, "cell has no occupant")
    #             else :
    #                 print("cell", cell.mover_id, "cell still has occupant is", cell.occupant)
    #                 return None
    #
    #         print("moving", mover, "to", destination_coordinate)
    #         for cell in destination_cells:
    #             if cell.occupant is None:
    #                 cell.enter_cell(mover)
    #                 print("cell", cell.mover_id, "has occupant", mover)
    #             if (cell.occupant is not None) and (cell.occupant != mover):
    #                 print("cell", cell.mover_id, "already occupied by", cell.occupant)
    #                 return None
    #         mover.top_left_coordinate = destination_coordinate
    #         return mover
    #
    #
    # def random_empty_cell(self) -> Optional[Cell]:
    #     return random.choice(self.empty_cells())
    #
    # def are_destination_cells_empty(self, destination_cells: List[Cell], mover: GridEntity) -> bool:
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
    # def get_cells_in_entity_area(self, upper_left_coordinate: GridCoordinate, mover: GridEntity) -> List[Cell]:
    #     if upper_left_coordinate is None:
    #         raise ValueError("Coordinate cannot be None")
    #     if mover is None:
    #         raise ValueError("Entity cannot be None")
    #
    #     cells = []
    #     if upper_left_coordinate.column + mover.dimension.length > self.dimension.length:
    #         print("Cannot traverse left beyond the board")
    #         return cells
    #     if upper_left_coordinate.row + mover.dimension.height > self.dimension.height:
    #         print("Cannot traverse up beyond the board")
    #         return cells
    #
    #     for row in range(upper_left_coordinate.row, upper_left_coordinate.row + mover.dimension.height):
    #         for col in range(upper_left_coordinate.column, upper_left_coordinate.column + mover.dimension.length):
    #             cell = self.find_cell_by_coordinate(GridCoordinate(row=row, column=col))
    #             if cell is not None:
    #                 print(cell.__str__(), " is in destination area", mover.dimension.area())
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
    #     mover = self.add_entity_to_grid(self.random_empty_cell().top_left_coordinate, mover)
    #     if mover is None:
    #         print("No place for mover")
    #         return None
    #     if not isinstance(mover, HorizontalMover):
    #         print("Mover is not horizontal")
    #         return None
    #     if isinstance(mover, HorizontalMover):
    #         placed_mover = cast(HorizontalMover, mover)
    #         self.entities.append(placed_mover)
    #         return placed_mover
    #     return None
    #
    # def random_mover(self) -> Optional[HorizontalMover]:
    #     if len(self.entities) == 0:
    #         return None
    #     return random.choice(self.entities)
