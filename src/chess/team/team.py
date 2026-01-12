# src/chess/team/team.py

"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-08-04
version: 1.0.0
"""

from chess.arena import Arena
from chess.schema import Schema
from chess.player import Player
from chess.team import HostageService, RosterService
from chess.token import HostageService


class Team:
    """
    # ROLE: Data-Holding

    # RESPONSIBILITY:
    1.  Disposition of Tokens the Player can move on a Board instance.
    2.  Holds the captured enemy Tokens.
    
    # PARENT:
    None
    
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   schema (Schema)
        *   arena (Arena)
        *   owner (Player)
        *   roster (HostageService)
        *   hostages (HostageService)
        
    # INHERITED ATTRIBUTES:
    None
    """
    MAX_ROSTER_SIZE = 16
    
    _id: int
    _arena: Arena
    _schema: Schema
    _owner: Player
    _roster: RosterService
    _hostages: HostageService


    def __init__(
            self,
            id: int,
            arena: Arena,
            schema: Schema,
            owner: Player,
            roster: RosterService = RosterService(),
            hostages: HostageService = HostageService(),
    ):
        """
        # ACTION:
        Construct a Team object.

        # PARAMETERS:
            *   id (int)
            *   owner (Player)
            *   arena (Arena)
            *   team_schema (Schema)
            *   roster (HostageService)
            *   hostages (HostageService)

        # RETURNS:
        None

        # RAISES:
        None
        """
        method = "Team.__init__"
        self._id = id
        self._arena = arena
        self._schema = schema
        self._roster = roster
        self._hostages = hostages
        self._owner = owner
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def owner(self) -> Player:
        return self._owner
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def schema(self) -> Schema:
        return self._schema

    @property
    def roster(self) -> HostageService:
        return self._roster
    
    @property
    def hostages(self) -> HostageService:
        return self._hostages
    
    def __eq__(self, other) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Team):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return f"Team{{id:{self._id} {self._owner.name} {self._schema}}}"