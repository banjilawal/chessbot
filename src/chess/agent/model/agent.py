# src/chess/agent/model/agent.py

"""
Module: chess.agent.model.agent
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from abc import ABC
from typing import Optional

from chess.team.team import Team
from chess.agent import TeamStackService


class Agent(ABC):
    _id: int
    _name: str
    _current_team: Optional[Team]
    _team_stack_service: TeamStackService
    
    def __init__(
            self,
            id: int,
            name: str,
            team_stack_service: TeamStackService = TeamStackService()
    ):
        self._id = id
        self._name = name
        self._team_stack_service = team_stack_service
        self._current_team = self._team_stack_service.current_team
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def team_stack_service(self) -> TeamStackService:
        return self._team_stack_service
    
    @property
    def current_team(self) -> Optional[Team]:
        return self._team_stack_service.current_team
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Agent):
            return self._id == other.id
        return False
    
    def __str__(self):
        total_games = self.teams.size()
        total_games_str = f"total games:{total_games}" if total_games > 0 else ""
        
        current_side = "" if self._current_team is None else \
            f" curren_team:[{self._current_team.id}, {self._current_team.schema.color}"
        return (
            f"Owner[id:{self._id}"
            f" name:{self._name}"
            f"{current_side}"
            f"{total_games_str}"
            f"]"
        )
    
    # agent.order_move(
    #   owner=TeamSearch.search(
    #     data_owner=self._team_name,
    #     search_category=SearchCategory.ROSTER,
    #     context=TeamSearchContext(visitor_name="BN1")
    #   ),
    #   square_name="C8"
    # )
    #
    # # Which internally uses your transactional system:
    # # 1. Search returns Result[Piece]
    # # 2. Validates inputs
    # # 3. Creates MoveEvent
    # # 4. Executes via TravelTransaction
    # # 5. Returns TransactionResult with rollback safety
    
    def move_piece(self, piece_name: str, destination: Coord):
        method = "Agent.move_piece"
        
        try:
            validation = NameValidator.validate(piece_name)
            if not validation.is_success():
                raise validation.exception
            
            result = self._current_team.find_piece_by_name(piece_name)
            if not result.is_success():
                raise result.exception
            
            piece = cast(Piece, result.payload)
            
            # if discover is None:
            #   raise PieceNotFoundException(
            #     f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE} at index {array_index}"
            #   )
            
            if piece.current_position is None:
                raise PieceCoordNullException(f"{method}: {PieceCoordNullException.DEFAULT_MESSAGE}")
            
            if isinstance(piece, CombatantPiece) and piece.captor is not None:
                raise PrisonerEscapeException(f"{method}: Cannot move {piece.name} it has been captured.")
            
            validation = CoordValidator.validate(destination)
            if not validation.is_success():
                raise validation.exception
            
            if piece.current_position == destination:
                raise AlreadyAtDestinationException(f"{method}: {AlreadyAtDestinationException.DEFAULT_MESSAGE}")
            
            piece.rank.walk(piece=piece, destination=destination)
        
        except (NullPieceException, ConflictingTeamException) as e:
            raise AddPieceException(f"{method}: {AddPieceException.DEFAULT_MESSAGE}")
