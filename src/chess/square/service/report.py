# src/chess/square/service/report.py

"""
Module: chess.square.service.report
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import Optional

from chess.square import Square
from chess.token.model import Token

class SquareOccupationReport:
    _square: Square
    _departing_occupant: Optional[Token]
    _entering_occupant: Optional[Token]
    _stable_occupant: Optional[Token]