# src/authorization/permitter/maneuver/permitter.py

"""
Module: authorization.permitter.maneuver.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ManeuverDecision
from authorization import Permitter, ReadyTokenChecker
from authorization.checker.maneuver.destination import ManeuverTokenDestinationChecker
from authorization.checker.maneuver.origin import ManeuverTokenOriginChecker
from bootstrap import ManeuverAuthorizationLoader
from exchange import ManeuverPermissionRequest, ManeuverRequest
from util import LoggingLevelRouter


class ManeuverPermitter(Permitter[ManeuverPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant a Token permission for a Maneuver.

    Attributes:
        loader: ManeuverAuthorizationLoader
        ready_token_checker: ReadyTokenChecker
        origin_checker: ManeuverTokenOriginChecker
        destination_checker: ManeuverTokenDestinationChecker

    Provides:
        -   def execute(candidate: Any) -> ManeuverDecision

    Super Class:
        Permitter
    """
    
    _ready_token_checker: ReadyTokenChecker
    _origin_checker: ManeuverTokenOriginChecker
    _destination_checker: ManeuverTokenDestinationChecker
    
    def __init__(
            self,
            loader: Optional[ManeuverAuthorizationLoader] | None = None,
            ready_token_checker: Optional[ReadyTokenChecker] | None = None,
            origin_checker: Optional[ManeuverTokenOriginChecker] | None = None,
            destination_checker: Optional[ManeuverTokenDestinationChecker] | None = None,
    ):
        """
        Args:
            loader: Optional[ManeuverAuthorizationLoader]
            ready_token_checker: Optional[ReadyTokenChecker]
            origin_checker: Optional[ManeuverTokenOriginChecker]
            destination_checker: Optional[ManeuverTokenDestinationChecker]
        """
        super().__init__(loader=loader or ManeuverAuthorizationLoader())
        self._ready_token_checker = ready_token_checker or ReadyTokenChecker()
        self._origin_checker = origin_checker or ManeuverTokenOriginChecker()
        self._destination_checker = destination_checker or ManeuverTokenDestinationChecker()
    
    @property
    def loader(self) -> ManeuverAuthorizationLoader:
        return cast(ManeuverAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ManeuverDecision:
        """
        Checks if a ManeuverPermissionRequest can be granted.
        
        Action:
            1.  Send an exception in the denial if any of the following occur.
                    -   The loader cannot bootstrap the process.
                    -   The token is not actionable.
                    -   The token is not at the origin to start the maneuver.
                    -   The token is already at the destination.
                    -   The destination is occupied by a friend.
            2.  Otherwise, send a maneuver approval.
        Args:
            candidate: Any
        Returns:
           ManeuverDecision
        Raises:
            ManeuverPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_form = cast(ManeuverPermissionRequest, bootstrap.permission_request)
        applicant = cast(ManeuverRequest, bootstrap.transaction_request)
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        token = applicant.traveler
        path = applicant.path
        
        # Handle the case that the token is disabled.
        readiness = self._ready_token_checker.execute(
            candidate=token,
            permission_request=permission_form,
            transaction_request=applicant,
        )
        if readiness.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    ex=readiness.exception,
                ),
            )
        # Handle the case that the token<->origin does not satisfy transaction requirements.
        decision = self._origin_checker.execute(
            role=path,
            principal=token,
            transaction_request=applicant,
            permission_request=permission_form,
        )
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # Handle the case that the token<->destination does not satisfy transaction requirements.
        decision = self._destination_checker.execute(
            role=path,
            principal=token,
            transaction_request=applicant,
            permission_request=permission_form,
        )
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermitterException.MSG,
                    err_code=ManeuverPermitterException.ERR_CODE,
                    ex=decision.exception,
                ),
            )
        # --- Prepare an approval of the transaction. ---#
        transaction_request = ManeuverRequest(
            id=applicant_id,
            traveler=token,
            path=path,
        )
        permission_request = ManeuverPermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
            
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )

