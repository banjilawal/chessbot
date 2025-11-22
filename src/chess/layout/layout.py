# src/chess/layout/layout.py

"""
Module: chess.layout/layout.py
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.rank import Rank
from chess.team import Team


class Layout:
    _square_name: str
    _rank: Rank
    _slot: int
    _piece_name: str
    _team: Team
