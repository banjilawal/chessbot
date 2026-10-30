# src/authorization/role/promotion/rank/permitter.py

"""
Module: authorization.role.promotion.rank.permitter
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionRolePermitter
from domain import Elevatable, Rank
from err import PromotionRankPermitterException
from exchange import PromotionPermissionRequest, RankValidationRequest, RankValidationService
from transit import RankCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionRankPermitter(PromotionRolePermitter[Elevatable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Grant permission to a Rank for a PromotionPermissionRequest.

    Attributes:
        validation_service : RankValidationService

    Provides:
        -   execute(request: PromotionPermissionRequest) -> PromotionDecision

    Super Class:
        PromotionRolePermitter
    """
    
    def __init__(self, validation_service: Optional[RankValidationService] | None = None):
        super().__init__(
            validation_service=validation_service or RankValidationService()
        )
    
    @property
    def validation_service(self) -> RankValidationService:
        return cast(RankValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Decide if a Promotion can be made to a Rank.

        Action:
            1.  Deny permission to the Promotion if any of the following occur
                    -   The activity is not a safe Rank.
                    -   The rank is not promotable.
            2.  Otherwise, issue a grant decision.
        Args:
            request: PromotionPermissionRequest
        Returns:
           PromotionDecision
        Raises:
          PromotionRankPermitterException
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
                exception=PromotionRankPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRankPermitterException.MSG,
                    err_code=PromotionRankPermitterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Handle the case that the validation payload is not Elevatable.
        rank = cast(Rank, validation.payload)
        if not isinstance(rank, Elevatable):
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionRankPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRankPermitterException.MSG,
                    err_code=PromotionRankPermitterException.ERR_CODE,
                    ex=TypeError(
                        f"Expected an Elevatable Rank got "
                        f"{type(rank).__class__.__name__} instead."
                    ),
                )
            )
        # --- Prepare an approval of the activity. ---#
        activity = cast(Elevatable, rank)
        approval = PromotionPermissionRequest(
            id=request.id,
            activity=activity,
            authorization_applicant=request.applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)
 