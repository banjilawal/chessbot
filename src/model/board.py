import random
from dataclasses import dataclass, field

from typing import Tuple, List, Optional, cast, Dict

from common.direction import Direction
from common.id_generator import global_id_generator
from exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.crate import Crate
from common.dimension import Dimension
from model.grid_entity import GridEntity
from model.portal.door import Door
from model.rack import Rack
from model.vault import Vault, VaultGroup, VerticalVaults, HorizontalVaults
from model.portal.portal import Portal
from src.common.game_default import GameDefault
from model.cell import Cell


@dataclass(frozen=True)
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    door: Portal = field(default_factory=lambda: Door(id=global_id_generator.next_portal_id(), coordinate=None))
    vaults: Dict[int, VaultGroup] = field(default_factory=dict)
    vertical_vaults: Dict[int, VerticalVaults] = field(default_factory=dict)
    horizontal_vaults: Dict[int, HorizontalVaults] = field(default_factory=dict)
    crates: List[Crate] = field(default_factory=list)
    racks: List[Rack] = field(default_factory=list)
    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(
        default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

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

        object.__setattr__(self, 'cells', cells)

    def row_count(self) -> int:
        return self.dimension.height

    def column_count(self) -> int:
        return self.dimension.length

    def add_boulder(self, boulder: Vault):
        self.vaults.append(boulder)

    def add_boulders(self, boulders: List[Vault]):

        self.vaults.extend(boulders)

    def position_crate(self, crate: Crate, coordinate: GridCoordinate) -> Optional[Crate]:
        self.crates.append(ladder)

    def add_ladders(self, ladders: List[Crate]):
        self.crates.extend(ladders)

    def are_occupied(self, top_left_coord: GridCoordinate, dimension: Dimension) -> bool:
        """
        Check if the cells starting from the top-left coordinate with the given dimension are occupied.
        """
        for row in range(top_left_coord.row, top_left_coord.row + dimension.height):
            for col in range(top_left_coord.column, top_left_coord.column + dimension.length):
                if self.cells[row][col].occupant is not None:
                    return True
        return False

    def place_boulders_randomly(self):
        placed_boulders = []
        for boulder in self.vaults:
            placed = False
            attempts = 0
            while not placed and attempts < 1:
                attempts += 1
                max_row = self.dimension.height - boulder.dimension.height
                max_col = self.dimension.length - boulder.dimension.length

                if max_row < 0 or max_col < 0:
                    # Vault is too big for the board, skip
                    print(f"Boulder {boulder.id} too big for the board, skipping.")
                    break

                row = random.randint(0, max_row)
                col = random.randint(0, max_col)
                coord = GridCoordinate(row=row, column=col)

                if not self.are_occupied(coord, boulder.dimension):
                    # Occupy cells and add boulder
                    cells_to_occupy = [
                        [self.cells[r][c] for c in range(col, col + boulder.dimension.length)]
                        for r in range(row, row + boulder.dimension.height)
                    ]
                    boulder.occupy_cells(coord, cells_to_occupy)
                    # self.vaults.append(boulder)
                    # print(f"Placed boulder {boulder.id} (area {boulder.dimension.area()}) at {coord}")
                    # placed = True
            #
            # if not placed:
            #     print(f"Failed to place boulder {boulder.id} after {max_attempts_per_boulder}

    def place_ladders_randomly(self):
        placed_boulders = []
        for ladder in self.crates:
            placed = False
            attempts = 0
            while not placed and attempts < 1:
                attempts += 1
                max_row = self.dimension.height -ladder.dimension.height
                max_col = self.dimension.length - ladder.dimension.length

                if max_row < 0 or max_col < 0:
                    # Vault is too big for the board, skip
                    print(f"Boulder {ladder.id} too big for the board, skipping.")
                    break

                row = random.randint(0, max_row)
                col = random.randint(0, max_col)
                coord = GridCoordinate(row=row, column=col)

                if not self.are_occupied(coord, ladder.dimension):
                    # Occupy cells and add boulder
                    cells_to_occupy = [
                        [self.cells[r][c] for c in range(col, col + ladder.dimension.length)]
                        for r in range(row, row + ladder.dimension.height)
                    ]
                    ladder.occupy_cells(coord, cells_to_occupy)
                    # self.crates.append(boulder)
                    # print(f"Placed boulder {boulder.id} (area {boulder.dimension.area()}) at {coord}")
                    # placed = True

    def position_crate(self, crate: Crate, top_left_coordinate: GridCoordinate) -> Optional[Crate]:
        entity = self.__position_grid_entity(crate, top_left_coordinate)

        if entity is not None and isinstance(entity, Crate):
            positioned_crate = cast(Crate, entity)
            self.crates.append(positioned_crate)
            return positioned_crate
        return None

    def position_rack(self, rack: Rack, top_left_coordinate: GridCoordinate) -> Optional[Rack]:
        entity = self.__position_grid_entity(rack, top_left_coordinate)

        if entity is not None and isinstance(entity, Rack):
            positioned_rack = cast(Rack, entity)
            self.racks.append(positioned_rack)
            return positioned_rack
        return None

    def position_vertical_vaults(self, starting_vault: Vault, starting_coordinate: GridCoordinate) -> Optional[VaultGroup]:
        entity = self.__position_grid_entity(starting_vault, starting_coordinate)

        if entity is not None and isinstance(entity, VerticalVaults):
            positioned_vault = cast(Vault, entity)
            vaults = [positioned_vault]
            for i in range(1, 5):
                vault = Vault(vault_id=global_id_generator.next_vault_id())
                coordinate = GridCoordinate(positioned_vault.coordinate.row + i, positioned_vault.coordinate.column)
                self.cells[coordinate.row][coordinate.column].occupant = vault
                vaults.append(vault)
            return vaults
        return None


    def position_horizontal_vaults(self, starting_vault: Vault, starting_coordinate: GridCoordinate) -> Optional[VaultGroup]:
        entity = self.__position_grid_entity(starting_vault, starting_coordinate)

        if entity is not None and isinstance(entity, HorizontalVaults):
            positioned_vault = cast(Vault, entity)
            max_vaults = self.dimension.length - positioned_vault.coordinate.column

            if max_vaults <= 0:
                return None

            total_new_vaults = random.randint(1, max_vaults)
            vaults = [positioned_vault]
            for i in total_new_vaults:
                vault = Vault(vault_id=global_id_generator.next_vault_id())
                coordinate = GridCoordinate(
                    positioned_vault.coordinate.row,
                    positioned_vault.coordinate.column + 1
                )
                self.cells[coordinate.row][coordinate.column].occupant = vault
                vaults.append(vault)
            key = len(self.vertical_vaults.keys()) + 1
            self.vertical_vaults[key] = vaults

            return vaults
        return None



    def position_vault_group(self, starting_vault: Vault, vault_group_direction: Direction, starting_coordinate: GridCoordinate) -> Optional[VaultGroup]:
        entity = self.__position_grid_entity(starting_vault, starting_coordinate)

        if entity is not None and isinstance(entity, Vault):
            positioned_vault = cast(Vault, entity)
            vault_group = VaultGroup(
                vault_group_id=global_id_generator.next_vault_group__id(),
                growth_direction=vault_group_direction
            )
            key = len(self.vaults) + 1
            self.vaults[key] = vault_group
            return vault_group
        return None

    def add_vaults(self, vault__group_id: int):
        max_growth_space = self._get_growth_space(vault__group_id)
        if max_growth_space == 0:
            return
        total_new_vaults = random.randint(1, max_growth_space)
        for i in range(total_new_vaults):
            vault_group = self.vaults[vault__group_id]
            vault_group.vaults.append(Vault(vault_id=global_id_generator.next_vault_id()))
            self.vaults[vault__group_id] = vault_group

    def _add_vertical_vault(self, vault_group_key: int):
        max_growth_space = self._get_growth_space(vault_group_key)

        if growth_space > 0:
            vault_group = self.vaults[vault_group_key]
            coordinate_bounds = self._coordinate_bounds(vault_group_key)
            total_new_vaults = random.randint(1, max_growth_space)

            for i in range(total_new_vaults):
                vault = Vault(vault_id=global_id_generator.next_vault_id())
                new_coordinate = GridCoordinate()
                vault_group = self.vaults[vault_group_key]
                vault_group.vaults.append(vault)
                self.vaults[vault_group_key] = vault_group
        vault_group = self.vaults[vault_group_key]
        if vault_group is None:
            return
        first_vault = vault_group[0]
        first_coordinate = first_vault.coordinate
        current_num_vaults = len(self.vaults[vault_group_key])

        if vault_group.growth_direction == Direction.RIGHT:
            last_coordinate = first_coordinate.column + first_vault.dimension.length - 1

    def _get_growth_space(self, vault_group_key: int) -> int:
        vaults = self.vaults[vault_group_key]
        if vaults is None:
            return 0

        coordinate_bounds = self._coordinate_bounds(vault_group_key)
        if coordinate_bounds is None:
            return 0

        if vaults.growth_direction == Direction.RIGHT:
            return self.dimension.length - coordinate_bounds.column.column - 1

        elif vaults.growth_direction == Direction.DOWN:
            return self.dimension.height - coordinate_bounds.row.row - 1
        else:
            return 0

        def _coordinate_range(self, entity: GridEntity) -> CoordinateRange:
            if entity is None:
                return None

            if isinstance(entity, Crate):
                first_coordinate = entity.coordinate
                last_coordinate = GridCoordinate(
                    row=first_coordinate.row,
                    column=first_coordinate.column + entity.dimension.length - 1
                )
                return CoordinateRange(first_coordinate=first_coordinate, last_coordinate=last_coordinate)

            if isinstance(entity, Rack):
                first_coordinate = entity.coordinate
                last_coordinate = GridCoordinate(
                    row=first_coordinate.row + entity.dimension.height - 1,
                    column=first_coordinate.column
                )
                return CoordinateRange(first_coordinate=first_coordinate, last_coordinate=last_coordinate)

            if isinstance(entity, Vault):
                first_coordinate = entity.coordinate
                last_coordinate = GridCoordinate(
                    row=first_coordinate.row + entity.dimension.height - 1,
                    column=first_coordinate.column + entity.dimension.length - 1
                )



















        if
        available_vault_space =

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