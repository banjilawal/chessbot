# src/chess/domain/domain.py
"""
Module: chess.domain.domain
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""
from typing import List

from chess.coord import Coord
from chess.piece import PieceDTO

class Domain:
    _metadata: PieceDTO
    _points: List[Coord]


