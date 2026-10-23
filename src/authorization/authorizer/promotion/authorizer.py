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
from authorization import Authorizer, PromotionAuthorizationLoader, PromotionRankReviewer
from authorization.reviewer.promotion import PromotionTokenReviewer
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionAuthorizer(Authorizer[PromotionRequest]):
    """
    Role:
        -   Permission Authorization
        -   Consistency and Integrity Management

    Responsibilities:
        1.  Check if a PawnToken satisfies promotion requirements.

    Attributes:
        loader: PromotionAuthorizationLoader
        rank_validation_service: RankValidationService
        applicant_reviewer: TokenValidationServic

    Provides:
        -  def process(form: PromotionAuthorizationForm) -> PromotionDecision

    Super Class:
        OperationAuthorizer
    """

    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            role_reviewer: Optional[PromotionRankReviewer] | None = None,
            applicant_reviewer: Optional[PromotionTokenReviewer] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            role_reviewer: Optional[PromotionRankReviewer]
            applicant_reviewer: Optional[PromotionTokenReviewer] 
        """
        super().__init__(
            loader=loader or PromotionAuthorizationLoader(),
            role_reviewer= role_reviewer or PromotionRankReviewer(),
            applicant_reviewer=applicant_reviewer or PromotionTokenReviewer(),
        )
    
    @property
    def role_reviewer(self) -> PromotionRankReviewer:
        return cast(PromotionRankReviewer, super().role_reviewer)
    
    @property
    def applicant_reviewer(self) -> PromotionTokenReviewer:
        return cast(PromotionTokenReviewer, super().applicant_reviewer)
    
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a PromotionRequest can be granted.
        
        Action:
            1.  Return Promotion denial if any of the following occur
                    -   The loader aborts.
                    -   The applicant_approver sends a denial.
                    -   The activity_reviewer sends a denial.
            2.  Otherwise, send a promotion approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionAuthorizerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        load_permission = self.loader.execute(request)
        if load_permission.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=PromotionAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizerException.MSG,
                    err_code=PromotionAuthorizerException.ERR_CODE,
                    ex=load_permission.exception,
                ),
            )
        job = cast(PromotionRequest, load_permission.request)
        role_approval = self.role_reviewer.execute(job)
        if role_approval.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=PromotionAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizerException.MSG,
                    err_code=PromotionAuthorizerException.ERR_CODE,
                    ex=role_approval.exception,
                ),
            )
        form = cast(PromotionRequest, role_approval.request)
        applicant_approval = self.applicant_reviewer.execute(form)
        if applicant_approval.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=PromotionAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizerException.MSG,
                    err_code=PromotionAuthorizerException.ERR_CODE,
                    ex=applicant_approval.exception,
                ),
            )
        approval = cast(PromotionRequest, applicant_approval.request)
        return PromotionDecision.grant(approval)
        