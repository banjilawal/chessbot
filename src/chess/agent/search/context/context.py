# src/chess/board/search/context/context

"""
Module: chess.board.search.context.context
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import Optional


from chess.system import GameColor, SearchContext


class AgentTeamSearchContext(SearchContext):
    """
    # ROLE: Search option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair AgentTeamSearch implementations use to
    find matches in PlayerAgent.team_assignments.
  
    # PROVIDES:
    AgentTeamSearchContext.
  
    # ATTRIBUTES:
        *   id (int):           Should produce one and only one, Team object team ids are globally unique.
        
        *   name (str):         Will produce a list of teams whose name matches this value. The results will
                                be the same as the color search context. There's only two possible
                                
        *   color (Gamecolor):  Should produce the same results as AgentSearchContext.name. There's only
                                two possible values and they match AgentSearchContext.name.
    """
    _id: Optional[int] = None
    _name: Optional[str] = None
    _color: Optional[GameColor] = None
    
    def __init__(
            self,
            id: Optional[int]=None,
            name: Optional[str]=None,
            color: Optional[GameColor]=None,
    ):
        self._id = id
        self._name = name
        self.color = color
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "color": self._color
        }
