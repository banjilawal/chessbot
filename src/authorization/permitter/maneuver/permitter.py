# src/authorization/permitter/maneuver/authorizer.py

"""
Module: authorization.permitter.maneuver.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverDecision
from authorization import Permitter, ReadyTokenChecker
from bootstrap import ManeuverAuthorizationLoader
from exchange import ManeuverPermissionRequest
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

    Provides:
        -   def execute(candidate: Any) -> ManeuverDecision

    Super Class:
        Permitter
    """
    
    def __init__(
            self,
            loader: Optional[ManeuverAuthorizationLoader] | None = None,
            ready_token_checker: Optional[ReadyTokenChecker] | None = None,
    ):
        """
        Args:
            loader: Optional[ManeuverAuthorizationLoader]
        """
        super().__init__(loader=loader or ManeuverAuthorizationLoader())
    
    @property
    def loader(self) -> ManeuverAuthorizationLoader:
        return cast(ManeuverAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverPermissionRequest) -> ManeuverDecision:
        """
        Checks if a ManeuverPermissionRequest can be granted.
        
        Action:
            1.  Send an exception in Decision if any authoriation delegated denies
                the request.
            2.  Otherwise, send a maneuver approval.
        Args:
            request: ManeuverPermissionRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverAuthorizerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
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
        token = applicant.token
        path = applicant.path
        
        # Handle the case that the case that the token is not at the path's origin.
        if
        approved_request = decision.request
        decision = self.role_permitter.execute(approved_request)
        if decision.request_is_denied:
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
        if decision.request_is_denied:
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
        approval = ManeuverPermissionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            authorization_applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)


# src/authorization/permitter/crud/insertion/push/account/permitter.py

"""
Module: authorization.permitter.crud.insertion.push.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ManeuverDecision
from authorization import PushPermitter
from bootstrap import ManeuverAuthorizationLoader
from err import ChessException
from exchange import ManeuverPermissionRequest, ManeuverRequest
from sensor import AccountCollisionSensor
from util import LoggingLevelRouter


class ManeuverPermitter(PushPermitter[ManeuverPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an ManeuverPermissionRequest.

    Attributes:
        loader: PushAuthorizationLoader
        collision_sensor: AccountCollisionSensor

    Provides:
        -   def execute(request: ManeuverPermissionRequest) -> ManeuverDecision

    Super Class:
        PushPermitter
    """
    
    def __init__(
            self,
            collision_sensor: Optional[AccountCollisionSensor] | None = None,
            loader: Optional[ManeuverAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PushAuthorizationLoader]
        """
        super().__init__(
            loader=loader or ManeuverAuthorizationLoader(),
            collision_sensor=collision_sensor or AccountCollisionSensor(),
        )
    
    @property
    def loader(self) -> ManeuverAuthorizationLoader:
        return cast(ManeuverAuthorizationLoader, super().loader)
    
    @property
    def collision_sensor(self) -> AccountCollisionSensor:
        return cast(AccountCollisionSensor, super().collision_sensor)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ManeuverDecision:
        """
        Grant permission for a stack push.

        Action:
            1.  Send an exception chain in the InsertionDecision if the request cannot be
                loaded.
            2.  If the item already exists in the collection, return a do_nothing decision.
            3.  Otherwise, send an approval decision.
        Args:
            candidate: Any
        Returns:
           ManeuverDecision
        Raises:
            ManeuverPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        

        
        # Handle the case that the item violates a uniqueness constraint.
        report = self.collision_sensor.execute(
            attractor=item,
            collection=collection,
        )
        if report.collision_exists:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = ManeuverRequest(
            id=applicant_id,
            item=item,
            collection=collection,
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

