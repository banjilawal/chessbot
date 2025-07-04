import random
from common.dimension import Dimension
from common.id_generator import global_id_generator
from model.occupant.boulder import Boulder
from model.occupant.ladder import Crate

class OccupantGenerator:
    def random_dimension(self) -> Dimension:
        return Dimension(
            length=random.randint(1, 4),
            height=random.randint(1, 3)
        )

    def generate_boulder(self) -> Boulder:
        boulder = Boulder(
            id=global_id_generator.next_boulder_id(),
            dimension=self.random_dimension()
        )
        print(f"created boulder with id: {boulder.id}, dimension: {boulder.dimension}, area: {boulder.dimension.area()}")
        return boulder

    def generate_boulders(self, count: int) -> list[Boulder]:
        return [self.generate_boulder() for _ in range(count)]

    def generate_crate(self) -> Crate:
        crate = Crate(
            id=global_id_generator.next_crate_id(),
            dimension=self.random_dimension()
        )
        print(f"created crate with id: {crate.id}, dimension: {crate.dimension}, area: {crate.dimension.area()}")
        return crate

    def generate_crates(self, count: int) -> list[Crate]:
        return [self.generate_crate() for _ in range(count)]