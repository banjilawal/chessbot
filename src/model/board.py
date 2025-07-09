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
from model.rack import Rack
from model.vault import VerticalVaults, HorizontalVaults
from model.portal.portal import Portal
from src.common.game_default import GameDefault
from model.cell import Cell


class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    door: Portal = field(default_factory=lambda: Door(id=global_id_generator.next_portal_id(), coordinate=None))
    vertical_vaults: Dict[int, VerticalVaults] = field(default_factory=dict)
    horizontal_vaults: Dict[int, HorizontalVaults] = field(default_factory=dict)
    crate: Crate = Crate(crate_id=1, coordinate=Nome)
    racks: List[Rack] = field(default_factory=list)
    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def _set_crate_coordinates(self) -> Crate:
        middle_column = self.dimension.length // 2
        if self.dimension.length % 2 == 0:
            coordinate = GridCoordinate(row=1, column=middle_column)
        else:
            coordinate = GridCoordinate(row=1, column=middle_column + 1)

        return Crate(id=1, coordinate=coordinate)


    def __post_init__(self):
        if not all([
            self.dimension.height >= self.MIN_ROW_COUNT,
            self.dimension.length >= self.MIN_COLUMN_COUNT
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

    def place_racks_randomly(self, racks: List[Rack]) -> None:
        for rack in racks:
            attempts = 0
            max_attempts = 10  # Limit attempts to avoid infinite loops
            placed = False

            while not placed and attempts < max_attempts:
                # Calculate maximum valid row and column positions
                max_row = self.dimension.height - rack.dimension.height
                max_col = self.dimension.length - rack.dimension.length

                if max_row < 0 or max_col < 0:
                    # Rack is too big for the board, skip it
                    break

                # Generate random coordinates
                row = random.randint(0, max_row)
                col = random.randint(0, max_col)
                coordinate = GridCoordinate(row=row, column=col)

                # Check if there's enough space for the rack
                if self._space_is_available(rack.dimension, coordinate):
                    # Try to position the rack
                    positioned_rack = self.position_rack(rack, coordinate)
                    if positioned_rack is not None:
                        # Set rack as occupant for all cells it covers
                        for r in range(coordinate.row, coordinate.row + rack.dimension.height):
                            for c in range(coordinate.column, coordinate.column + rack.dimension.length):
                                self.cells[r][c].occupant = positioned_rack
                        placed = True

                attempts += 1

    def place_vertical_vaults_randomly(self, vaults: List[VerticalVaults]) -> None:
        for vault in vaults:
            attempts = 0
            max_attempts = 10  # Limit attempts to avoid infinite loops
            placed = False

            while not placed and attempts < max_attempts:
                # Calculate maximum valid row and column positions
                max_row = self.dimension.height - vault.dimension.height
                max_col = self.dimension.length - vault.dimension.length

                if max_row < 0 or max_col < 0:
                    # Vault is too big for the board, skip it
                    break

                # Generate random coordinates
                row = random.randint(0, max_row)
                col = random.randint(0, max_col)
                coordinate = GridCoordinate(row=row, column=col)

                # Check if there's enough space for the vault and space above for growth
                if (self._space_is_available(vault.dimension, coordinate) and
                        row >= vault.dimension.height):  # Ensure space above for vertical growth
                    # Try to position the vault
                    positioned_vault = self.position_vertical_vaults(vault, coordinate)
                    if positioned_vault is not None:
                        for r in range(coordinate.row, coordinate.row - vault.dimension.height, -1):
                            self.cells[r][coordinate.column].occupant = positioned_vault

                        next_key = len(self.vertical_vaults) + 1
                        self.vertical_vaults[next_key] = positioned_vault
                        placed = True

                attempts += 1

    def place_horizontal_vaults_randomly(self, vaults: List[HorizontalVaults]) -> None:
        """
        Places horizontal vaults randomly on the board and adds them to the horizontal_vaults dictionary.
        Each vault is placed in a random valid position or skipped if no valid position is found.
        Sets the vault as the occupant for all cells it covers.

        Args:
            vaults: List[HorizontalVaults] objects to be placed
        """
        for vault in vaults:
            attempts = 0
            max_attempts = 10  # Limit attempts to avoid infinite loops
            placed = False

            while not placed and attempts < max_attempts:
                # Calculate maximum valid row and column positions
                max_row = self.dimension.height - vault.dimension.height
                max_col = self.dimension.length - vault.dimension.length

                if max_row < 0 or max_col < 0:
                    # Vault is too big for the board, skip it
                    break

                # Generate random coordinates
                row = random.randint(0, max_row)
                col = random.randint(0, max_col)
                coordinate = GridCoordinate(row=row, column=col)

                # Check if there's enough space for the vault and space to the right for growth
                if (self._space_is_available(vault.dimension, coordinate) and
                        col + vault.dimension.length <= self.dimension.length):  # Ensure space to the right for horizontal growth
                    # Try to position the vault
                    positioned_vault = self.position_horizontal_vaults(vault, coordinate)
                    if positioned_vault is not None:
                        # Set vault as occupant for all cells it covers horizontally
                        for c in range(coordinate.column, coordinate.column + vault.dimension.length):
                            self.cells[coordinate.row][c].occupant = positioned_vault

                        # Add to horizontal_vaults dictionary with next available key
                        next_key = len(self.horizontal_vaults) + 1
                        self.horizontal_vaults[next_key] = positioned_vault
                        placed = True

                attempts += 1

    def __position_grid_entity(
            self,
            entity: GridEntity,
            top_left_coordinate: GridCoordinate
    ) -> Optional[GridEntity]:
        if not self._check_space_available(entity.dimension, top_left_coordinate):
            return None

        entity.position = top_left_coordinate
        for row in range(top_left_coordinate.row, top_left_coordinate.row + entity.dimension.height):
            for col in range(top_left_coordinate.column, top_left_coordinate.column + entity.dimension.width):
                self.occupied_cells.add(GridCoordinate(row=row, column=col))

        return entity

    def _space_is_available(self, dimension: Dimension, top_left_coordinate: GridCoordinate) -> bool:
        # Early boundary check
        if (top_left_coordinate.row + dimension.height > self.height or
                top_left_coordinate.column + dimension.width > self.width):
            return False

        for row in range(top_left_coordinate.row, top_left_coordinate.row + dimension.height):
            for col in range(top_left_coordinate.column, top_left_coordinate.column + dimension.width):
                coord = GridCoordinate(row=row, column=col)
                if not self._is_valid_coordinate(coord) or self._is_cell_occupied(coord):
                    return False
        return True

    def print(self):
        """Print the board with cell IDs"""
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")
            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.id:^3}" for cell in row) + "|")
        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")