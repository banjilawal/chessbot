import random
from typing import Union, Dict

from common.direction import Direction
from model.grid import Grid
from model.bin import Bin
from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from model.vault import VerticalMover, HorizontalMover
from model.crate import Crate


class Generator:
    def random_dimension(self, max_length: int, max_height: int) -> Dimension:
        return Dimension(
            length=random.randint(1, max_length),
            height=random.randint(1, max_height)
        )

    def random_crate(self, max_length: int) -> Crate:
        return Crate(
            id=global_id_generator.next_crate_id(),
            length=random.randint(1, max_length),
            coordinate=None
        )
        # print(f"created crate with cell_id: {ladder.cell_id}, dimension: {ladder.dimension}, area: {ladder.dimension.area()}")
        # return ladder

    def random_rack(self, max_height: int) -> Bin:
        return Bin(
            rack_id=global_id_generator.next_rack_id(),
            height=random.randint(1, max_height),
            coordinate=None
        )

    def random_vertical_vault(self, max_height: int) -> VerticalMover:
        return VerticalMover(
            mover_id=global_id_generator.next_vault_id(),
            height=random.randint(2, max_height),
            coordinate=None
        )

    def random_horizontal_vault(self, max_length: int) -> HorizontalMover:
        return HorizontalMover(
            mover_id=global_id_generator.next_vault_id(),
            length=random.randint(2, max_length),
            coordinate=None
        )

    def racks(self, max_height:int, count: int) -> list[Bin]:
        racks: list[Bin] = []
        for _ in range(count):
            racks.append(self.random_rack(max_height))
        return racks

    def horizontal_vaults(self, max_length: int, count: int) -> list[HorizontalMover]:
        vaults: list[HorizontalMover] = []
        for _ in range(count):
            vaults.append(self.random_horizontal_vault(max_length))
        return vaults

    def vertical_vaults(self, max_height: int, count: int) -> list[VerticalMover]:
        vaults: list[VerticalMover] = []
        for _ in range(count):
            vaults.append(self.random_vertical_vault(max_height))
        return vaults

    def board(
            self,
            dimension=Dimension(21, 21),
            max_array_length: int = 7,
            dictionary_size: int = 20,
            max_height=7,
            max_length=7
    ) -> Grid:
        board = Grid()
        board.place_horizontal_vaults_randomly(self.horizontal_vaults(max_length=max_length, count=10)        )
        board.place_vertical_vaults_randomly(self.vertical_vaults(max_height=max_height, count=10))
        board.place_racks_randomly(self.racks(max_height=max_height, count=max_array_length))
        return board


