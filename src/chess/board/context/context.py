# src/chess/board/context/context.py

"""
Module: chess.board.context.context
Author: Banji Lawal
Created: 2025-10-02
version: 1.0.0
"""

from typing import Optional

from chess.board import Board
from chess.arena import Arena
from chess.system import Context


class BoardContext(Context[Board]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an SquareFinder with an attribute value to find Squares with a matching value in their version of
    the attribute.
    
    # PARENT:
        *   Context
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
        *   arena (Arena)
        
    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _arena: Optional[Arena] = None
    
    def __init__( self, id: Optional[int] = None, arena: Optional[Arena] = None,):
        super().__init__(id=id, name=None)
        self._arena = arena
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    def to_dict(self) -> dict:
        """
        # ACTION:
            Convert a SquareContext attributes into a dictionary.
        # PARAMETERS:
        None
        # RETURNS:
            dict
        # RAISES:
        None
        """
        return {
            "id": self.id,
            "arena": self._arena
        }
