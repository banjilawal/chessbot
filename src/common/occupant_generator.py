import random

from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from src.model.occupant.vault import Vault
from src.model.occupant.crate import Crate


class OccupantGenerator:
    def random_dimension(self, max_length: int, max_height: int) -> Dimension:
        return Dimension(
            length=random.randint(1, max_length),
            height=random.randint(1, max_height)
        )

    def generate_boulder(self, max_length: int, max_height: int) -> Vault:
        boulder = Vault(
            id=global_id_generator.next_boulder_id(),
            dimension=self.random_dimension(max_length, max_height),
        )
        print(f"created boulder with id: {boulder.id}, dimension: {boulder.dimension}, area: {boulder.dimension.area()}")
        return boulder

    def generate_boulders(self, max_length: int, max_height:int, count: int) -> list[Vault]:
        return [self.generate_boulder(max_length, max_height) for _ in range(count)]

    def generate_ladder(self, max_height: int) -> Crate:
        ladder = Crate(id=global_id_generator.next_crate_id(), height=random.randint(2, max_height), coordinate=None)
        print(f"created crate with id: {ladder.id}, dimension: {ladder.dimension}, area: {ladder.dimension.area()}")
        return ladder

    def generate_ladders(self,  max_height:int, count: int) -> list[Crate]:
        return [self.generate_ladder(max_height) for _ in range(count)]