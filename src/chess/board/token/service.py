# src/chess/board/token/service.py

"""
Module: chess.board.token.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import (
    AddingBoardTokenFailedException, BoardTokenRelationAnalyzer, BoardTokenServiceException,
    BoardTokenServiceIsFullException
)
from chess.token import Token, TokenContext, UniqueTokenDataService
from chess.system import COLUMN_SIZE, InsertionResult, ROW_SIZE


class BoardTokenService:
    _capacity: int
    _data_service: UniqueTokenDataService
    _analyzer: BoardTokenRelationAnalyzer
    
    def __init__(
            self,
            capacity: int = ROW_SIZE * COLUMN_SIZE,
            data_service: UniqueTokenDataService = UniqueTokenDataService(),
            analyzer: BoardTokenRelationAnalyzer = BoardTokenRelationAnalyzer(),
    ):
        self._capacity = capacity
        self._analyzer = analyzer
        self._data_service = data_service
    
    @property
    def is_empty(self) -> bool:
        return self._data_service.is_empty
    
    @property
    def is_full(self) -> bool:
        return self._data_service.size == self._capacity
    
    @property
    def number_of_tokens(self) -> int:
        return self._data_service.size
    
    @property
    def board_token_analyzer(self) -> BoardTokenRelationAnalyzer:
        return self._analyzer
    
    def add(self, token: Token) -> InsertionResult[Token]:
        """
        # ACTION:
            1.  If the token fails validation send the wrapped exception in the InsertionResult.
            2.  If the token does not belong to the board a wrapped exception needs to be sent in the InsertionResult.
            3.  If token is a captured CombatantToked a wrapped exception needs to be sent in the InsertionResult.
            4.  If self._calculate_remaining_rank_quota returns an error or zero open slots then send the wrapped
                in the InsertionResult.
            5.  Send the number of open slots in the InsertionResult.
        # PARAMETERS:
            *   rank (Rank)
        # RETURN:
            *   CalculationReport[int] containing either:
                - On failure: Exception
                - On success: int
        # RAISES:
            *   BoardRankQuotaFullException
            *   AddingDuplicateTokenException
            *   AddingCapturedBoardMemberException
            *   AddingRosterMemberFailedException
            *   EnemyCannotJoinRosterException
        """
        method = "RosterService.member_insertion"
        
        # Handle the case that the BoardTokenService is at capacity.
        if self.is_full:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=BoardTokenServiceIsFullException(
                            f"{method}: {BoardTokenServiceIsFullException.DEFAULT_MESSAGE}"
                            )
                    )
                )
            )
        # Handle the case that the token is not certified safe.
        token_validation = self._data_service.integrity_service.validator.validate(token=token)
        if token_validation.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        # --- Find out if a token is already at the coord ---#
        search_result = self._data_service.search_tokens(context=TokenContext(coord=token.coord))
        
        # Handle the case that the search was not completed.
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that the coord is already in use.
        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=BoardTokenCoordCollisionException(
                            f"{method}: {BoardTokenCoordColliionException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Run the insertion operation on the DataService. ---#
        insertion_result = self._data_service.add_unique_token(token=token)
        
        # Handle the case that the insertion was not completed
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On insertion success extract the insertion payload and send in the BuildResult. ---#
        return InsertionResult.success(cast(Token, insertion_result.payload))