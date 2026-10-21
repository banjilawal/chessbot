# src/authorization/applicant/token/promotion/approver.py

"""
Module: authorization.applicant.token.promotion.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionAuthorizationLoader, TokenApprover
from domain import PawnToken, Token
from err import DisabledPawnPromotionException, TokenPromotionApproverException
from exchange import PromotionRequest, TokenValidationService
from logic.promotion.promotion.exception import DoublePromotionException
from util import LoggingLevelRouter


class TokenPromotionApprover(TokenApprover[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be promoted.

    Attributes:
        validation_service: TokenValidationService
        loader: Optional[PromotionAuthorizationLoader]

    Provides:
        -   def request: PromotionRequest) -> PromotionDecision

    Super Class:
        TokenApprover
    """
    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            validation_service: Optional[TokenValidationService] | None = None
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
    

    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a Token meets the requirements to perform an activity.
        
        Action:
            1.  Return Promotion denial if any of the following occur:
                    -   The request is either null or the wrong type.
                    -   The applicant is not a PawnToken.
                    -   The applicant is not ready.
                    -   The applicant has already been promoted.
                    -   The actor is not on its enemy's rank row.
            2.  Otherwise, send a promotion approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            TokenPromotionApproverException
        """
        method = f"{self.__class__.__name__}"
        
        load = self.load_request(request=request, loader=self.loader)
        if load.is_denied:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=load.exception
                ),
            )
        operation = cast(PromotionRequest, load.request)
        validation_check = self.run_validation_check(operation.applicant)
        if validation_check.is_failure:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=validation_check.exception
                ),
            )
        token = cast(Token, validation_check.payload)
        if not isinstance(token, PawnToken):
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=validation_check.exception
                ),
            )
        readiness = self.run_applicant_readiness_check(operation)
        if readiness.is_denied:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=readiness.exception
                ),
            )
        if operation.applicant.is_promoted:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=DoublePromotionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DoublePromotionException.MSG,
                        err_code=DoublePromotionException.ERR_CODE,
                    )
                ),
            )
        promotion_row = operation.applicant.team.enemy_rank_row
        position = operation.applicant.footstep.position
        
        if position is None or position.row != promotion_row:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=DoublePromotionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DoublePromotionException.MSG,
                        err_code=DoublePromotionException.ERR_CODE,
                    )
                ),
            )
        id = operation.id
        activity = operation.activity
        applicant = cast(PawnToken, operation.applicant)
        
        approval = PromotionRequest(id=id, activity=activity, applicant=applicant)
        return PromotionDecision.grant(approval)
        
        
        
    @LoggingLevelRouter.monitor
    def load_request(
            self,
            request: PromotionRequest,
            loader: PromotionAuthorizationLoader,
    ) -> PromotionDecision:
        """
        Checks if a Token is ready for its promotion

        Action:
            1.  Deny the promotion if the request cannot be loaded into the Approver.
            2.  Otherwise, forward an approval.
        Args:
            request: PromotionRequest
            loader: PromotionAuthorizationLoader
        Returns:
           PromotionDecision
        Raises:
            TokenPromotionApproverException
        """
        method = f"{self.__class__.__name__}.load_request"
        
        # Handle the case that the loader cannot bootstrap the request.
        loading = self.loader.execute(request=request)
        if loading.is_denied:
            # Send an exception chain on denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=loading.exception
                ),
            )
        # --- Forward the work product. ---#
        approval = cast(PromotionRequest, loading.request)
        return PromotionDecision.grant(approval)
    
    @LoggingLevelRouter.monitor
    def run_applicant_readiness_check(self, request: PromotionRequest) -> PromotionDecision:
        """
        Check if a PawnToken.readiness == ComabtantReadiness.Ready

        Action:
            1.  Deny the promotion if the request PawnToken is disabled.
            2.  Otherwise, forward an approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            TokenPromotionApproverException
        """
        method = f"{self.__class__.__name__}.run_readiness_check"
        
        if request.applicant.is_not_ready:
            # Send an exception chain on denial.
            return PromotionDecision.denial(
                request=request,
                exception=DisabledPawnPromotionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPromotionApproverException.MSG,
                        err_code=TokenPromotionApproverException.ERR_CODE,
                )
            )
        # --- Forward the work product. ---#
        return PromotionDecision.grant(request)
        