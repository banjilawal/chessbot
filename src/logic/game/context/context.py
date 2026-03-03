# src/logic/game/map.py

"""
Module: logic.game.map
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from logic.agent import PlayerAgent
from logic.board import Board
from logic.game import Game
from logic.system import Context
from logic.team import Team


class GameContext(Context[Game]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an GameFinder with an attribute value to find Games with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    GameContext

    # LOCAL ATTRIBUTES:
        *   team (Optional[Team])
        *   owner (Optional[Player])
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
            *   owner (Optional[Player])
            *   board (Optional[Board])

        # RETURNS:
        None

        Raises:
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

        # RETURNS:
        dict

        Raises:
        """
        return {
            "id": self.id,
            "team": self.team,
            "owner": self._agent,
            "board": self._board,
        }