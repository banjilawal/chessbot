from typing import List

from chess.arena.arena import Arena
from chess.geometry.coordinate.coordinate_stack import CoordinateStack
from chess.owner.model.owner import Owner


class Game:
    _id: int
    _white_owner: Owner
    _black_owner: Owner
    _arena: Arena
    _game_Log: List[CoordinateStack]