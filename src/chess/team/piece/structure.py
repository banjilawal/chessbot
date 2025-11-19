# src/chess/team/piece/__init__.py

"""
Module: chess.team.piece__init__
Author: Banji Lawal
Created: 2025-11-18
version: 1.0.0
"""


from chess.piece import Piece


class PieceList:
    _items: list[Piece]
    
    def __init__(self):
        self._items = []
        
    def items(self) -> list[Piece]:
        return self._items
    
    