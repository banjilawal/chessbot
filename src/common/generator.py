import random

from common.direction import Direction
from model.board import Board
from model.rack import Rack
from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from model.vault import Vault, VaultGroup
from model.crate import Crate


class Generator:
    def random_dimension(self, max_length: int, max_height: int) -> Dimension:
        return Dimension(
            length=random.randint(1, max_length),
            height=random.randint(1, max_height)
        )

    def generate_boulder(self, max_length: int, max_height: int) -> Vault:
        boulder = Vault(
            id=global_id_generator.next_vault_id(),
            dimension=self.random_dimension(max_length, max_height),
        )
        print(f"created boulder with id: {boulder.id}, dimension: {boulder.dimension}, area: {boulder.dimension.area()}")
        return boulder

    def generate_boulders(self, max_length: int, max_height:int, count: int) -> list[Vault]:
        return [self.generate_boulder(max_length, max_height) for _ in range(count)]

    def random_crate(self, max_length: int) -> Crate:
        return Crate(
            id=global_id_generator.next_crate_id(),
            length=random.randint(1, max_length),
            coordinate=None
        )
        # print(f"created crate with id: {ladder.id}, dimension: {ladder.dimension}, area: {ladder.dimension.area()}")
        # return ladder

    def crates(self, max_length:int, count: int) -> list[Crate]:
        crates: list[Crate] = []
        for _ in range(count):
            crates.append(self.random_crate(max_length))
        return crates

    def random_rack(self, max_height: int) -> Rack:
        return Rack(
            id=global_id_generator.next_rack_id(),
            height=random.randint(1, max_height),
            coordinate=None
        )
        # print(f"created crate with id: {ladder.id}, dimension: {ladder.dimension}, area: {ladder.dimension.area()}")
        # return ladder

    def racks(self, max_height:int, count: int) -> list[Rack]:
        racks: list[Rack] = []
        for _ in range(count):
            racks.append(self.random_rack(max_height))
        return racks

    def random_vault_group(self) -> VaultGroup:
        return VaultGroup(
            id=global_id_generator.vault_group_id(),
            growth_direction=random.choice([Direction.DOWN, Direction.RIGHT])
        )

    def vault_groups(self, count: int) -> list[VaultGroup]:
        vault_groups: list[VaultGroup] = []
        for _ in range(count):
            vault_groups.append(self.random_vault_group())
        return vault_groups

    def board(
            self,
            length:int = 21,
            height:int = 21,
            max_crates:int = 20,
            max_racks:int = 20,
            max_vault_groups: int = 10,
            max_vault_group_length:int = 10
    ) -> Board:
        board: Board(Dimension(length=length, height=height))
        crates = self.crates(max_length=8, count=max_crates)
        racks = self.racks(max_height=10, count=max_racks)
        vault_groups = self.vault_groups(count=max_vault_groups)

        board.add_vault_groups(vault_groups)
        board.add_crates(crates)
        board.add_racks(racks)

        board.add_boulders(self.generate_boulders(max_length=2, max_height=3, count=9))
        board.place_boulders_randomly()
        board.add_ladders(self.racks(max_height=3, count=9))
        board.place_ladders_randomly()
        return board
