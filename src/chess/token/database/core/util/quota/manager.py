# src/chess/token/database/core/util/quota/manager.py

"""
Module: chess.token.database.core.util.quota.manager
Author: Banji Lawal
Created: 2026-01-31
version: 1.0.0
"""

from typing import List, cast

from chess.rank import Rank, RankService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.token import (
    RankQuotaComputationFailedException, RankQuotaManagerException, Token, TokenContext, TokenStack
)


class RankQuotaAnalyzer:
    """
    # ROLE: Quota management, Utility class.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Token objects and their lifecycles.
    3.  Ensure integrity of Token data stack
    4.  Stack data structure for Token objects with no guarantee of uniqueness.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute_rank_size_in_stack(
            cls,
            rank: Rank,
            token_stack: TokenStack,
            rank_service: RankService = RankService(),
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
            *   RankQuotaManagerException
            *   RankQuotaComputationFailedException
        """
        method = "RankQuotaAnalyzer.compute_rank_size_in_stack"
        
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaManagerException(
                    message=f"{method}: {RankQuotaManagerException.DEFAULT_MESSAGE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.DEFAULT_MESSAGE}",
                        ex=rank_validation.exception
                    )
                )
            )
        # --- Cast the context_build_result payload and run a search-by-rank on token-stack. ---#
        search_result = token_stack.query(context=TokenContext(rank=rank))
        
        # Handle the case that the search was not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaManagerException(
                    message=f"{method}: {RankQuotaManagerException.DEFAULT_MESSAGE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.DEFAULT_MESSAGE}",
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
    def stack_has_opening_for_rank(
            cls,
            rank: Rank,
            token_stack: TokenStack,
            rank_service: RankService = RankService(),
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
            *   RankQuotaManagerException
            *   RankQuotaComputationFailedException
        """
        method = "RankQuotaAnalyzer.stack_has_opening_for_rank"
        
        # Handle the case that the rank is not certified safe.
        openings_count_result = cls.count_openings_for_rank(
            rank=rank,
            token_stack=token_stack,
            rank_service=rank_service,
        )
        if openings_count_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaManagerException(
                    message=f"{method}: {RankQuotaManagerException.DEFAULT_MESSAGE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.DEFAULT_MESSAGE}",
                        ex=openings_count_result.exception
                    )
                )
            )
        
        # --- Find if there are open slots for the rank. ---#
        has_opening = cast(int, openings_count_result.payload) > 0
        return ComputationResult.success(payload=has_opening)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def count_openings_for_rank(
            cls,
            rank: Rank,
            token_stack: TokenStack,
            rank_service: RankService = RankService(),
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
            *   RankQuotaManagerException
            *   RankQuotaComputationFailedException
        """
        method = "RankQuotaAnalyzer.count_openings_for_rank"
        
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaManagerException(
                    message=f"{method}: {RankQuotaManagerException.DEFAULT_MESSAGE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.DEFAULT_MESSAGE}",
                        ex=rank_validation.exception
                    )
                )
            )
        # --- Find if there are open slots for the rank. ---#
        rank_size_computation = cls.stack_has_opening_for_rank(
            rank=rank,
            token_stack=token_stack,
            rank_service=rank_service,
        )
        
        # Handle the case that the rank_count_result_computation was not completed.
        if rank_size_computation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaManagerException(
                    message=f"{method}: {RankQuotaManagerException.DEFAULT_MESSAGE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.DEFAULT_MESSAGE}",
                        ex=rank_size_computation.exception
                    )
                )
            )
        # --- On success send the difference between the quota and rank_member_count in the ComputationResult. ---#
        number_of_openings = rank.team_quota - rank_size_computation.payload
        return ComputationResult.success(number_of_openings)