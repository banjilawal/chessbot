# src/authorization/checker/valid/activity/elevatable/checker.py

"""
Module: authorization.checker.valid.activity.elevatable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from authorization import ValidActivityChecker
from domain import Bishop, Elevatable, King, Knight, Pawn, Persona, Queen, Rank, Rook
from err import ElevatableApproverException
from exchange import AuthorizationRequest, RankValidationRequest, RankValidationService
from transit import ElevatableCarrier
from util import IdFactory, LoggingLevelRouter

class ValidElevationChecker(ValidActivityChecker[Elevatable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Elevatable meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: RankValidationService

    Provides:
        -   def execute(request: AuthorizationRequest) -> Decision

    Super Class:
        ValidActivityChecker
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
    def execute(self, request: AuthorizationRequest) -> Decision:
        """
        Checks if a Elevatable meets the requirements to perform an activity.

        Args:
            request: AuthorizationRequest
        Returns:
           Decision
        Raises:
            ElevatableApproverException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate gets flagged.
        validation = self.validation_service.extract_model(
            request=RankValidationRequest(
                item=ElevatableCarrier(model=request.activity),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return Decision.denial(
                request=request,
                exception=ElevatableApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ElevatableApproverException.MSG,
                    err_code=ElevatableApproverException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        rank = cast(Rank, validation.payload)
        if not isinstance(rank, Elevatable):
            # Send the exception chain on failure.
            return Decision.denial(
                request=request,
                exception=ElevatableApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ElevatableApproverException.MSG,
                    err_code=ElevatableApproverException.ERR_CODE,
                    ex=TypeError(
                        f"Expected an Elevatable Rank got "
                        f"{type(rank).__class__.__name__} instead."
                    ),
                )
            )
        activity = cast(Elevatable, rank)
        approval = AuthorizationRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the work product. ---#
        return Decision.grant(approval)
 