# src/model/token/model.py

"""
Module: model.token.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

from database import CoordDatabase
from model import Coord, Formation, OpeningSquare, Rank, Team, TokenActivityState, DeploymentState


class Token(ABC):
    """
    Role:
        -   Stateful Data Holder
        
    Responsibilities:
        1. Abstract representation of a chess piece.
        
    Attributes:
        id: int
        team: Team
        rank: Rank
        designation: str
        roster_number: int
        positions: CoordDatabase
        opening_square: OpeningSquare
        current_position: Optional[Coord]
        previous_address: Optional[Coord]
        token_board_state: TokenBoardState
        readiness_state: TokenActivityState
        is_not_deployed: bool
        is_active(self): bool
        is_disabled: bool
        is_enemy: bool
        
    Provides:

    Super Class:
    """
    _id: int
    _team: Team
    _rank: Rank
    _formation: Formation
    _positions: CoordDatabase
    _opening_square: OpeningSquare
    _current_position: Optional[Coord]
    _previous_address: Optional[Coord]
    _deployment_state: DeploymentState
    _readiness_state: TokenActivityState

    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            formation: Formation,
            opening_square: OpeningSquare,
    ):
        """
        Args:
            id: int
            team: Team
            rank: Rank
            formation: Formation
            opening_square: OpeningSquare
        """
        self._id = id
        self._team = team
        self._rank = rank
        self._formation = formation
        self._positions = CoordDatabase()
        self._opening_square = opening_square
        self._current_position = self._positions.current_item
        self._previous_address = self._positions.previous_coord
        self._deployment_state = DeploymentState.NOT_DEPLOYED
        self._readiness_state = TokenActivityState.NOT_INITIALIZED
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def designation(self) -> str:
        return self._formation.designation
    
    @property
    def roster_number(self) -> int:
        return self._formation.roster_number
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def opening_square(self) -> OpeningSquare:
        return self._opening_square
    
    @property
    def readiness_state(self) -> TokenActivityState:
        return self._readiness_state
    
    @readiness_state.setter
    def readiness_state(self, readiness_state: TokenActivityState):
        self._readiness_state = readiness_state
    
    @property
    def positions(self) -> CoordDatabase:
        return self._positions
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._positions.current_item
    
    @property
    def previous_coord(self) -> Optional[Coord]:
        return self._previous_address
    
    @property
    def deployment_state(self) -> DeploymentState:
        return self._deployment_state
    
    def mark_deployed(self,):
        self._deployment_state = DeploymentState.DEPLOYED
    
    @property
    def is_not_deployed(self) -> bool:
        return (
                self.positions.is_empty and
                self._deployment_state == DeploymentState.NOT_DEPLOYED
        )
    
    @property
    def is_deployed(self) -> bool:
        return (
                self.positions.size >= 1 and
                self._deployment_state == DeploymentState.DEPLOYED
        )
    
    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_disabled(self) -> bool:
        pass
    
    @mark_deployed.setter
    def deployment_state(self, token_board_state: DeploymentState):
        self._deployment_state = token_board_state
    
    def set_rank(self, rank: Rank) -> None:
        self._rank = rank
    
    def is_friend(self, token: Token) -> bool:
        return self._team == token.team
    
    def is_enemy(self, token: Token) -> bool:
        return not self.is_friend(token)
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other in None: return False
        if isinstance(other, Token):
            return self._id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return (
            f"Token[id:{self._id} "
            f"designation:{self._designation} "
            f"rank:{self._rank.persona.name} "
            f"team:{self._team.schema.name} "
            f"position:{self.current_position}"
        )
