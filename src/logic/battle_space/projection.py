# src/logic/battle_space/projection.py

"""
Module: logic.battle_space.projection
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""


from typing import Dict, List

from logic.coord import Coord
from logic.piece import PieceDTO



__all__ = [
    'Projection',
    'ProjectionTable'
]

from logic.team import Team


class Projection:
    _metadata: PieceDTO
    _points: List[Coord]
    
class ProjectionTable:
    _table: Dict[str, List[Projection]]
    
    def __init__(self, white_team: Team, black_team: Team):
        self._table = {}
