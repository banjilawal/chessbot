# src/authorization/authorizer/maneuver/authorizer.py

"""
Module: authorization.authorizer.maneuver.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverDecision
from authorization import (
    Authorizer, ManeuverAuthorizationLoader, ManeuverRankPermitter, ManeuverTokenReviewer
)
from err import ManeuverAuthorizerException

from exchange import ManeuverAuthorizationRequest
from util import LoggingLevelRouter


class ManeuverAuthorizer(Authorizer[ManeuverAuthorizationRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant a Token permission for a Maneuver.

    Attributes:
        loader: ManeuverAuthorizationLoader
        role_permitter: ManeuverRankPermitter
        applicant_reviewer: ManeuverTokenReviewer

    Provides:
        -   def execute(request: ManeuverAuthorizationRequest) -> ManeuverDecision

    Super Class:
        Authorizer
    """
    
    def __init__(
            self,
            loader: Optional[ManeuverAuthorizationLoader] | None = None,
            role_permitter: Optional[ManeuverRankPermitter] | None = None,
            applicant_reviewer: Optional[ManeuverTokenReviewer] | None = None,
    ):
        """
        Args:
            loader: Optional[ManeuverAuthorizationLoader]
            role_permitter: Optional[ManeuverRankPermitter]
            applicant_reviewer: Optional[ManeuverTokenReviewer
        """
        super().__init__(
            loader=loader or ManeuverAuthorizationLoader(),
            role_permitter=role_permitter or ManeuverRankPermitter(),
            applicant_reviewer=applicant_reviewer or ManeuverTokenReviewer(),
        )
    
    @property
    def loader(self) -> ManeuverAuthorizationLoader:
        return cast(ManeuverAuthorizationLoader, super().loader)
    
    @property
    def role_reviewer(self) -> ManeuverRankPermitter:
        return cast(ManeuverRankPermitter, super().role_permitter)
    
    @property
    def applicant_reviewer(self) -> ManeuverTokenReviewer:
        return cast(ManeuverTokenReviewer, super().applicant_reviewer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverAuthorizationRequest) -> ManeuverDecision:
        """
        Checks if a ManeuverAuthorizationRequest can be granted.
        
        Action:
            1.  Send an exception in Decision if any authoriation delegated denies
                the request.
            2.  Otherwise, send a maneuver approval.
        Args:
            request: ManeuverAuthorizationRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverAuthorizerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the loader does not grant permission.
        decision = self.loader.execute(request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizerException.MSG,
                    err_code=ManeuverAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the role_permitter does not grant activity permission.
        approved_request = decision.request
        decision = self.role_permitter.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizerException.MSG,
                    err_code=ManeuverAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the applicant reviewe does not grant actor permission.
        approved_request = decision.request
        decision = self.applicant_reviewer.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizerException.MSG,
                    err_code=ManeuverAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # --- Prepare an approval from the completed chain. ---#
        approval = ManeuverAuthorizationRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)
