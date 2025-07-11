import random
from typing import Union, Dict, List

from common.direction import Direction
from model.board import Board
from model.bin import Bin
from model.grid_entity import HorizontalMover
from src.common.dimension import Dimension
from src.common.id_generator import global_id_generator
from model.crate import Crate


class EntityFactory:

    @staticmethod
    def build_dimensopm(max_length: int, max_height: int) -> Dimension:
        return Dimension(
            length=random.randint(1, max_length),
            height=random.randint(1, max_height)
        )

    @staticmethod
    def build_horizontal_mover(max_height: int) -> HorizontalMover:
        mover = HorizontalMover(
            mover_id=global_id_generator.next_vault_id(),
            height=random.randint(2, max_height),
            coordinate=None
        )
        print(mover)
        return mover

    @staticmethod
    def build_horizontal_mover_list(max_height: int, count: int) -> List[HorizontalMover]:
        return [EntityFactory.horizontal_mover(max_height) for _ in range(count)]

    @staticmethod
    def build_board(
            dimension=Dimension(21, 21),
            max_entity_dimension: int = 7,
            max_entities: int = 10
    ) -> Board:
        board = Board()
        board.add_horizontal_mover(EntityFactory.horizontal_mover(max_height=max_entity_dimension))
        return board


