# src/authorization/permitter/token/promotion/permitter.py

"""
Module: authorization.permitter.token.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from err import PromotionPermitterException
from authorization.permitter.token import OperationPermitter
from report import PromotionRequestDecision
from request.microservice.token.promotion import PromotionRequest
from authorization.adjudicator import PromotionRequestAdjudicator
from util import LoggingLevelRouter


class PromotionPermitter(OperationPermitter):
    """
    Role:
        -   Request Analyzer
        -   Rights Granter
        -   Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if promotion request can be granted.
        
    Attributes:
        carrier_validator: PromotionRequestAdjudicator
        
    Provides:
        -   run(self, request: PromotionRequest) -> PromotionApprovalReport
        
    Super Class:
        Permitter
    """
    _bootstrapper: PromotionRequestAdjudicator
    
    def __init__(
            self, bootstrapper: PromotionRequestAdjudicator | None = PromotionRequest(),
    ):
        """
        Args:
            bootstrapper: PromotionRequestAdjudicator
        """
        self._bootstrapper = bootstrapper
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionRequestDecision:
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
            PromotionRequestDecision.deny(
                PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Send the work product. ---#
        return PromotionRequestDecision.approve(
            pawn=request.candidate,
            rank_level=request.rank_level,
        )
