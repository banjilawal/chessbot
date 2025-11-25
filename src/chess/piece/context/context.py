# src/chess/piece/context/context.py

"""
Module: chess.piece.context.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Dict, Optional

from chess.coord import Coord
from chess.piece import Piece
from chess.system import Context, LoggingLevelRouter


class PieceContext(Context[Piece]):
    _coord: Optional[Coord]
    
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None
    ):
        super().__init__(id=id, name=name)
        self._coord = coord
        
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "coord": self._coord
        }