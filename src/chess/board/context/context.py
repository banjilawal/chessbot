# src/chess/board/searcher/context/context
"""
Module: chess.board.searcher.context.context
Author: Banji Lawal
Created: 2025-10-08
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
    Provide a BoardFinder with an attribute-value which finds Boards which match the targeted attribute-value.
    
    # PARENT:
        *   Context
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        
    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _id: Optional[int] = None
    _arena: Optional[Arena] = None
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            arena: Optional[Arena] = None,
    ):
        super().__init__(id=id, name=None)
        self._arena = arena
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "arena": self._arena
        }
