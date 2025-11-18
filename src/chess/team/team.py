# src/chess/team/team.py

"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-08-04
version: 1.0.0
"""
from typing import List

from chess.piece import Piece
from chess.team import TeamSchema
from chess.agent import PlayerAgent


class Team:
    """
    # ROLE: Data-Holding

    # RESPONSIBILITY:
    1.  Disposition of Pieces the PlayerAgent can move on a Board instance.
    2.  Holds the captured enemy Pieces.

    # PROVIDES:
    Team

    # ATTRIBUTES:
        *   MAX_ROSTER_SIZE (int):  Size of roster at full strength.
        *   id (int):               Globally unique identifier for the team.
        *   roster (List[Piece]):   Collection of Pieces the PlayerAgent can move on a Board instance.
        *   hostages (List[Piece):  Collection of captured enemy Pieces.
        *   agent (PlayerAgent):  Directs moves of Pieces in Team.roster.
        *   schema (TeamSchema):    Defines the Team's
                *   name (str):                 Unique within the Game instance.
                *   color (GameColor):          Color of the Team. (white/black)
                *   rank_row (int):             Index or row containing the Team's ranked Pieces.
                *   pawn_row (int):             Index or row containing the Team's pawn Pieces.
                *   advancing_step (Vector):    Direction of the Team's roster member to get to the enemy's
                                                Pieces.
    """

    MAX_ROSTER_SIZE = 16
    
    _id: int
    _player_agent: PlayerAgent
    _schema: TeamSchema
    _roster: [Piece]
    _hostages: [Piece]
    
    def __init__(self, id: int, player_agent: PlayerAgent, schema: TeamSchema):
        """
        # ACTION:
        Construct a Team object.

        # PARAMETERS:
            *   id (int):               Globally unique identifier for the team.
            *   agent (PlayerAgent):   Directs moves of Pieces in Team.roster.
            *   schema (TeamSchema):    Defines the Team's

        # Returns:
        None

        # RAISES:
        None
        """
        method = "Team.__init__"
        
        self._id = id
        self._schema = schema
        self._roster = [Piece]
        self._hostages = [Piece]
        self._player_agent = player_agent

    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def roster(self) -> [Piece]:
        return self._roster
    
    @property
    def hostages(self) -> [Piece]:
        return self._hostages
    
    @property
    def schema(self) -> TeamSchema:
        return self._schema
    
    @property
    def player_agent(self) -> PlayerAgent:
        return self._player_agent
    
    def __eq__(self, other) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Team):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return (
            f"Team{{"
            f"id:{self._id} {self._player_agent.name} {self._schema}"
            f"}}"
        )