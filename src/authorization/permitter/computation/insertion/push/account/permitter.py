# src/authorization/permitter/computation/insertion/push/account/permitter.py

"""
Module: authorization.permitter.computation.insertion.push.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountPushDecision
from authorization import PushPermitter
from bootstrap import AccountPushAuthorizationLoader
from err import AccountPushPermitterException
from exchange import AccountPushPermissionRequest, AccountPushRequest
from production import AccountCollisionManager
from util import LoggingLevelRouter


class AccountPushPermitter(PushPermitter[AccountPushPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an AccountPushPermissionRequest.

    Attributes:
        loader: PushAuthorizationLoader
        collision_manager: AccountCollisionManager
        
    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> AccountPushDecision

    Super Class:
        PushPermitter
    """

    def __init__(
            self,
            loader: Optional[AccountPushAuthorizationLoader] | None = None,
            collision_manager: Optional[AccountCollisionManager] | None = None,
    ):
        """
        Args:
            loader: Optional[PushAuthorizationLoader]
            collision_manager: Optional[AccountCollisionManager]
        """
        super().__init__(
            loader=loader or AccountPushAuthorizationLoader(),
            collision_manager=collision_manager or AccountCollisionManager(),
        )
    
    @property
    def loader(self) -> AccountPushAuthorizationLoader:
        return cast(AccountPushAuthorizationLoader, super().loader)
    
    @property
    def collision_manager(self) -> AccountCollisionManager:
        return cast(AccountCollisionManager, super().collision_manager)

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountPushDecision:
        """
        Grant permission for a stack push.
        
        Action:
            1.  Send an exception chain in the InsertionDecision if the request
                cannot be loaded.
            2.  Return a do_nothing when the item already exists.
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
        permission_form = cast(
            AccountPushPermissionRequest,
            bootstrap.permission_request,
        )
        applicant = cast(
            AccountPushRequest,
            bootstrap.transaction_request,
        )
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        item = applicant.item
        collection = applicant.collection
        # --- Run the uniqueness assurance checks. ---#
        
        # The simplest case that
        if item in collection.list:
            return AccountPushDecision.do_nothing()
        # Handle the case that the item will not be unique.
        report = self.collision_manager.execute(
            item=item,
            particle_stream=collection,
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
        