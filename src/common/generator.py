import random
from typing import Union

from common.direction import Direction
from model.board import Board
from model.rack import Rack
from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from model.vault import Vault, VaultGroup, VaultArrayBuilder, VerticalVaults, VerticalVaultsDictionary, \
    HorizontalVaultsDictionary, HorizontalVaults
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

    def create_vaults(self, direction: Direction, length: int) -> Union[VerticalVaults, HorizontalVaults]:
        if direction in (Direction.UP, Direction.DOWN):
            build_direction = Direction.UP
            return VaultArrayBuilder.build(
                vault=Vault(vault_id=1),
                direction=build_direction,
                size=length
            )
        elif direction in (Direction.LEFT, Direction.RIGHT):
            build_direction = Direction.RIGHT  # VaultArrayBuilder only needs RIGHT
            return VaultArrayBuilder.build(
                vault=Vault(vault_id=1),
                direction=build_direction,
                size=length
            )
        else:
            raise ValueError("Direction must be UP, DOWN, LEFT, or RIGHT")

    def create_vaults_dictionary(
            self,
            direction: Direction,
            max_array_length: int = 10,
            dictionary_size: int = 10
    ) -> Union[VerticalVaultsDictionary, HorizontalVaultsDictionary]:
        if max_array_length < 2:
            raise ValueError("max_array_length must be at least 2")

        if direction in (Direction.UP, Direction.DOWN):
            dictionary = VerticalVaultsDictionary()
            build_direction = Direction.UP
        elif direction in (Direction.LEFT, Direction.RIGHT):
            dictionary = HorizontalVaultsDictionary()
            build_direction = Direction.RIGHT
        else:
            raise ValueError("Direction must be UP, DOWN, LEFT, or RIGHT")

        for i in range(dictionary_size):
            length = random.randint(2, max_array_length)

            vaults = VaultArrayBuilder.build(
                vault=Vault(vault_id=i + 1),  # Using index+1 as vault_id
                direction=build_direction,
                size=length
            )
            dictionary.add(i, vaults)

        return dictionary

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
            max_racks:int = 20,
            max_vertical_vaults:int = 10,
            max_horizontal_vaults:int = 10,
    ) -> Board:
        board: Board(Dimension(length=length, height=height))
        racks = self.racks(max_height=10, count=max_racks)
        horizontal_vaults = self.create_vaults_dictionary(max_array_length=max_horizontal_vaults, direction=Direction.DOWN)
        vertical_vaults = self.create_vaults_dictionary(max_array_length=max_vertical_vaults, direction=Direction.RIGHT)
        return board
