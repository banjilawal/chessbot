# src/authorization/loader/attack/loader.py

"""
Module: authorization.loader.attack.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import AttackDecision
from authorization import AuthorizationLoader
from err import AttackAuthorizationLoaderException, AttackPermissionRequestNullException
from exchange import AttackPermissionRequest
from util import LoggingLevelRouter


class AttackAuthorizationLoader(AuthorizationLoader[AttackPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure only not-null PermissionRequest is processed.

    Attributes:

    Provides:
        -   def execute(request: AttackPermissionRequest) -> AttackDecision

    Super Class:
        AuthorizationLoader
    """
    def __init__(self):
        """Args:"""
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, target: AttackPermissionRequest) -> AttackDecision:
        """
        Checks if the request is null or the wrong type

        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   not a AttackPermissionRequest.
            2.  Otherwise, send an approval.
        Args:
            target: AttackPermissionRequest
        Returns:
           AttackDecision
        Raises:
            AttackAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that request gets flagged.
        priming = self.priming_validator.execute(
            candidate=target,
            target_model=AttackPermissionRequest,
            null_exception=AttackPermissionRequestNullException(),
        )
        # Send an exception chain in the denial.
        if priming.is_failure:
            return AttackDecision.denial(
                request=target,
                exception=AttackAuthorizationLoaderException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=AttackAuthorizationLoaderException.MSG,
                   err_code=AttackAuthorizationLoaderException.ERR_CODE,
                   ex=priming.exception,
                )
            )
        approved_request = cast(AttackPermissionRequest, priming.payload)
        # --- Prepare an approval from the completed chain. ---#
        approval = AttackPermissionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return AttackDecision.grant(approval)