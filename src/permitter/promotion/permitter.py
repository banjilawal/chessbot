# src/permitter/promotion/permitter.py

"""
Module: permitter.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from err import PromotionPermitterException
from permitter import Permitter
from report import PromotionApprovalReport
from request.promotion import PromotionRequest
from tester import PromotionRequestTester
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
        carrier_validator: PromotionRequestTester
        
    Provides:
        -   run(self, request: PromotionRequest) -> PromotionApprovalReport
        
    Super Class:
        Permitter
    """
    _bootstrapper: PromotionRequestTester
    
    def __init__(
            self, bootstrapper: PromotionRequestTester | None = PromotionRequest(),
    ):
        """
        Args:
            bootstrapper: PromotionRequestTester
        """
        self._bootstrapper = bootstrapper
    
    
    @LoggingLevelRouter.monitor
    def run(self, request: PromotionRequest) -> PromotionApprovalReport:
        """
        Evaluate a pawn promotion request.
        
        Action:
            1.  Deny the request if it cannot be bootstrapped. Otherwise, approve
                it.
        Args:
            request: PromotionRequest
        Returns:
            PromotionApprovalReport
        Raises:
            PromotionPermitterException
        """
        method = f"{self.__class__.__name__}.run"
        
        # Handle the case that, the request cannot get bootstrapped.
        bootstrap = self._bootstrapper.execute(request)
        if bootstrap.is_failure:
            PromotionApprovalReport.deny(
                PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Send the work product. ---#
        return PromotionApprovalReport.approve(
            pawn=request.candidate,
            rank_level=request.rank_level,
        )
