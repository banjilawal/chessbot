from typing import List

from chess.arena.arena import Arena
from chess.geometry.coordinate.coordinate_stack import CoordinateStack
from chess.owner.model.owner import Owner

class Match:
    _id: int
    _arena: Arena
    _winner: Owner
    _game_Log: List[CoordinateStack]