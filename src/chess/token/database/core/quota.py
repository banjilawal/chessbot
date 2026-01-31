# src/chess/token/database/core/service_.py

"""
Module: chess.token.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.formation import FormationService
from chess.rank import Rank, RankService
from chess.system import (
    ComputationResult, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter
)
from chess.token import (
    AppendingTokenDirectlyIntoItemsFailedException, PoppingEmptyTokenStackException, Token, TokenContext, TokenService,
    TokenDataServiceException, TokenDoesNotExistForRemovalException, TokenContextService, TokenDeletionFailedException,
    TokenInsertionFailedException, RankCountCalculationFailedException, TokenServiceCapacityException,
)
from chess.token.database.core.stack import TokenStack


class RankQuotaManager:
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Token objects and their lifecycles.
    3.  Ensure integrity of Token data stack
    4.  Stack data structure for Token objects with no guarantee of uniqueness.

    # PARENT:
        *   StackService[Token]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """

    
    @LoggingLevelRouter.monitor
    def rank_quota(self, token_stack: TokenStack, rank: Rank) -> ComputationResult[int]:
        """
        # ACTION:
            1.  If formation_service fails to return a quota value, send the exception chain in the ComputationResult.
                Else, directly forward quota_result to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenDataServiceException
        """
        method = "TokenStack.team_max_tokens_per_rank"
        
        # --- Handoff the rank validation and quote lookup to self._formation_service ---#
        
        # Handle the case that the quota lookup is not completed.
        quota_result = self._formation_service.persona_service.quota_per_rank(rank=rank)
        if quota_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=quota_result.exception
                )
            )
        # On success just forward the quota_result to the caller.
        return quota_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def rank_size(
            cls,
            rank: Rank,
            token_stack: TokenStack,
            rank_service: RankService = RankService()
    ) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Build the search-by-rank TokenContext. If the build fails send the exception in the InsertionResult.
                Else run the search.
            2.  If the search fails send the exception in the InsertionResult. Else the calculation was successful.
                Return the number of hits in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenDataServiceException
            *   RankCountCalculationFailedException
        """
        method = "TokenStack.number_of_rank_members"
        
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=rank_validation.exception
                    )
                )
            )
        
        # --- Cast the context_build_result payload and run the search. ---#
        search_result = token_stack.context_service.finder.find(context=TokenContext(rank=rank))
        
        # Handle the case that the search was not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that no tokens hold the rank
        if search_result.is_empty:
            return ComputationResult.success(payload=0)
        # Handle the case that some hits were found
        return ComputationResult.success(payload=len(cast(List[Token], search_result.payload)))
  
    @classmethod
    @LoggingLevelRouter.monitor
    def has_slot_for_rank(
            cls,
            rank: Rank,
            token_stack: TokenStack,
    ) -> ComputationResult[bool]:
        """
        # ACTION:
            1.  If self.count_rank_openings fails send the exception chain in the ComputationResult. Else,
                send open_slot_count > 0 in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
        # RETURN:
            *   CalculationReport[bool] containing either:
                    - On failure: Exception
                    - On success: bool
        # RAISES:
            *   TokenDataServiceException
            *   RankCountCalculationFailedException
        """
        method = "TokenStack.has_slot_for_rank"
        
        # Handle the case that the rank is not certified safe.
        openings_count_result = cls.count_rank_openings(token_stack=token_stack, rank=rank)
        if openings_count_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=openings_count_result.exception
                    )
                )
            )
        
        # --- Find if there are open slots for the rank. ---#
        has_opening = cast(int, openings_count_result.payload) > 0
        return ComputationResult.success(payload=has_opening)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def count_rank_openings(
            cls,
            rank: Rank,
            token_stack: TokenStack,
            rank_service: RankService = RankService()
    ) -> ComputationResult[int]:
        """
        # ACTION:
            1.  If the rank is not validated, send an exception chain in the ComputationResult.
            2.  If calculating the number of rank members fails send an exception chain in the ComputationResult.
                Else, send rank.team_quota - rank_members in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
            *   rank_service (RankService
        # RETURN:
            *   CalculationReport[int] containing either:
                    - On failure: Exception
                    - On success: int
        # RAISES:
            *   TokenDataServiceException
            *   RankCountCalculationFailedException
        """
        method = "TokenStack.count_rank_openings"
        
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=rank_validation.exception
                    )
                )
            )
        # --- Find if there are open slots for the rank. ---#
        rank_size_computation = cls.rank_size(token_stack=token_stack, rank=rank)
        
        # Handle the case that the rank_count_result_computation was not completed.
        if rank_size_computation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=rank_size_computation.exception
                    )
                )
            )
        # --- On success send the difference between the quota and rank_member_count in the ComputationResult. ---#
        number_of_openings = rank.team_quota - rank_size_computation.payload
        return ComputationResult.success(number_of_openings)