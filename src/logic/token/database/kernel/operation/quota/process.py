# src/logic/token/database/kernel/operation/quota/validator.py

"""
Module: logic.token.database.kernel.operation.quota.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import Rank, RankService
from logic.system import ComputationResult, LoggingLevelRouter
from logic.token import RankQuotaAnalysisException, RankQuotaReport, TokenContext, TokenStackService


class RankQuotaAnalysis:
    """
    Role:
        - Statistical Analyzer
        - Report Generator

    Responsibilities:
        1.  Produce a report of how many openings a TokenStackService instance has for
            a rank.


    Attributes:

    Provides:
        -   execute(
                    rank: Rank,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
            ) -> ComputationResult[RankQuotaReport]

    Super:
    """
 
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            rank: Rank,
            token_stack: TokenStackService,
            rank_service: RankService = RankService(),
    ) -> ComputationResult[RankQuotaReport]:
        """
        Create a RankQuotaReport.
        
        Actions:
            1.  Send an exception chain in the ComputationResult if:
                    *   The rank does not pass a validation check.
                    *   The rank search fails.
            2.  Otherwise, send the success result.
        Args:
            rank: Rank
            token_stack: TokenStack
            rank_service: RankService
        Returns:
            ComputationResult[RankQuotaReport]
        Raises:
            RankQutaAnalysisException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the rank does not pass a validation check.
        rank_validation_result = rank_service.validator.validate(rank)
        if rank_validation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaAnalysisException(
                    mthd=method,
                    op=RankQuotaAnalysisException.OP,
                    msg=RankQuotaAnalysisException.MSG,
                    err_code=RankQuotaAnalysisException.ERR_CODE,
                    rslt_type=RankQuotaAnalysisException.RSLT_TYPE,
                    ex=rank_validation_result.exception
                )
            )
        # --- Search for the schema for rank members. ---#
        rank_search_result = token_stack.search(context=TokenContext(rank=rank))
        
        # Handle the case that, a search error occurred.
        if rank_search_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RankQuotaAnalysisException(
                    mthd=method,
                    op=RankQuotaAnalysisException.OP,
                    msg=RankQuotaAnalysisException.MSG,
                    err_code=RankQuotaAnalysisException.ERR_CODE,
                    rslt_type=RankQuotaAnalysisException.RSLT_TYPE,
                    ex=rank_search_result.exception
                )
            )
        # --- Send the work product. ---#
        return ComputationResult.success(
            RankQuotaReport(
                rank=rank,
                number_of_openings=rank.persona.quota - len(rank_search_result.payload),
            )
        )