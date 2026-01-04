from typing import List, cast

from chess.rank import Rank
from chess.system import CalculationResult, InsertionResult
from chess.team import (
    AddCapturedTeamMemberException, AddingRosterMemberFailedException, Team, RosterRelationAnalyzer, RosterTable,
    TeamRankQuotaFullException, TokenBelongsOnDifferentRosterException
)
from chess.token import AddingDuplicateTokenException, Token, TokenContext, UniqueTokenDataService
from chess.token.model.combatant.token import CombatantToken


class RosterService:
    _table: RosterTable
    _tokens: UniqueTokenDataService
    _analyzer: RosterRelationAnalyzer

    
    def __init__(
            self,
            table: RosterTable = RosterTable(),
            tokens: UniqueTokenDataService = UniqueTokenDataService(),
            analyzer: RosterRelationAnalyzer = RosterRelationAnalyzer(),
    ):
        self._table = table
        self._tokens = tokens
        self._analyzer = analyzer
        
        
    def member_insertion(self, team: Team, piece: Token) -> InsertionResult[Token]:
        method = "RosterService.member_insertion"
        
        piece_validation = self._tokens.token_service.validator.validate(piece)
        if piece_validation.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=piece_validation.exception
                )
            )
        if piece.team != team:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=TokenBelongsOnDifferentRosterException(
                        f"{method}: {TokenBelongsOnDifferentRosterException.DEFAULT_MESSAGE}"
                    )
                )
            )
        if isinstance(CombatantToken, piece) and cast(CombatantToken, piece).captor is not None:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=AddCapturedTeamMemberException(f"{method}: {AddCapturedTeamMemberException.DEFAULT_MESSAGE}")
                )
            )
        search_result = self._tokens.search_tokens(context=TokenContext(piece.id))
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
                )
            )
        calculation_result = self._calculate_remaining_rank_quota(piece.rank)
        if calculation_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=calculation_result.exception
                )
            )
        remaining_slots = cast(int, calculation_result.payload)
        # Handle the case that the rank has been filled.
        if remaining_slots <= 0:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=TeamRankQuotaFullException(f"{method}: {TeamRankQuotaFullException.DEFAULT_MESSAGE}")
                )
            )
        insertion_result = self._tokens.add_token(token=piece)
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        payload = insertion_result.payload
        self._table.decrease_quota(rank=piece.rank)
        return InsertionResult.success(payload=payload)
    
    def _calculate_remaining_rank_quota(
            self,
            rank: Rank,
    ) -> CalculationResult[int]:
        """
        # ACTION:
            1.  If either the team or rank are not certified send the exception in the CalculationResult.
                Else, search the roster by the rank.
            2.  If the search did not complete send the exception in the CalculationResult.
            3.  Calculate rank.team_quota - len(matches) and send in the CalculationResult.
        # PARAMETERS:
            *   team (Team)
            *   rank (Rank)
            *   rank_service (RankService)
        # RETURN:
            *   CalculationReport[Rank, int] containing either:
                - On failure: Exception
                - On success: (Rank, int) tuple
        # RAISES:
            *   TeamServiceException
        """
        method = "TeamService.calculate_remaining_rank_quota"
        

        # --- Search the team's roster for tokens that share the persona's rank. ---#
        search_result = self._members.search_tokens(context=TokenContext(rank=rank))
        
        # Handle the case that the search did not succeed
        if search_result.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(search_result.exception)
        if search_result.is_success:
            # Handle the case that the payload  is not a list.
            if not isinstance(List[Token], search_result.payload):
                # Return the exception chain on failure.
                return CalculationResult.failure(
                    AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=TypeError(f"{method}: Expected List[Token], got {search_result.payload.__name__} instead.")
                    )
                )
            # Send how many slots are open.
            return CalculationResult.success(payload=(rank.team_quota - len(cast(List, search_result.payload))))
        # Else the search was empty just send the quota.
        return CalculationResult.success(payload=rank.team_quota)