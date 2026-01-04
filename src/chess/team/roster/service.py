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
        """
        # ACTION:
            1.  If the piece fails validation send the wrapped exception in the InsertionResult.
            2.  If the piece does not belong to the team a wrapped exception needs to be sent in the InsertionResult.
            3.  If piece is a captured CombatantToked a wrapped exception needs to be sent in the InsertionResult.
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
            *   TeamRankQuotaFullException
            *   AddingDuplicateTokenException
            *   AddCapturedTeamMemberException
            *   AddingRosterMemberFailedException
            *   TokenBelongsOnDifferentRosterException
        """
        method = "RosterService.member_insertion"
        
        # Handle the case that the piece fails validation.
        piece_validation = self._tokens.token_service.validator.validate(piece)
        if piece_validation.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=piece_validation.exception
                )
            )
        # Handle the case that the piece is on a different team.
        if piece.team != team:
            # Return exception chain.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=TokenBelongsOnDifferentRosterException(
                        f"{method}: {TokenBelongsOnDifferentRosterException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the piece is a captured combatant.
        if isinstance(piece, CombatantToken) and cast(CombatantToken, piece).captor is not None:
            # Return exception chain.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=AddCapturedTeamMemberException(f"{method}: {AddCapturedTeamMemberException.DEFAULT_MESSAGE}")
                )
            )
        # --- Search the collection for the token. ---#
        search_result = self._tokens.search_tokens(context=TokenContext(piece.id))
        
        # Handle the case that search did not complete.
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # Handle the case that the token is already present.
        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
                )
            )
        # --- Find how many slots are open for the rank. ---#
        calculation_result = self._calculate_remaining_rank_quota(piece.rank)
        
        # Handle the case that the calculation operation was not completed.
        if calculation_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=calculation_result.exception
                )
            )
        # --- Make sure the payload is an int. ---#
        remaining_slots = cast(int, calculation_result.payload)
        
        # Handle the case that the rank has been filled.
        if remaining_slots <= 0:
            # Return exception chain.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=TeamRankQuotaFullException(f"{method}: {TeamRankQuotaFullException.DEFAULT_MESSAGE}")
                )
            )
        # --- Run the insertion operation on the DataService. ---#
        insertion_result = self._tokens.add_token(token=piece)
        
        #Handle the case that the insertion was not completed
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # Get the payload from insertion result. Decrease the rank's quota. Send the payload to the caller.
        payload = insertion_result.payload
        self._table.decrease_quota(rank=piece.rank)
        return InsertionResult.success(payload=payload)
    
    def _calculate_remaining_rank_quota(self,rank: Rank,) -> CalculationResult[int]:
        """
        # ACTION:
            1.  Search self._tokens for pieces with the rank. If the search fails send the wrapped exception
                in the CalculationResult.
            2.  If no matches are found send rank.team_quota in the CalculationResult.
            3.  If matches are found ut the payload is not a List[Token] send the wrapped exception in the
                CalculationResult. Else send team_quota - len(matches) in the CalculationResult.
        # PARAMETERS:
            *   rank (Rank)
        # RETURN:
            *   CalculationReport[int] containing either:
                - On failure: Exception
                - On success: int
        # RAISES:
            *   TypeError
            *   AddingRosterMemberFailedException
        """
        method = "TeamService._calculate_remaining_rank_quota"
        
        # --- Search the team's roster for tokens that share the persona's rank. ---#
        search_result = self._tokens.search_tokens(context=TokenContext(rank=rank))
        
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