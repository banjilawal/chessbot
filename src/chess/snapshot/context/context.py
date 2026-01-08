# src/chess/snapshot/map.py

"""
Module: chess.snapshot.map
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.arena import Arena
from chess.game import Game
from chess.team import Team
from chess.snapshot import Snapshot
from chess.agent import PlayerAgent
from chess.system import Context, GameColor


class SnapshotContext(Context[Snapshot]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    1.  Provide an SchemaLookup with an attribute-value-tuple to perform forward Schema entry lookups.
    # Provtimestampe a SnapshotFinder with a Snapshot or Arena attribute used to find snapshots which a matching
    # attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   game (Optional[Game])
        *   team (Optional[Team])
        *   arena (Optional[Arena])
        *   timestamp (Optional[int])
        *   exception (Optional[Exception])
        *   player (Optional[Player])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _game: Optional[Game]
    _team: Optional[Team]
    _arena: Optional[Arena]
    _timestamp: Optional[int]
    _exception: Optional[Exception]
    _player: Optional[PlayerAgent]
    
    def __init__(
            self,
            game: Optional[Game],
            team: Optional[Team],
            arena: Optional[Arena],
            timestamp: Optional[int],
            player: Optional[PlayerAgent],
            exception: Optional[Exception],
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   game (Optional[Game])
            *   team (Optional[Team])
            *   arena (Optional[Arena])
            *   timestamp (Optional[int])
            *   exception (Optional[Exception])
            *   player (Optional[Player])

        # RETURNS:
        None

        # RAISES:
        Non
        """
        super().__init__(id=None, name=None)
        self._game = game
        self._team = team
        self._arena = arena
        self._player = player
        self._timestamp = timestamp
        self._exception = exception
        
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def player(self) -> Optional[PlayerAgent]:
        return self._player
    
    @property
    def timestamp(self) -> Optional[int]:
        return self._timestamp
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    def to_dict(self) -> dict:
        """
        # Convert the SnapshotContext object to a dictionary.

        # PARAMETERS:
        None

        # RETURNS:
        dict

        # RAISES:
        None
        """
        return {
            "game": self._game,
            "team": self._team,
            "arena": self._arena,
            "player": self._agent,
            "timestamp": self._timestamp,
            "exception": self._exception,
        }
