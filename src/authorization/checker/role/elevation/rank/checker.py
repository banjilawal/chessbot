# src/authorization/checker/role/elevatable/checker.py

"""
Module: authorization.checker.role.elevatable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionRoleChecker
from domain import Elevatable, Rank
from err import AuthorizationException
from exchange import PromotionRequest, RankValidationRequest, RankValidationService
from transit import RankCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionRankChecker(PromotionRoleChecker[Elevatable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Elevatable meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: RankValidationService

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionRoleChecker
    """
    
    def __init__(
            self,
            validation_service: Optional[RankValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[RankValidationService]
        """
        super().__init__(
            validation_service=validation_service or RankValidationService()
        )
        
    @property
    def validation_service(self) -> RankValidationService:
        return cast(RankValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a Elevatable meets the requirements to perform an activity.

        Args:
            request: AuthorizationRequest
        Returns:
           Decision
        Raises:
            AuthorizationException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate gets flagged.
        validation = self.validation_service.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=request.activity_to_rank),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
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
        rank = cast(Rank, validation.payload)
        if not isinstance(rank, Elevatable):
            # Send the exception chain on failure.
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
        activity = cast(Elevatable, rank)
        approval = PromotionRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the work product. ---#
        return PromotionDecision.grant(approval)
 