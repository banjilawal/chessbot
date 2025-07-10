import random
from typing import Union, Dict, List

from common.direction import Direction
from model.grid import Grid
from model.bin import Bin
from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from model.vault import VerticalMover, HorizontalMover
from model.crate import Crate


class Generator:

    @staticmethod
    def random_dimension(max_length: int, max_height: int) -> Dimension:
        return Dimension(
            length=random.randint(1, max_length),
            height=random.randint(1, max_height)
        )

    @staticmethod
    def random_horizontal_mover(max_height: int) -> HorizontalMover:
        mover = HorizontalMover(
            mover_id=global_id_generator.next_vault_id(),
            height=random.randint(2, max_height),
            coordinate=None
        )
        print(mover)
        return mover

    @staticmethod
    def horizontal_movers(max_height: int, count: int) -> List[HorizontalMover]:
        return [Generator.random_horizontal_mover(max_height) for _ in range(count)]

    @staticmethod
    def board(
            dimension=Dimension(21, 21),
            max_entity_dimension: int = 7,
            max_entities: int = 10
    ) -> Grid:
        board = Grid()
        board.add_horizontal_mover(Generator.random_horizontal_mover(max_height=max_entity_dimension))
        return board


