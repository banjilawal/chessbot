# src/authorization/authorizer/attack/authorizer.py

"""
Module: authorization.authorizer.attack.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackDecision
from authorization import (
    Authorizer, AttackAuthorizationLoader, AttackRankPermitter, AttackTokenReviewer
)
from err import AttackAuthorizerException

from exchange import AttackRequest
from util import LoggingLevelRouter


class AttackAuthorizer(Authorizer[AttackRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant a Token permission for a Attack.

    Attributes:
        loader: AttackAuthorizationLoader
        role_permitter: AttackRankPermitter
        applicant_reviewer: AttackTokenReviewer

    Provides:
        -   def execute(request: AttackRequest) -> AttackDecision

    Super Class:
        Authorizer
    """
    
    def __init__(
            self,
            loader: Optional[AttackAuthorizationLoader] | None = None,
            role_permitter: Optional[AttackRankPermitter] | None = None,
            applicant_reviewer: Optional[AttackTokenReviewer] | None = None,
    ):
        """
        Args:
            loader: Optional[AttackAuthorizationLoader]
            role_permitter: Optional[AttackRankPermitter]
            applicant_reviewer: Optional[AttackTokenReviewer
        """
        super().__init__(
            loader=loader or AttackAuthorizationLoader(),
            role_permitter=role_permitter or AttackRankPermitter(),
            applicant_reviewer=applicant_reviewer or AttackTokenReviewer(),
        )
    
    @property
    def loader(self) -> AttackAuthorizationLoader:
        return cast(AttackAuthorizationLoader, super().loader)
    
    @property
    def role_reviewer(self) -> AttackRankPermitter:
        return cast(AttackRankPermitter, super().role_permitter)
    
    @property
    def applicant_reviewer(self) -> AttackTokenReviewer:
        return cast(AttackTokenReviewer, super().applicant_reviewer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        """
        Checks if a AttackRequest can be granted.
        
        Action:
            1.  Send an exception in Decision if any authoriation delegated denies
                the request.
            2.  Otherwise, send a attack approval.
        Args:
            request: AttackRequest
        Returns:
           AttackDecision
        Raises:
            AttackAuthorizerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the loader does not grant permission.
        decision = self.loader.execute(request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackAuthorizerException.MSG,
                    err_code=AttackAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the role_permitter does not grant activity permission.
        approved_request = decision.request
        decision = self.role_permitter.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackAuthorizerException.MSG,
                    err_code=AttackAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the applicant reviewe does not grant actor permission.
        approved_request = decision.request
        decision = self.applicant_reviewer.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackAuthorizerException.MSG,
                    err_code=AttackAuthorizerException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # --- Prepare an approval from the completed chain. ---#
        approval = AttackRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return AttackDecision.grant(approval)
