# src/chess/board/token/service.py

"""
Module: chess.board.token.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import cast

from chess.board import (
    AddingBoardTokenFailedException, BoardTokenRelationAnalyzer, BoardTokenServiceException,
    BoardTokenServiceIsFullException
)
from chess.team import TeamRankQuotaFullException
from chess.token import Token, TokenContext, UniqueTokenDataService
from chess.system import NUMBER_OF_COLUMNS, InsertionResult, ROW_SIZE


class BoardTokenService:
    _capacity: int
    _members: UniqueTokenDataService
    _analyzer: BoardTokenRelationAnalyzer
    
    def __init__(
            self,
            capacity: int = ROW_SIZE * NUMBER_OF_COLUMNS,
            members: UniqueTokenDataService = UniqueTokenDataService(),
            analyzer: BoardTokenRelationAnalyzer = BoardTokenRelationAnalyzer(),
    ):
        self._capacity = capacity
        self._analyzer = analyzer
        self._members = members
    
    @property
    def is_empty(self) -> bool:
        return self._members.is_empty
    
    @property
    def is_full(self) -> bool:
        return self._members.size == self._capacity
    
    @property
    def number_of_members(self) -> int:
        return self._members.size
    
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
            *   FillingTeamRosterFailedException
            *   EnemyCannotJoinTeamRosterException
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
        token_validation = self._members.integrity_service.validator.validate(token=token)
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
        # --- Get the rank's quota. ---#
        rank_quota_lookup = self._members.lookup_team_rank_quote(token.rank)
        
        # Handle the case that the rank_quota_lookup was not completed.
        if rank_quota_lookup.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=rank_quota_lookup.exception
                    )
                )
            )
        rank_quota = cast(int, rank_quota_lookup.payload)
        
        # --- Find if there are open slots for the token's rank. ---#
        rank_count_result = self._members.rank_count(rank=token.rank)
        
        # Handle the case that the rank_count_result_computation was not completed.
        if rank_count_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=rank_count_result.exception
                    )
                )
            )
        # Handle the case that the rank's quota has been filled.
        if rank_quota >= cast(int, rank_count_result.payload):
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardTokenServiceException(
                    message=f"{method}: {BoardTokenServiceException.ERROR_CODE}",
                    ex=AddingBoardTokenFailedException(
                        message=f"{method}: {AddingBoardTokenFailedException.ERROR_CODE}",
                        ex=TeamRankQuotaFullException(f"{method}: {TeamRankQuotaFullException.DEFAULT_MESSAGE}")
                    )
                )
            )

        
        # --- Find out if a token is already at the coord ---#
        search_result = self._members.search_tokens(context=TokenContext(coord=token.current_position))
        
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
        insertion_result = self._members.add_unique_token(token=token)
        
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