# src/chess/board/service.py

"""
Module: chess.board.service
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.board.analyzer.square.analyzer import BoardSquareRelationAnalyzer
from chess.graph import Graph, GraphComputationException
from chess.system import ComputationResult, InsertionResult, LoggingLevelRouter, id_emitter, EntityService
from chess.board import (
    Board, BoardAlreadyLaidOutException, BoardBuilder, BoardLayoutFailedException, BoardServiceException,
    BoardState, BoardValidator,
)
from chess.team import Team, TeamBelongsToDifferentBoardException, TeamService, TeamSlotAlreadyOccupiedException
from chess.token import TokenStackState


class BoardService(EntityService[Board]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Board microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Board state by providing single entry and exit points to Board
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "BoardService"
    _square_relation_analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: BoardBuilder = BoardBuilder(),
            validator: BoardValidator = BoardValidator(),
            square_relation_analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer()
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (BoardFactory)
            *   validator (BoardValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._square_relation_analyzer = square_relation_analyzer
    
    @property
    def builder(self) -> BoardBuilder:
        """get BoardBuilder"""
        return cast(BoardBuilder, self.entity_builder)
    
    @property
    def validator(self) -> BoardValidator:
        """get BoardValidator"""
        return cast(BoardValidator, self.entity_validator)
    
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
                    message=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERROR_CODE}",
                    ex=team_validation.exception
                ),
            )
        # Handle the case that, the team belongs on a different board.
        if not board == team.board:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERROR_CODE}",
                    ex=TeamBelongsToDifferentBoardException(
                        message=f"{method}: {TeamBelongsToDifferentBoardException.DEFAULT_MESSAGE}",
                    ),
                )
            )
        # Handle the case that, the team's slot is already occupied.
        if board.team_hash.slot_is_occupied(team):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERROR_CODE}",
                    ex=TeamSlotAlreadyOccupiedException(
                        f"{method}: {TeamSlotAlreadyOccupiedException.DEFAULT_MESSAGE}"
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
                    message=f"ServiceId:{self.id}, {method}: {BoardServiceException}",
                    ex=
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
                    f"{method}: {BoardServiceException.DEFAULT_MESSAGE}",
                    ex=BoardLayoutFailedException(
                        message=f"{method}: {BoardLayoutFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the board has already been laid out.
        if board.state == BoardState.HAS_TOKENS_LAID_OUT:
            # Return exception chain on failure
            return InsertionResult.failure(
                BoardServiceException(
                    f"{method}: {BoardServiceException.DEFAULT_MESSAGE}",
                    ex=BoardLayoutFailedException(
                        message=f"{method}: {BoardLayoutFailedException.DEFAULT_MESSAGE}",
                        ex=BoardAlreadyLaidOutException(
                            f"{method}: {BoardLayoutFailedException.DEFAULT_MESSAGE}",
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
                        f"{method}: {BoardServiceException.DEFAULT_MESSAGE}",
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
                    f"{method}: {BoardServiceException.DEFAULT_MESSAGE}",
                    ex=GraphComputationException(
                        message=f"{method}: {GraphComputationException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            )
        
        
        

        
            
        
        

