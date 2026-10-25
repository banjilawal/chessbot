# src/transit/dispatcher/authorization/crud/insertion/account/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from exchange import AccountPushPermissionRequest
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
        authorizer: AccountPushAuthorizer

    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> Decision

    Super Class:
        InsertionCrudPermissionDispatcher
    """

    def __init__(
            self,
            authorizer: Optional[AccountPushAuthorizer] | None = None,
    ):
        """
        Args:
            authorizer: Optional[AccountPushAuthorizer]
        """
        super().__init__(authorizer=authorizer or AccountPushAuthorizer())
        
    @property
    def authorizer(self) -> AccountPushAuthorizer:
        return cast(AccountPushAuthorizer, super().authorizer)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushPermissionRequest ) -> Decision:
        """
        Forward a job to a AccountPushAuthorizer then deliver the result.

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
        
        # Handle the case that the candidate is not safe.
        build = self.crudAuthorizer.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return CrudRequest.failure(
                AccountCrudPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountCrudPermissionDispatcherException.MSG,
                    err_code=AccountCrudPermissionDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AccountCarrier, build.payload)
        return CrudRequest.success(carrier)