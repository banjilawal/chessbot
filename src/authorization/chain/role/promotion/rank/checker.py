# src/authorization/chain/role/promotion/rank/checker.py

"""
Module: authorization.chain.role.promotion.rank.checker_
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionDecision
from authorization import PromotionRoleChecker
from domain import Elevateable, Rank
from err import AuthorizationException
from exchange import PromotionRequest, RankValidationRequest
from transit import RankCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionRankChecker(PromotionRoleChecker[Elevateable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Grant permission to a Rank for a PromotionRequest.

    Attributes:
        validation_service : RankValidationService

    Provides:
        -   execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionRoleChecker
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Decide if a Promotion can be made to a Rank.

        Action:
            1.  Deny permission to the Promotion if any of the following occur
                    -   The activity is not a safe Rank.
                    -   The rank is not promotable.
            2.  Otherwise, issue a grant decision.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
          PromotionRankCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that request.activity is not a safe rank.
        validation = self.validation_service.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=request.activity_to_rank),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=AuthorizationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AuthorizationException.MSG,
                    err_code=AuthorizationException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Handle the case that the validation payload is not Elevatable.
        rank = cast(Rank, validation.payload)
        if not isinstance(rank, Elevateable):
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=AuthorizationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AuthorizationException.MSG,
                    err_code=AuthorizationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected an Elevatable Rank got "
                        f"{type(rank).__class__.__name__} instead."
                    ),
                )
            )
        # --- Prepare an approval of the activity. ---#
        activity = cast(Elevateable, rank)
        approval = PromotionRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)
 