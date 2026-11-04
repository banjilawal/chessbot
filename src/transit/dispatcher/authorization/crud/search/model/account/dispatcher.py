# src/transit/dispatcher/authorization/crud/search/model/account/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.search.model.account.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountSearchDecision, SearchDecision
from authorization import AccountSearchPermitter
from exchange import AccountSearchPermissionRequest, AccountSearchRequest
from transit import ModelSearchPermissionDispatcher
from util import LoggingLevelRouter


class AccountSearchPermissionDispatcher(
    ModelSearchPermissionDispatcher[AccountSearchPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards an AccountSearchPermitter then send the results
            back to clients.

    Attributes:
        permitter: AccountSearchPermitter

    Provides:
        -   def  execute(candidate: Any) -> SearchDecision

    Super Class:
        ModelSearchPermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[AccountSearchPermitter] | None = None):
        """
        Args:
             permitter: Optional[AccountSearchPermitter]
        """
        super().__init__(permitter=permitter or AccountSearchPermitter())
        
    @property
    def permitter(self) -> AccountSearchPermitter:
        return cast(AccountSearchPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountSearchDecision:
        """
        Make a decision about an AccountSearchRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the AccountSearchRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            SearchDecision
        Raises:
            AccountSearchPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AccountSearchDecision.denial(
                exception=AccountSearchPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSearchPermissionDispatcherException.MSG,
                    err_code=AccountSearchPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(AccountSearchPermissionRequest, decision.permission_request)
        transaction_request = cast(AccountSearchRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return AccountSearchDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )