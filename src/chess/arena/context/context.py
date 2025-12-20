# src/chess/arena/context/context.py

"""
Module: chess.arena.arena.context.context
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.board import Board
from chess.arena import Arena
from chess.system import Context, GameColor



class ArenaContext(Context[Arena]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an ArenaFinder with an attribute-value which finds Arenas which match the targeted attribute-value.

    # PARENT:
        *   Context

    # PROVIDES:
    ArenaContext

    # LOCAL ATTRIBUTES:
        *   id (Optional[int])
        *   team (Optional[Team])
        *   color (Optional[GameColor])
        *   board (Optional[Board])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _team: Optional[Team]
    _color: Optional[GameColor]
    _board: Optional[Board]
    
    def __init__(
            self,
            id: Optional[id] = None,
            team: Optional[Team] = None,
            color: Optional[GameColor] = None,
            board: Optional[Board] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (Optional[int])
            *   team (Optional[Team])
            *   player_color (Optional[GameColor])
            *   board (Optional[Board])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=None)
        self._team = team
        self._color = color
        self._board = board
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    def to_dict(self) -> dict:
        """
        # Convert the ArenaContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "id": self.id,
            "team": self.team,
            "color": self._color,
            "board": self._board,
        }