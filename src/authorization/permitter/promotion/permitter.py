# src/authorization/permitter/promotion/authorizer.py

"""
Module: authorization.permitter.promotion.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import Permitter
from bootstrap import PromotionAuthorizationLoader
from err import PromotionAuthorizerException

from exchange import PromotionPermissionRequest, TokenValidationService
from util import LoggingLevelRouter


class PromotionPermitter(Permitter[PromotionPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant a Token permission for a Promotion.

    Attributes:
        loader: PromotionAuthorizationLoader
        validation_service: TokenValidationService


    Provides:
        -   def execute(request: PromotionPermissionRequest) -> PromotionDecision

    Super Class:
        Permitter
    """
    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            validation_service: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            validation_service: Optional[TokenValidationService]
        """
        super().__init__(
            loader=loader or PromotionAuthorizationLoader(),
            validation_service=validation_service or TokenValidationService(),
        )
    
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    
    @property
    def validation_service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Checks if a PromotionPermissionRequest can be granted.
        
        Action:
            1.  Send an exception in Decision if any authoriation delegated denies
                the request.
            2.  Otherwise, send a promotion approval.
        Args:
            request: PromotionPermissionRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionAuthorizerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the loader does not grant permission.
        decision = self.loader.execute(request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizerException.MSG,
                    err_code=PromotionAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the role_permitter does not grant activity permission.
        approved_request = decision.request
        decision = self.role_permitter.execute(approved_request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizerException.MSG,
                    err_code=PromotionAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the applicant reviewe does not grant actor permission.
        approved_request = decision.request
        decision = self.applicant_reviewer.execute(approved_request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizerException.MSG,
                    err_code=PromotionAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # --- Prepare an approval from the completed chain. ---#
        approval = PromotionPermissionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            authorization_applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)
