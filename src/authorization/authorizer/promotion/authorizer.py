# src/authorization/authorizer/promotion/authorizer.py

"""
Module: authorization.authorizer.promotion.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import (
    Authorizer, PromotionAuthorizationLoader, PromotionRankPermitter, PromotionTokenReviewer
)
from err import PromotionAuthorizerException

from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionAuthorizer(Authorizer[PromotionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant a Token permission for a Promotion.

    Attributes:
        loader: PromotionAuthorizationLoader
        role_permitter: PromotionRankPermitter
        applicant_reviewer: PromotionTokenReviewer

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        Authorizer
    """
    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            role_permitter: Optional[PromotionRankPermitter] | None = None,
            applicant_reviewer: Optional[PromotionTokenReviewer] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            role_permitter: Optional[PromotionRankPermitter]
            applicant_reviewer: Optional[PromotionTokenReviewer
        """
        super().__init__(
            loader=loader or PromotionAuthorizationLoader(),
            role_permitter=role_permitter or PromotionRankPermitter(),
            applicant_reviewer=applicant_reviewer or PromotionTokenReviewer(),
        )
    
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    
    @property
    def role_reviewer(self) -> PromotionRankPermitter:
        return cast(PromotionRankPermitter, super().role_permitter)
    
    @property
    def applicant_reviewer(self) -> PromotionTokenReviewer:
        return cast(PromotionTokenReviewer, super().applicant_reviewer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a PromotionRequest can be granted.
        
        Action:
            1.  Send an exception in Decision if any authoriation delegated denies
                the request.
            2.  Otherwise, send a promotion approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionAuthorizerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the loader does not grant permission.
        decision = self.loader.execute(request)
        if decision.is_denial:
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
        # Handle the case that the role_permitter does not grant activity permission.
        approved_request = decision.request
        decision = self.role_permitter.execute(approved_request)
        if decision.is_denial:
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
        if decision.is_denial:
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
        approval = PromotionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)
