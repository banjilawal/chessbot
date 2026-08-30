# src/domain/model/searchable/state/team/model/searchable/model.py.py

"""
Module: domain.model.searchable.state.team.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import CheckChain
from collection.database import TokenDatabase
from domain.model import Board, Player, StateModel, TeamState
from domain.schema import Archetype
from logic.checking import CheckingException


class Team(StateModel):
    """
    Role:
        - Model
        -  Stateless Data-Holder
        
    Responsibilities:
        1.   Manages tokens assigned to a Team.
        
    Attributes:
        MAX_ROSTER_SIZE = 16
        id: int
        board: Board
        owner: Player
        archetype: Archetype
        roster: TokenDatabase
        
    Provides:
        - def is_ready_to_play() -> bool
        - def is_waiting_to_play() -> bool
        - def is_not_ready_to_play() -> bool
        
    Super Class
    """
    MAX_ROSTER_SIZE = 16
    
    _id: int
    _board: Board
    _owner: Player
    _state: TeamState
    _archetype: Archetype
    _roster: TokenDatabase
    _check_event_log: CheckChain

    def __init__(
            self,
            id: int,
            board: Board,
            owner: Player,
            archetype: Archetype,
    ):
        """
        Args:
            id: int
            board: Board
            owner: Player
            archetype: Archetype

        """
        super().__init__()
        self._id = id
        self._board = board
        self._archetype = archetype
        self._owner = owner
        self._state = TeamState.NOT_READY_TO_PLAY
        self._roster = TokenDatabase()
        self._check_event_log = CheckChain(team=self)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def owner(self) -> Player:
        return self._owner
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def archetype(self) -> Archetype:
        return self._archetype
    
    @property
    def enemy_archetype(self) -> Archetype:
        return self._archetype.enemy_archetype
    
    @property
    def enemy_rank_row(self) -> int:
        return self.enemy_archetype.rank_row

    @property
    def roster(self) -> TokenDatabase:
        return self._roster
    
    @property
    def state(self) -> TeamState:
        return self._state
    
    @property
    def check_event_log(self) -> CheckChain:
        return self._check_event_log
    
    @state.setter
    def state(self, state: TeamState):
        self._state = state
        
    def is_ready_to_play(self) -> bool:
        return self._roster.is_deployed_on_board and self._state == TeamState.READY_TO_PLAY
    
    def is_not_ready_to_play(self) -> bool:
        return not self._roster.is_deployed_on_board and not self._state != TeamState.NOT_READY_TO_PLAY
    
    def is_waiting_to_play(self) -> bool:
        return self._roster.is_deployed_on_board and self._state == TeamState.WAITING_TO_PLAY
    
    def __eq__(self, other) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Team):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return f"Team{{id:{self._id} {self._owner.name} {self._archetype}}}"