# src/chess/game/context/context.py

"""
Module: chess.game.context.context
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.agent import PlayerAgent
from chess.board import Board
from chess.game import Game
from chess.system import Context
from chess.team import Team


class GameContext(Context[Game]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an GameFinder with an attribute value to find Games with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    GameContext

    # LOCAL ATTRIBUTES:
        *   team (Optional[Team])
        *   player_agent (Optional[PlayerAgent])
        *   board (Optional[Board])
        
    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _team: Optional[Team]
    _agent: Optional[PlayerAgent]
    _board: Optional[Board]
    
    def __init__(
            self,
            id: Optional[id] = None,
            team: Optional[Team] = None,
            agent: Optional[PlayerAgent] = None,
            board: Optional[Board] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (Optional[int])
            *   team (Optional[Team])
            *   player_agent (Optional[PlayerAgent])
            *   board (Optional[Board])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=None)
        self._team = team
        self._agent = agent
        self._board = board
        
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def agent(self) -> Optional[PlayerAgent]:
        return self._agent
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    def to_dict(self) -> dict:
        """
        # Convert the GameContext object to a dictionary.

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
            "player_agent": self._agent,
            "board": self._board,
        }