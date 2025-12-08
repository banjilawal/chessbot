# src/chess/game/context/context.py

"""
Module: chess.game.context.context
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent
from chess.game import Game
from chess.system import Context



class GameContext(Context[Game]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an GameFinder with an attribute value to find Games with a matching value in
    their version of the attribute.

    # PARENT
        *   Context

    # PROVIDES:
    GameContext

    # LOCAL ATTRIBUTES:
        *   agent (Optional[Agent])

        
    # INHERITED ATTRIBUTES:
    See Context class for inherited attributes.
    """
    _agent: Optional[Agent]
    
    def __init__(
            self,
            id: Optional[id] = None,
            agent: Optional[Agent] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (Optional[int])
            *   agent (Optional[Agent])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=None)
        self._agent = agent
        
    @property
    def agent(self) -> Optional[Agent]:
        return self._agent
    
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
            "name": self.name,
            "agent": self._agent,
        }
    