import random

from model.rack import Rack
from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from model.vault import Vault
from model.crate import Crate


class GridEntityGenerator:
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
        return Crate(id=global_id_generator.next_crate_id(), length=random.randint(1, max_length), coordinate=None)
        # print(f"created crate with id: {ladder.id}, dimension: {ladder.dimension}, area: {ladder.dimension.area()}")
        # return ladder

    def random_crates(self, max_length:int, count: int) -> list[Crate]:
        crates: list[Crate] = []
        for _ in range(count):
            crates.append(self.random_crate(max_length))
        return crates

    def random_rack(self, max_height: int) -> Rack:
        return Rack(id=global_id_generator.next_rack_id(), height=random.randint(1, max_height), coordinate=None)
        # print(f"created crate with id: {ladder.id}, dimension: {ladder.dimension}, area: {ladder.dimension.area()}")
        # return ladder

    def random_racks(self, max_height:int, count: int) -> list[Rack]:
        racks: list[Rack] = []
        for _ in range(count):
            racks.append(self.random_rack(max_height))
        return racks