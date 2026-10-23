# src/authorization/loader/maneuver/loader.py

"""
Module: authorization.loader.maneuver.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ManeuverDecision
from authorization import AuthorizationLoader
from err import ManeuverAuthorizationLoaderException, ManeuverRequestNullException
from exchange import ManeuverRequest
from util import LoggingLevelRouter


class ManeuverAuthorizationLoader(AuthorizationLoader[ManeuverRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure only not-null PermissionRequest is processed.

    Attributes:

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        AuthorizationLoader
    """
    def __init__(self):
        """Args:"""
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Checks if the request is null or the wrong type

        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   not a ManeuverRequest.
            2.  Otherwise, send an approval.
        Args:
            request: ManeuverRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that request gets flagged.
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=ManeuverRequest,
            null_exception=ManeuverRequestNullException(),
        )
        # Send an exception chain in the denial.
        if priming.is_failure:
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverAuthorizationLoaderException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=ManeuverAuthorizationLoaderException.MSG,
                   err_code=ManeuverAuthorizationLoaderException.ERR_CODE,
                   ex=priming.exception,
                )
            )
        approved_request = cast(ManeuverRequest, priming.payload)
        # --- Prepare an approval from the completed chain. ---#
        approval = ManeuverRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)