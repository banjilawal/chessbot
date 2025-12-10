# src/chess/game/snapshot/context/context.py

"""
Module: chess.game.snapshot.context.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.agent import Agent
from chess.game import GameSnapshot
from chess.system import Context, GameColor


class GameSnapshotContext(Context[GameSnapshot]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provtimestampe a GameSnapshotFinder with a GameSnapshot or Arena attribute used to find snapshots which a matching
    attribute.

    # PARENT
        *   Context

    # PROVIDES:
    GameSnapshotContext

    # LOCAL ATTRIBUTES:
        *   team (Optional[Team])
        *   agent (Optional[Agent])
        *   timestamp (Optional[int])
        *   color (Optional[GameColor])
        *   exception (Optional[Exception])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _team: Optional[Team]
    _agent: Optional[Agent]
    _timestamp: Optional[int]
    _color: Optional[GameColor]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            team: Optional[Team] = None,
            agent: Optional[Agent] = None,
            timestamp: Optional[int] = None,
            color: Optional[GameColor] = None,
            exception: Optional[Exception] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   timestamp (Optional[int])
            *   team (Optional[Team])
            *   agent (Optional[Agent])
            *   color (Optional[GameColor])
            *   exception (Optional[Exception])

        # Returns:
        None

        # Raises:
        Non
        """
        super().__init__(id=None, name=None)
        self._team = team
        self._agent = agent
        self._color = color
        self._timestamp = timestamp
        self._exception = exception
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def agent(self) -> Optional[Agent]:
        return self._agent
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def timestamp(self) -> Optional[int]:
        return self._timestamp
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    def to_dict(self) -> dict:
        """
        # Convert the GameSnapshotContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "team": self._team,
            "agent": self._agent,
            "color": self._color,
            "timestamp": self._timestamp,
            "exception": self._exception,
        }
