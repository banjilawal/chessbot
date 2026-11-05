# src/authorization/permitter/crud/insertion/push/account/permitter.py

"""
Module: authorization.permitter.crud.insertion.push.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountPushDecision, CollisionReport
from authorization import PushPermitter
from bootstrap import AccountPushAuthorizationLoader
from collection import AccountStack
from domain import Account, AccountContext, HumanAccount, MachineAccount
from err import AccountPushPermitterException
from exchange import AccountPushPermissionRequest, AccountPushRequest
from production import AccountCollisionDetector
from util import LoggingLevelRouter


class AccountPushPermitter(PushPermitter[AccountPushPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an AccountPushPermissionRequest.

    Attributes:
        loader: PushAuthorizationLoader
        collision_detector: AccountCollisionDetector
        
    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> AccountPushDecision

    Super Class:
        PushPermitter
    """

    def __init__(
            self,
            loader: Optional[AccountPushAuthorizationLoader] | None = None,
            collision_detector: Optional[AccountCollisionDetector] | None = None,
    ):
        """
        Args:
            loader: Optional[PushAuthorizationLoader]
            collision_detector: Optional[AccountCollisionDetector]
        """
        super().__init__(
            loader=loader or AccountPushAuthorizationLoader(),
            collision_detector=collision_detector or AccountCollisionDetector(),
        )
    
    @property
    def loader(self) -> AccountPushAuthorizationLoader:
        return cast(AccountPushAuthorizationLoader, super().loader)
    
    @property
    def collision_detector(self) -> AccountCollisionDetector:
        return cast(AccountCollisionDetector, super().collision_detector)

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
        
        # Handle the case that a uniqueness constraint is violated
        report = self._uniqueness_checker(item, collection)
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
        
        
    @LoggingLevelRouter.monitor
    def _uniqueness_checker(
            self,
            item: Account,
            collection: AccountStack,
    ) -> CollisionReport:
        """Runs uniqueness checks sequentially."""
        
        # --- Run the universal check for an id. ---#
        report = self.collision_detector.execute(
            stream=collection,
            context=AccountContext(id=item.id),
        )
        # Return if a duplicate id is found.
        if report.collision_exists:
            return report
        # --- Handoff to a collider_branch for final processing. ---#
        if isinstance(item, HumanAccount):
            report = self._email_collider_branch(item, collection)
        if isinstance(item, MachineAccount):
            report = self._machine_collider_branch(item, collection)
        # Send the completed repot
        return report
    
    @LoggingLevelRouter.monitor
    def _email_collider_branch(
            self,
            account: HumanAccount,
            collection: AccountStack
    ) -> CollisionReport:
        """
        Send a denial if account.email will not be unique.
        """
        return self.collision_detector.execute(
            context=AccountContext(email=account.email),
            stream=collection,
        )
    
    @LoggingLevelRouter.monitor
    def _machine_collider_branch(
            self,
            account: MachineAccount,
            collection: AccountStack
    ) -> CollisionReport:
        """
        Send a denial if machine_account.name will not be unique.
        """
        return self.collision_detector.execute(
            context=AccountContext(machine_name=account.name),
            stream=collection,
        )
        