# src/tester/promotion/rank/tester.py

"""
Module: tester.promotion.rank.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from analyzer import RankReadinessAnalyzer
from err import PromoteToKingException, PromoteToPawnException, PromotionLevelTesterException
from model import King, Pawn, Rank
from result import MethodResultType, ValidationResult
from tester import Tester
from util import LoggingLevelRouter
from validator import RankValidator


class PromotionLevelTester(Tester):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a valid promotion level
        
    Attributes:
        validator: RankValidator
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _validator: RankValidator
    
    def __init__(
            self,
            validator: RankValidator | None = RankValidator(),
    ):
        """
        Args:
            validator: RankValidator
        """
        self._validator = validator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, subject: Any) -> ValidationResult:
        """
        Verifies the subject is a promotable rank.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   the elevation is to either Pawn or King.
            2.  Otherwise, Send the success result.
        Args:
            subject: Any
        Returns:
            ValidationResult[Rank]
        Raises:
            PromotionLevelTesterException
            PromoteToPawnException
            PromoteToKingException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is malformed
        validation_result = self._validator.execute(candidate=subject)
        if validation_result.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionLevelTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionLevelTesterException.MSG,
                    err_code=PromotionLevelTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=validation_result.exception
                )
            )
        rank = cast(Rank, subject)

        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionLevelTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionLevelTesterException.MSG,
                    err_code=PromotionLevelTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=PromoteToKingException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromoteToKingException.MSG,
                        err_code=PromoteToKingException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the new rank is still a Rank's.
        if isinstance(rank, Pawn):
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionLevelTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionLevelTesterException.MSG,
                    err_code=PromotionLevelTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=PromoteToPawnException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromoteToPawnException.MSG,
                        err_code=PromoteToPawnException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(rank)
