# src/microservice/board/microservice.py

"""
Module: microservice.board.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import BoardBuilder, BoardValidator
from logic.board import BoardRelationAnalyzer
from microservice import Microservice, BoardTeamBinderService
from model import Board


class BoardService(Microservice[Board]):
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Board microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Board state by providing single entry and exit points to Board
        lifecycle.

    Super Class:
        *   Microservice

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Microservice for inherited attributes.
    """
    SERVICE_NAME = "BoardService"
    _team_binder_service: BoardTeamBinderService
    _relation_analyzer: BoardRelationAnalyzer
    
    def __init__(
            self,
            id: int | None = None,
            name: str | None = None,
            builder: BoardBuilder | None = None,
            validator: BoardValidator | None = None,
            team_binder_service: BoardTeamBinderService | None = None,
            relation_analyzer: BoardRelationAnalyzer = BoardRelationAnalyzer()
    ):
        """
        Args:
                id: int
                name: str
                builder: BoardBuilder
                validator: BoardValidator
                square_relation_analyzer: SquareRelationAnalyzer
        """
        super().__init__(id=id, name=name)
        self._builder = builder or BoardBuilder()
        self._validator = validator or BoardValidator()
        self._team_binder_service = team_binder_service or BoardTeamBinderService()
        self._relation_analyzer = relation_analyzer
    
    @property
    def builder(self) -> BoardBuilder:
        return self._builder
    
    @property
    def validator(self) -> BoardValidator:
        return self._validator
    
    @property
    def relation_analyzer(self) -> BoardRelationAnalyzer:
        return  self._relation_analyzer
    
    @property
    def team_binder_service(self) -> BoardTeamBinderService:
        return self._team_binder_service
    
    @LoggingLevelRouter.monitor
    def form_team_on_board(
            self,
            board: Board,
            team: Team,
            team_service: TeamService = TeamService()
    ) -> InsertionResult:
        method = "BoardService.forma_team_on_board"
        
        # Handle the case that, the team does not pass a validation check.
        team_validation = team_service.validate(candidate=team)
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardServiceException.ERR_CODE}",
                    ex=team_validation.exception
                ),
            )
        # Handle the case that, the team belongs on a different board.
        if not board == team.board:
            # Send the exception chain on failure.
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
            # Send the exception chain on failure.
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
            # Send the exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardServiceException}",
                ),
            )
    
    @LoggingLevelRouter.monitor
    def layout_board(self, board: Board) -> InsertionResult[bool]:
        method = "BoardService.layout_board"
        
        # Handle the case that, the board does not pass a validation check.
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
        for key in board.team_hash.entry.keys():
            deployment_result = board.team_hash.entry[key].roster.deploy_tokens_on_board
            
            # Handle the case that, the team's deployment is not completed.
            if deployment_result.is_failure:
                # Send the exception chain on failure.
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
    
        # Handle the case that, the board does not pass a validation check.
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
        
        
        

        
            
        
        

