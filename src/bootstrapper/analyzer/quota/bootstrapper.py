# src/logic/token/database/kernel/operation/quota/validator.py

"""
Module: logic.token.database.kernel.operation.quota.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from typing import Type

from bootstrapper import AnalyzerBootstrapper, PrimingValidator
from context import TokenContext
from model import Rank
from report import RankQuotaReport
from result import AnalysisResult, MethodResultType
from stack import TokenStackService
from util import LoggingLevelRouter
from validator import RankValidator


class QuotaAnalyzerBootstrapper(AnalyzerBootstrapper):
    """
    Role:
        - Statistical Analyst
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
            ) -> AnalysisResult[RankQuotaReport]

    Super:
    """
    _priming_validator: PrimingValidator | None = PrimingValidator()
    _rank_validator: RankValidator | None = RankValidator()
 
    @LoggingLevelRouter.monitor
    def execute(self, rank: Rank, token_stack: TokenStackService) -> AnalysisResult[RankQuotaReport]:
        """
        Create a RankQuotaReport.
        
        Actions:
            1.  Send an exception chain in the AnalysisResult if:
                    -   The rank does not pass a validation check.
                    -   The rank search fails.
            2.  Otherwise, send the success result.
        Args:
            rank: Rank
            token_stack: TokenStack
            rank_service: RankService
        Returns:
            AnalysisResult[RankQuotaReport]
        Raises:
            RankQutaAnalystException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, token_stack is null or the the wrong type
        stack_validation_result = self._priming_validator.execute(
            candidate=token_stack,
            target_model=Type[TokenStackService],
            null_exception=TokenStackNullException(),
        )
        if stack_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                QuotaAnalyzerBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuotaAnalyzerBootstrapperException.MSG,
                    err_code=QuotaAnalyzerBootstrapperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=stack_validation_result.exception
                )
            )
        # Handle the case that, the rank does not pass a validation check.
        rank_validation_result = self._rank_validator.execute(candidate=rank)
        if rank_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                QuotaAnalyzerBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuotaAnalyzerBootstrapperException.MSG,
                    err_code=QuotaAnalyzerBootstrapperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=rank_validation_result.exception
                )
            )
        # --- Search for the schema for rank members. ---#
        rank_search_result = token_stack.search(context=TokenContext(rank=rank))
        
        # Handle the case that, a search error occurred.
        if rank_search_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                QuotaAnalyzerBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=QuotaAnalyzerBootstrapperException.MSG,
                    err_code=QuotaAnalyzerBootstrapperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=rank_search_result.exception
                )
            )
        # --- Send the work product. ---#
        return AnalysisResult.success(
            RankQuotaReport(
                rank=rank,
                number_of_openings=rank.persona.quota - len(rank_search_result.payload),
            )
        )