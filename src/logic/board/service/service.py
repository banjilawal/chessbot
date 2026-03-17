# src/logic/board/service.py

"""
Module: logic.board.service
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.board import (
    Board, BoardAlreadyLaidOutException, BoardBuilder, BoardLayoutFailedException, BoardSquareRelationAnalyzer,
    BoardState, BoardValidator
)
from logic.board.service.exception.anchor import BoardServiceException
from logic.graph import Graph, GraphComputationException
from logic.system import ComputationResult, IdFactory, InsertionResult, IntegrityService, LoggingLevelRouter
from logic.team import Team, TeamBelongsToDifferentBoardException, TeamService, TeamSlotAlreadyOccupiedException


class BoardService(IntegrityService[Board]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Board microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Board state by providing single entry and exit points to Board
        lifecycle.

    Super Class:
        *   IntegrityService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "BoardService"
    _square_relation_analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: BoardBuilder = BoardBuilder(),
            validator: BoardValidator = BoardValidator(),
            id: int = IdFactory.next_id(class_name="BoardService"),
            square_relation_analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer()
    ):
        """
        Args:
                id: int
                name: str
                builder: BoardBuilder
                validator: BoardValidator
                square_relation_analyzer: SquareRelationAnalyzer
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._square_relation_analyzer = square_relation_analyzer
    
    @property
    def builder(self) -> BoardBuilder:
        return cast(BoardBuilder, self.builder)
    
    @property
    def validator(self) -> BoardValidator:
        return cast(BoardValidator, self.validator)
    
    @property
    def square_relation_analyzer(self) -> BoardSquareRelationAnalyzer:
        return  self._square_relation_analyzer
    
    @LoggingLevelRouter.monitor
    def form_team_on_board(
            self,
            board: Board,
            team: Team,
            team_service: TeamService = TeamService()
    ) -> InsertionResult:
        method = "BoardService.forma_team_on_board"
        
        # Handle the case that, the team is not certified as safe.
        team_validation = team_service.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERR_CODE}",
                    ex=team_validation.exception
                ),
            )
        # Handle the case that, the team belongs on a different board.
        if not board == team.board:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERR_CODE}",
                    ex=TeamBelongsToDifferentBoardException(
                        msg=f"{method}: {TeamBelongsToDifferentBoardException.MSG}",
                    ),
                )
            )
        # Handle the case that, the team's slot is already occupied.
        if board.team_hash.slot_is_occupied(team):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERR_CODE}",
                    ex=TeamSlotAlreadyOccupiedException(
                        f"{method}: {TeamSlotAlreadyOccupiedException.MSG}"
                    ),
                )
            )
        # Handle the case that, the team is already deployed.
        if team.is_ready_to_play():
            return InsertionResult.success()
        # --- The is rea. ---#
        
        # Handle the case that, the team is not ready
        if team.is_not_ready_to_play():
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardServiceException}",
                ),
            )
    
    @LoggingLevelRouter.monitor
    def layout_board(self, board: Board) -> InsertionResult[bool]:
        method = "BoardService.layout_board"
        
        # Handle the case that, the board is not certified as safe.
        validation = self.validator.validate(candidate=board)
        if validation.is_failure:
            # Return exception chain on failure
            return InsertionResult.failure(
                BoardServiceException(
                    f"{method}: {BoardServiceException.MSG}",
                    ex=BoardLayoutFailedException(
                        msg=f"{method}: {BoardLayoutFailedException.MSG}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the board has already been laid out.
        if board.state == BoardState.HAS_TOKENS_LAID_OUT:
            # Return exception chain on failure
            return InsertionResult.failure(
                BoardServiceException(
                    f"{method}: {BoardServiceException.MSG}",
                    ex=BoardLayoutFailedException(
                        msg=f"{method}: {BoardLayoutFailedException.MSG}",
                        ex=BoardAlreadyLaidOutException(
                            f"{method}: {BoardLayoutFailedException.MSG}",
                        )
                    )
                )
            )
        # --- Deploy each team's tokens on the board by looping through their hash-table. ---#
        for key in board.team_hash.table.keys():
            deployment_result = board.team_hash.table[key].roster.deploy_tokens_on_board
            
            # Handle the case that, the team's deployment is not completed.
            if deployment_result.is_failure:
                # Return the exception chain on failure.
                return InsertionResult.failure(
                    BoardServiceException(
                        f"{method}: {BoardServiceException.MSG}",
                        ex=deployment_result.exception,
                    )
                )
        # --- Update the board's state and send the success result to the caller. ---#
        board.state = BoardState.HAS_TOKENS_LAID_OUT
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def generate_graph(self, board: Board) -> ComputationResult[Graph]:
        method = "BoardService.generate_graph"
    
        # Handle the case that, the board is not certified as safe.
        validation = self.validator.validate(candidate=board)
        if validation.is_failure:
            # Return exception chain on failure
            return ComputationResult.failure(
                BoardServiceException(
                    f"{method}: {BoardServiceException.MSG}",
                    ex=GraphComputationException(
                        msg=f"{method}: {GraphComputationException.MSG}",
                        ex=validation.exception
                    )
                )
            )
        
        
        

        
            
        
        

