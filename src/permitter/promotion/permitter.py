# src/permitter/promotion/permitter.py

"""
Module: permitter.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations
from typing import Type, cast

from bootstrapper import PrimingValidator
from err import PromotionPermitterException, PromotionRequestNullException
from model import PawnToken
from permitter import Permitter
from report import PromotionApprovalReport
from request.promotion import PromotionRequest
from tester import PromotionLevelTester, PromotionPawnTester
from util import LoggingLevelRouter


class PromotionPermitter(Permitter):
    """
    Role:
        -   Request Analyzer
        -   Rights Granter
        -   Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if promotion request can be granted.
        
    Attributes:
        pawn_tester: PromotionPawnTester
        rank_level: PromotionLevelTester
        priming_validator: PrimingValidator
        
    Provides:
        -   run(self, request: PromotionRequest) -> PromotionApprovalReport
        
    Super Class:
        Permitter
    """
    _pawn_tester: PromotionPawnTester
    _rank_level_tester: PromotionLevelTester
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            pawn_tester: PromotionPawnTester | None = PromotionPawnTester(),
            rank_level: PromotionLevelTester | None = PromotionLevelTester(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            pawn_tester: PromotionPawnTester
            rank_level: PromotionLevelTester
            priming_validator: PrimingValidator
        """
        self._pawn_tester = pawn_tester
        self._rank_level_tester = rank_level
        self._priming_validator = priming_validator
    
    
    @LoggingLevelRouter.monitor
    def run(self, request: PromotionRequest) -> PromotionApprovalReport:
        """
        Evaluate a pawn promotion request.
        
        Action:
            1.  Deny the request if any of the following occur:
                    -   The request is malformed.
                    -   The candidate does not satisfy the selection criteria.
                    -   A rank_level test fails.
            2.  Otherwise, approve the request.
        Args:
            request: PromotionRequest
        Returns:
            PromotionApprovalReport
        Raises:
            PromotionPermitterException
            PromotionRequestNullException
        """
        method = f"{self.__class__.__name__}.run"
        
        # Handle the case that, the request is malformed
        request_type_validation_result = self._priming_validator.execute(
            candidate=request,
            target_model=Type[PromotionRequest],
            null_exception=PromotionRequestNullException()
        )
        if request_type_validation_result.is_failure:
            # Send the exception chain in the permission denial.
            PromotionApprovalReport.deny(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=request_type_validation_result.exception,
                )
            )
        # Handle the case that, the requestor fails a test.
        pawn_test_result = self._pawn_tester.execute(request.candidate)
        if pawn_test_result.is_failure:
            # Send the exception chain in the permission denial.
            PromotionApprovalReport.deny(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=pawn_test_result.exception
                )
            )
        pawn = cast(PawnToken, pawn_test_result.payload)
        
        # Handle the case that, the promotion level test fails.
        rank_level_test_result = self._rank_level_tester.execute(request.rank_level)
        if rank_level_test_result.is_failure:
            # Send the exception chain in the permission denial.
            PromotionApprovalReport.deny(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=rank_level_test_result.exception
                )
            )
        rank_level = cast(
            type(request.rank_level),
            rank_level_test_result.payload
        )
        # --- Send the work product. ---#
        return PromotionApprovalReport.approve(pawn=pawn, rank_level=rank_level)
