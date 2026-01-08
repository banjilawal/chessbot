
from typing import List, cast


from chess.system import InsertionResult
from chess.team import (
    AddingActiveTokenException, AddingHostageTokenFailedException, EnemyAlreadyCapturedException,
    FriendCannotCaptureFriendException, HostageRelationAnalyzer,
)
from chess.token import TokenContext, UniqueTokenDataService



class HostageService:
    _prisoners: UniqueTokenDataService
    _analyzer: HostageRelationAnalyzer
    
    def __init__(
            self,
            prisoners: UniqueTokenDataService = UniqueTokenDataService(),
            analyzer: HostageRelationAnalyzer = HostageRelationAnalyzer(),
    ):
        self._prisoners = prisoners
        self._analyzer = analyzer
    
    
    def add_prisoner(self, combatant: CombatantToken) -> InsertionResult[CombatantToken]:
        """
        # ACTION:
            1.  If the combatant fails validation send the wrapped exception in the InsertionResult.
            2.  If the combatant does not belong to the team a wrapped exception needs to be sent in the InsertionResult.
            3.  If combatant is a captured CombatantToked a wrapped exception needs to be sent in the InsertionResult.
            4.  If self._calculate_remaining_rank_quota returns an error or zero open slots then send the wrapped
                in the InsertionResult.
            5.  Send the number of open slots in the InsertionResult.
        # PARAMETERS:
            *   combatant (CombatantToken)
        # RETURN:
            *   InsertionResult[CombatantToken] containing either:
                - On failure: Exception
                - On success: CombatantToken
        # RAISES:
            *   TeamRankQuotaFullException
            *   EnemyAlreadyCapturedException
            *   CannotCaptureKingException
            *   AddingHostageTokenFailedException
            *   AddingActiveTokenException
        """
        method = "RosterService.member_insertion"
        
        # Handle the case that the combatant fails validation.
        combatant_validation = self._prisoners.token_service.validator.validate(combatant)
        if combatant_validation.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingHostageTokenFailedException(
                    message=f"{method}: {AddingHostageTokenFailedException.ERROR_CODE}",
                    ex=combatant_validation.exception
                )
            )
        # Handle the case that the combatant has not been captured.
        if combatant.captor is None:
            # Return exception chain.
            return InsertionResult.failure(
                AddingHostageTokenFailedException(
                    message=f"{method}: {AddingHostageTokenFailedException.ERROR_CODE}",
                    ex=AddingActiveTokenException(f"{method}: {AddingActiveTokenException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the combatant was captured by a friend.
        if not combatant.captor.is_enemy(combatant):
            # Return exception chain.
            return InsertionResult.failure(
                AddingHostageTokenFailedException(
                    message=f"{method}: {AddingHostageTokenFailedException.ERROR_CODE}",
                    ex=FriendCannotCaptureFriendException(
                        f"{method}: {FriendCannotCaptureFriendException.DEFAULT_MESSAGE}")
                    
                )
            )
        # --- Search the collection for the token. ---#
        search_result = self._prisoners.search_tokens(context=TokenContext(combatant.id))
        
        # Handle the case that search did not complete.
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingHostageTokenFailedException(
                    message=f"{method}: {AddingHostageTokenFailedException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # Handle the case that the token is already present.
        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingHostageTokenFailedException(
                    message=f"{method}: {AddingHostageTokenFailedException.ERROR_CODE}",
                    ex=EnemyAlreadyCapturedException(f"{method}: {EnemyAlreadyCapturedException.DEFAULT_MESSAGE}")
                )
            )
        # --- Run the insertion operation on the DataService. ---#
        insertion_result = self._prisoners.add_token(token=combatant)
        
        # Handle the case that the insertion was not completed
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingHostageTokenFailedException(
                    message=f"{method}: {AddingHostageTokenFailedException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        payload = insertion_result.payload
        return InsertionResult.success(payload=payload)