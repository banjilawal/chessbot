# src/chess/team/team.py

"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-08-04
version: 1.0.0
"""

from typing import List

from chess.game.model import Game
from chess.piece import Piece, UniquePieceDataService
from chess.team import TeamSchema
from chess.agent import Agent


class Team:
    """
    # ROLE: Data-Holding

    # RESPONSIBILITY:
    1.  Disposition of Pieces the Agent can move on a Board instance.
    2.  Holds the captured enemy Pieces.

    # PROVIDES:
    Team

    # ATTRIBUTES:
        *   MAX_ROSTER_SIZE (int):  Size of roster at full strength.
        *   id (int):               Globally unique identifier for the team.
        *   roster (UniquePieceDataService):   Collection of Pieces the Agent can move on a Board instance.
        *   hostages (UniquePieceDataService):  Collection of captured enemy Pieces.
        *   agent (Agent):  Directs moves of Pieces in Team.roster.
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
    _agent: Agent
    _game: Game
    _schema: TeamSchema
    _roster: UniquePieceDataService
    _hostages: UniquePieceDataService

    def __init__(
            self,
            id: int,
            agent: Agent,
            game: Game,
            schema: TeamSchema,
            roster: UniquePieceDataService,
            hostages: UniquePieceDataService,
    ):
        """
        # ACTION:
        Construct a Team object.

        # PARAMETERS:
            *   id (int)
            *   agent (Agent)
            *   schema (TeamSchema)
            *   roster (UniquePieceDataService)
            *   hostages (UniquePieceDataService)

        # Returns:
        None

        # RAISES:
        None
        """
        method = "Team.__init__"
        self._id = id
        self._agent = agent
        self._game = game
        self._schema = schema
        self._roster = roster
        self._hostages = hostages
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def agent(self) -> Agent:
        return self._agent
    
    @property def game(self) -> Game:
        return self._game
    
    @property
    def schema(self) -> TeamSchema:
        return self._schema

    @property
    def roster(self) -> UniquePieceDataService:
        return self._roster
    
    @property
    def hostages(self) -> UniquePieceDataService:
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
        return (
            f"Team{{"
            f"id:{self._id} {self._agent.name} {self._schema}"
            f"}}"
        )