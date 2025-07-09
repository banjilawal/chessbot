import random
from dataclasses import dataclass, field

from typing import Tuple, List

from common.id_generator import global_id_generator
from exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from model.grid_coordinate import GridCoordinate
from model.crate import Crate
from common.dimension import Dimension
from model.portal.door import Door
from model.rack import Rack
from model.vault import Vault
from model.portal.portal import Portal
from src.common.game_default import GameDefault
from model.cell import Cell


@dataclass(frozen=True)
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    door: Portal = field(default_factory=lambda: Door(id=global_id_generator.next_portal_id(), coordinate=None))
    vaults: List[Vault] = field(default_factory=list)
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

    def add_ladder(self, ladder: Crate):
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

    def print(self):
        """Print the board with cell IDs"""
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")
            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.id:^3}" for cell in row) + "|")
        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")