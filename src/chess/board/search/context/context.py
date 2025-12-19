# src/chess/board/searcher/context/context
"""
Module: chess.board.searcher.context.context
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class BoardContext(SearchContext):
    """
    # ROLE: Finder option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair BoardSearch implementations use to find matches.
  
    # PROVIDES:
    TeamSearchContext.
  
    # ATTRIBUTES:
        *   id (int):       Find items whose id matches this value.
        *   designation (str):     Find items whose designation matches this value.
        *   target (Coord):  Find items whose target matches this value.
    """
    _id: Optional[int] = None
    _name: Optional[str] = None
    _coord: Optional[Coord] = None
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
    ):
        self._id = id
        self._name = name
        self._coord = coord
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "designation": self._name,
            "target": self._coord
        }
