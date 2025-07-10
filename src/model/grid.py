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

    door: Portal = field(default_factory=lambda: Door(id=global_id_generator.next_portal_id(), coordinate=None))
    vertical_vaults: List[VerticalMover] = field(default_factory=list)
    horizontal_vaults: List[HorizontalMover] = field(default_factory=list)
    crate: Crate = field(default_factory=lambda: Crate(crate_id=1, coordinate=None))
    racks: List[Bin] = field(default_factory=list)
    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def _set_crate_coordinates(self):
        middle_column = self.dimension.length // 2
        if self.dimension.length % 2 == 0:
            coordinate = GridCoordinate(row=1, column=middle_column)
        else:
            coordinate = GridCoordinate(row=1, column=middle_column + 1)

        return Crate(crate_id=1, coordinate=coordinate)

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

    def row_count(self) -> int:
        return self.dimension.height

    def column_count(self) -> int:
        return self.dimension.length

    def are_occupied(self, top_left_coord: GridCoordinate, dimension: Dimension) -> bool:
        """
        Check if the cells starting from the top-left coordinate with the given dimension are occupied.
        """
        for row in range(top_left_coord.row, top_left_coord.row + dimension.height):
            for col in range(top_left_coord.column, top_left_coord.column + dimension.length):
                if self.cells[row][col].occupant is not None:
                    return True
        return False

    def place_racks_randomly(self, racks: List[Bin]) -> None:
        for rack in racks:
            coordinate = self.rand_coordinate()
            if self.has_enough_space(coordinate, rack.dimension):  # Changed from _space_is_available to has_enough_space
                    for r in range(coordinate.row, coordinate.row + rack.dimension.height):
                        self.cells[r][coordinate.column].occupant = rack
                    self.racks.append(rack)
    #
    # def place_horizontal_vaults_randomly(self, vaults: List[HorizontalMover]) -> None:
    #     for vault in vaults:
    #
    #         while not placed and attempts < max_attempts:
    #             # Calculate maximum valid row and column positions
    #             max_row = self.dimension.row - 1  # height is always 1
    #             max_col = self.dimension.length - vault.dimension.length
    #
    #             if max_col < 0:
    #                 # Vault is too long for the board, skip it
    #                 break
    #
    #             # Generate random coordinates
    #             row = random.randint(0, max_row)
    #             col = random.randint(0, max_col)
    #             coordinate = GridCoordinate(row=row, column=col)
    #
    #             # Check if there's enough space for the vault
    #             if self.has_enough_space(dimension=vault.dimension, coordinate=coordinate):
    #                 # Try to position the vault
    #                 positioned_vault = self.position_vault(vault, coordinate)
    #                 if positioned_vault is not None:
    #                     # Set vault as occupant for all cells it covers
    #                     for c in range(coordinate.column, coordinate.column + vault.dimension.length):
    #                         self.cells[coordinate.row][c].occupant = positioned_vault
    #                     placed = True
    #
    #             attempts += 1

    def place_vertical_vaults_randomly(self, vaults: List[VerticalMover]) -> None:
        for vault in vaults:
            coordinate = self.rand_coordinate()
            if self.has_enough_space(coordinate, vault.dimension):  # Changed from _space_is_available to has_enough_space
                positioned_vault = self.position_vault(vault, coordinate)
                if positioned_vault is not None:
                    for r in range(coordinate.row, coordinate.row + vault.dimension.height):
                        self.cells[r][coordinate.column].occupant = positioned_vault
                    self.vertical_vaults.append(positioned_vault)

    def _covered_cells(self, top_left_coord: GridCoordinate, dimension: Dimension) -> List[Cell]:
        """Returns list of cells covered by an entity based on its dimensions and top-left coordinate"""
        cells = []
        # Check if the entity would fit within board boundaries
        if (top_left_coord.row + dimension.height > self.dimension.height or
                top_left_coord.column + dimension.length > self.dimension.length):
            raise ValueError("Entity placement exceeds board boundaries")

        for row in range(dimension.height):
            for col in range(dimension.length):
                cells.append(self.cells[top_left_coord.row + row][top_left_coord.column + col])
        return cells

    def _assign_cells(self, top_left_coord: GridCoordinate, entity: GridEntity) -> None:
        """Assigns entity to all cells it covers"""
        for cell in self._covered_cells(top_left_coord, entity.dimension):
            cell.occupant = entity

    def place_horizontal_vaults_randomly(self, vaults: List[HorizontalMover]) -> None:
        for vault in vaults:
            attempts = 0
            max_attempts = 10
            while attempts < max_attempts:
                coordinate = self.rand_coordinate()
                if self.has_enough_space(coordinate, vault.dimension):
                    self._assign_cells(coordinate, vault)
                    self.horizontal_vaults.append(vault)
                    break
                attempts += 1

    def rand_coordinate(self) -> GridCoordinate:
        """Returns coordinates of a random cell on the board"""
        return GridCoordinate(
            row=random.randint(0, self.dimension.height - 1),
            column=random.randint(0, self.dimension.length - 1)
        )

    def has_enough_space(self, top_left_coord: GridCoordinate, dimension: Dimension) -> bool:
        # Check board boundaries
        if (top_left_coord.row + dimension.height > self.dimension.height or
                top_left_coord.column + dimension.length > self.dimension.length):
            return False

        # Check if all required cells are unoccupied
        for row in range(top_left_coord.row, top_left_coord.row + dimension.height):
            for col in range(top_left_coord.column, top_left_coord.column + dimension.length):
                if self.cells[row][col].occupant is not None:
                    return False

    def print(self):
        """Print the board with cell IDs"""
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")
            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.cell_id:^3}" for cell in row) + "|")
        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")

def print_info(self) -> None:
    """
    Prints information about all racks and vaults placed on the board.
    Includes:
    - All racks
    - All horizontal vaults from the horizontal_vaults dictionary
    - All vertical vaults from the vertical_vaults dictionary
    """
    # Print racks information
    print("\n=== Racks ===")
    for rack in self.racks.values():
        rack.print_info()

    # Print horizontal vaults information
    print("\n=== Horizontal Vaults ===")
    if self.horizontal_vaults:
        for vault_id, vault in self.horizontal_vaults.items():
            vault.print_info()
    else:
        print("No horizontal vaults placed")

    # Print vertical vaults information
    print("\n=== Vertical Vaults ===")
    if self.vertical_vaults:
        for vault_id, vault in self.vertical_vaults.items():
            vault.print_info()
    else:
        print("No vertical vaults placed")
