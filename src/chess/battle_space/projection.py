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



__all__ = [
    'Projection',
    'ProjectionTable'
]

from chess.team import Team


class Projection:
    _metadata: PieceDTO
    _points: List[Coord]
    
class ProjectionTable:
    _table: Dict[str, List[Projection]]
    
    def __init__(self, white_team: Team, black_team: Team):
        self._table = {}
