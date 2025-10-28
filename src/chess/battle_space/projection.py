# src/chess/battle_space/projection.py

"""
Module: chess.battle_space.projection
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""


from typing import Dict, List

from chess.coord import Coord
from chess.piece import PieceDTO
from chess.system import GameColor


__all__ = [
    'Projection',
    'TeamProjectionTable'
]

class Projection:
    _metadata: PieceDTO
    _points: List[Coord]
    
class TeamProjectionTable:
    _table: Dict[GameColor, List[Projection]]