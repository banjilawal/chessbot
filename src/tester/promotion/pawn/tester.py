# src/tester/promotion/pawn/tester.py

"""
Module: tester.promotion.pawn.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, cast

from analyzer import TokenReadinessAnalyzer
from err import (
    PawnDoublePromotionException, PawnPromotionRowException, PromoteInactivePawnException,
    PromotionPawnTesterException
)
from model import PawnToken
from report import TokenReadinessReport
from result import MethodResultType, ValidationResult
from tester import Tester

f


class PromotionPawnTester(Tester):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a pawn that can be promoted.
        
    Attributes:
        readiness_analyzer: TokenReadinessAnalyzer
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
        Tester
    """
    _readiness_analyzer: TokenReadinessAnalyzer
    
    def __init__(
            self,
            readiness_analyzer: TokenReadinessAnalyzer | None = TokenReadinessAnalyzer(),
    ):
        """
        Args:
            readiness_analyzer: TokenReadinessAnalyzer
        """
        self._readiness_analyzer = readiness_analyzer
    
    
    @LoggingLevelRouter.monitor
    def execute(self, subject: Any) -> ValidationResult:
        """
        Verifies the subject is a promotable pawn.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free pawn.
                    -   The pawn has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            subject: Any
        Returns:
            ValidationResult[PawnToken]
        Raises:
            PromotionPawnTesterException
            PromoteInactivePawnException
            PawnDoublePromotionException
            PawnPromotionRowException
            TypeError
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is malformed
        readiness_analysis_result = self._readiness_analyzer.execute(token=subject)
        # Handle the case that, the readiness analysis is not completed.
        if readiness_analysis_result.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionPawnTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPawnTesterException.MSG,
                    err_code=PromotionPawnTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=readiness_analysis_result.exception
                )
            )
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        # Handle the case that, the pawn is not free.
        if report.token_is_not_ready:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionPawnTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPawnTesterException.MSG,
                    err_code=PromotionPawnTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=PromoteInactivePawnException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromoteInactivePawnException.MSG,
                        err_code=PromoteInactivePawnException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the subject is not a pawn.
        if not isinstance(subject, PawnToken):
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionPawnTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPawnTesterException.MSG,
                    err_code=PromotionPawnTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=TypeError(
                        f"Expected type PawnToken for promotion. "
                        f"Got {type(subject).__name__} instead."
                    )
                )
            )
        pawn = cast(PawnToken, report.token)
        # Handle the case that, the pawn_token has already been promoted.
        if pawn.is_promoted:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionPawnTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPawnTesterException.MSG,
                    err_code=PromotionPawnTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=PawnDoublePromotionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PawnDoublePromotionException.MSG,
                        err_code=PawnDoublePromotionException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the is not on its promotion row..
        if pawn.current_position.row != pawn.team.enemy_rank_row:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionPawnTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPawnTesterException.MSG,
                    err_code=PromotionPawnTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=PawnPromotionRowException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        var=pawn.name,
                        msg=PawnPromotionRowException.MSG,
                        err_code=PawnPromotionRowException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(pawn)