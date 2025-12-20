# src/chess/game/snapshot/context/context.py

"""
Module: chess.game.snapshot.context.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.agent import PlayerAgent
from chess.game import GameSnapshot
from chess.system import Context, GameColor


class GameSnapshotContext(Context[GameSnapshot]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provtimestampe a GameSnapshotFinder with a Snapshot or Arena attribute used to find snapshots which a matching
    attribute.

    # PARENT:
        *   Context

    # PROVIDES:
        *   GameSnapshotContext.to_dict

    # LOCAL ATTRIBUTES:
        *   team (Optional[Team])
        *   player_agent (Optional[PlayerAgent])
        *   timestamp (Optional[int])
        *   color (Optional[GameColor])
        *   exception (Optional[Exception])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _team: Optional[Team]
    _agent: Optional[PlayerAgent]
    _timestamp: Optional[int]
    _color: Optional[GameColor]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            team: Optional[Team] = None,
            agent: Optional[PlayerAgent] = None,
            timestamp: Optional[int] = None,
            exception: Optional[Exception] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   timestamp (Optional[int])
            *   team (Optional[Team])
            *   player_agent (Optional[PlayerAgent])
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
        self._timestamp = timestamp
        self._exception = exception
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def agent(self) -> Optional[PlayerAgent]:
        return self._agent
    
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
            "player_agent": self._agent,
            "timestamp": self._timestamp,
            "exception": self._exception,
        }
