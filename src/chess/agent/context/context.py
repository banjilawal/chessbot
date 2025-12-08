# src/chess/agent/context/context.py

"""
Module: chess.agent.context.context
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.game import Game
from chess.team import Team
from chess.system import Context
from chess.agent import Agent, AgentVariety


class AgentContext(Context[Agent]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an AgentFinder with an attribute value to find Agents with a matching value in
    their version of the attribute.

    # PARENT
        *   Context

    # PROVIDES:
    AgentContext

    # LOCAL ATTRIBUTES:
        *   team (Optional[Team])
        *   game (Optional[Game])
        *   variety (Optional[AgentVariety])
        
    # INHERITED ATTRIBUTES:
    See Context class for inherited attributes.
    """
    _team: Optional[Team]
    _game: Optional[Game]
    _variety: Optional[AgentVariety]
    
    def __init__(
            self,
            id: Optional[id] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[AgentVariety] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (Optional[int])
            *   name (Optional[str])
            *   team (Optional[Team])
            *   game (Optional[Game])
            *   variety (Optional[AgentVariety])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name)
        self._team = team
        self._game = game
        self._variety = variety
        
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def variety(self) -> Optional[AgentVariety]:
        return self._variety
    
    def to_dict(self) -> dict:
        """
        # Convert the AgentContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "id": self.id,
            "name": self.name,
            "team": self._team,
            "game": self._game,
            "variety": self._variety,
        }
    