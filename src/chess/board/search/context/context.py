# src/chess/board/search/context/context
"""
Module: chess.board.search.context.context
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class BoardSearchContext(SearchContext):
    """
    # ROLE: Search option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair BoardSearch implementations use to find matches.
  
    # PROVIDES:
    BoardSearchContext.
  
    # ATTRIBUTES:
        *   id (int):       Find items whose id matches this value.
        *   name (str):     Find items whose name matches this value.
        *   coord (Coord):  Find items whose coord matches this value.
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
            "name": self._name,
            "coord": self._coord
        }
