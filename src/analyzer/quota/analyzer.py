# src/logic/token/database/kernel/operation/quota/validator.py

"""
Module: logic.token.database.kernel.operation.quota.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from analyzer import Analyzer
from bootstrapper.analyzer.quota.bootstrapper import QuotaAnalyzerBootstrapper
from err import RankQuotaAnalyzerException
from model import Rank
from report import RankQuotaReport
from result import AnalysisResult, MethodResultType
from stack import TokenStackService
from util import LoggingLevelRouter


class RankQuotaAnalyzer(Analyzer):
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
    _bootstrapper: QuotaAnalyzerBootstrapper | None = QuotaAnalyzerBootstrapper()
 

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
        
        bootstrapper_result = self._bootstrapper.execute(rank=rank, token_stack=token_stack)
        # Handle the case that the bootstrapper does not produce a result.
        if bootstrapper_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                RankQuotaAnalyzerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankQuotaAnalyzerException.MSG,
                    err_code=RankQuotaAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=bootstrapper_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return bootstrapper_result