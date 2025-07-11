import random
from typing import List

from board import Board
from grid_entity import HorizontalMover
from geometry import Dimension


class IdFactory:
    def __init__(self):
        self.cell_id = 1
        self.mover_id = 1

    def next_cell_id(self) -> int:
        current_id = self.cell_id
        self.cell_id += 1
        return current_id

    def next_mover_id(self) -> int:
        current_id = self.mover_id
        self.mover_id += 1
        return current_id
global_id_generator = IdFactory()


class EntityFactory:

    @staticmethod
    def build_dimension(max_length: int, max_height: int) -> Dimension:
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


