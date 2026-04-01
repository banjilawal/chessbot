# src/logic/square/database/kernel/operation/quota/validator.py

"""
Module: logic.square.database.kernel.operation.quota.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations


from logic.system import ComputationResult, LoggingLevelRouter
from logic.square import SquareStackService


class SquareStackCapacityAnalysis:
    """
    Role:
        - Statistical Analyzer
        - Report Generator

    Responsibilities:
        1.  Produce a report of how many openings a SquareStackService instance has for
            a rank.


    Attributes:

    Provides:
        -   analyze(
                    square_stack: SquareStackService,
            ) -> ComputationResult[SquareStackCapacityReport]

    Super:
    """
 
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls,  square_stack: SquareStackService, ) -> SquareStackCapacityReport:
        """
        Create a SquareStackCapacityReport.
        
        Actions:
            1.  Send an exception chain in the ComputationResult if:
                    *   The rank search fails.
            2.  Otherwise, send the success result.
        Args:
            square_stack: SquareStack
        Returns:
            ComputationResult[SquareStackCapacityReport]
        Raises:
            RankQutaAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        # Handle the case that, the rank does not pass a validation check.
        rank_validation_result = rank_service.validator.query(rank)
        if rank_validation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                SquareStackCapacityAnalysisException(
                    mthd=method,
                    op=SquareStackCapacityAnalysisException.OP,
                    msg=SquareStackCapacityAnalysisException.MSG,
                    err_code=SquareStackCapacityAnalysisException.ERR_CODE,
                    rslt_type=SquareStackCapacityAnalysisException.RSLT_TYPE,
                    ex=rank_validation_result.exception
                )
            )
        # --- Search for the stack for rank members. ---#
        rank_search_result = square_stack.query(context=SquareContext(rank=rank))
        
        # Handle the case that, a search error occurred.
        if rank_search_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                SquareStackCapacityAnalysisException(
                    mthd=method,
                    op=SquareStackCapacityAnalysisException.OP,
                    msg=SquareStackCapacityAnalysisException.MSG,
                    err_code=SquareStackCapacityAnalysisException.ERR_CODE,
                    rslt_type=SquareStackCapacityAnalysisException.RSLT_TYPE,
                    ex=rank_search_result.exception
                )
            )
        # --- Send the work product. ---#
        return ComputationResult.success(
            SquareStackCapacityReport(
                rank=rank,
                number_of_openings=rank.persona.quota - len(rank_search_result.payload),
            )
        )