# src/authorization/permitter/crud/insertion/push/account/permitter.py

"""
Module: authorization.permitter.crud.insertion.push.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountPushDecision
from authorization import PushPermitter
from bootstrap import AccountPushAuthorizationLoader
from exchange import AccountPushPermissionRequest, AccountPushRequest
from sensor import AccountCollisionSensor
from util import LoggingLevelRouter


class AccountPushPermitter(PushPermitter[AccountPushPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an AccountPushPermissionRequest.

    Attributes:
        loader: PushAuthorizationLoader
        collision_sensor: AccountCollisionSensor
        
    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> AccountPushDecision

    Super Class:
        PushPermitter
    """

    def __init__(
            self,
            collision_sensor: Optional[AccountCollisionSensor] | None = None,
            loader: Optional[AccountPushAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PushAuthorizationLoader]
        """
        super().__init__(
            loader=loader or AccountPushAuthorizationLoader(),
            collision_sensor=collision_sensor or AccountCollisionSensor(),
        )
    
    @property
    def loader(self) -> AccountPushAuthorizationLoader:
        return cast(AccountPushAuthorizationLoader, super().loader)
    
    @property
    def collision_sensor(self) -> AccountCollisionSensor:
        return cast(AccountCollisionSensor, super().collision_sensor)

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountPushDecision:
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
           AccountPushDecision
        Raises:
            AccountPushPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermitterException.MSG,
                    err_code=AccountPushPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_form = cast(AccountPushPermissionRequest, bootstrap.permission_request)
        applicant = cast(AccountPushRequest, bootstrap.transaction_request)
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        item = applicant.item
        collection = applicant.collection
        
        # Handle the case that the item violates a uniqueness constraint.
        report = self.collision_sensor.execute(
            attractor=item,
            collection=collection,
        )
        if report.collision_exists:
            # Send the exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermitterException.MSG,
                    err_code=AccountPushPermitterException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = AccountPushRequest(
            id=applicant_id,
            item=item,
            collection=collection,
        )
        permission_request = AccountPushPermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
        )
        
        # --- Forward the approval. ---#
        return AccountPushDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        
        
        
        