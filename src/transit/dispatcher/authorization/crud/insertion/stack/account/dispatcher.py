# src/transit/dispatcher/authorization/crud/insertion/stack/account/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.stack.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionDecision
from authorization import AccountPushPermitter
from exchange import AccountPushPermissionRequest, AccountPushRequest
from transit import PushPermissionDispatcher
from util import LoggingLevelRouter


class AccountPushPermissionDispatcher(
    PushPermissionDispatcher[AccountPushPermissionRequest]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AccountBuild workflow.

    Attributes:
        authorizer: AccountPushPermitter

    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> Decision

    Super Class:
        InsertionCrudPermissionDispatcher
    """

    def __init__(
            self,
            authorizer: Optional[AccountPushPermitter] | None = None,
    ):
        """
        Args:
            authorizer: Optional[AccountPushPermitter]
        """
        super().__init__(authorizer=authorizer or AccountPushPermitter())
        
    @property
    def authorizer(self) -> AccountPushPermitter:
        return cast(AccountPushPermitter, super().authorizer)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushPermissionRequest) -> InsertionDecision:
        """
        Forward a job to a AccountPushPermitter then deliver the result.

        Action:
            1.  Send an exception chain in the CrudRequest if the crudAuthorizer cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AccountCarrier and send in
                the success result.
        Args:
            request: AccountPushPermissionRequest
        Returns:
            Decision
        Raises:
             AccountPushPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is denied.
        decision = self.authorizer.execute(request)
        if decision.request_is_denied:
            return InsertionDecision.denial(
                permission_request=request,
                exception=AccountPushPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionDispatcherException.MSG,
                    err_code=AccountPushPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        permission_request = cast(
            AccountPushPermissionRequest,
            decision.permission_request,
        )
        approval = cast(AccountPushRequest, decision.approval)
        return InsertionDecision.grant(
            approval=approval,
            permission_request=permission_request,
        )
        
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = AccountPushRequest(
            id=transaction_request.id,
            item=item,
            collection=collection,
        )
        # --- Forward the approval. ---#
        return InsertionDecision.grant(
            approval=transaction_request,
            permission_request=permission_request,
        )