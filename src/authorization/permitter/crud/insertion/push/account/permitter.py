# src/authorization/permitter/crud/insertion/push.account//permitter.py

"""
Module: authorization.permitter.crud.insertion.push.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionDecision
from authorization import PushPermitter
from repo.collection import AccountStack
from domain import Account
from err import ChessException
from exchange import AccountPushPermissionRequest, AccountPushRequest
from util import LoggingLevelRouter


class AccountPushPermitter(PushPermitter[AccountPushPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Forward a decision about an AccountPushPermissionRequest to an 
            AccountPushPermitter.

    Attributes:
        loader: PushAuthorizationLoader
        
    Provides:
        -   def execute(request: AccountPushPermissionRequest) -> InsertionDecision

    Super Class:
        PushPermitter
    """

    
    def __init__(
            self, loader: Optional[AccountCrudAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PushAuthorizationLoader]
        """
        super().__init__(loader=loader or AccountCrudAuthorizationLoader())
    
    @property
    def loader(self) -> AccountCrudAuthorizationLoader:
        return cast(AccountCrudAuthorizationLoader, super().loader)

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushPermissionRequest) -> InsertionDecision:
        """
        Grant permission for a stack push.
        
        Action:
            1.  Send an exception chain in the InsertionDecision if the request cannot be
                loaded.
            2.  If the item already exists in the collection, return a do_nothing decision.
            3.  Otherwise, send an approval decision.
        Args:
            request: AccountPushPermissionRequest
        Returns:
           InsertionDecision
        Raises:
            AccountPushPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        decision = self.loader.execute(candidate=request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return InsertionDecision.denial(
                permission_request=request,
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_request = cast(AccountPushPermissionRequest, decision.permission_request)
        transaction_request = cast(AccountPushRequest, decision.transaction_request)
        item = transaction_request.item
        collection = transaction_request.collection
        
        # Do nothing when the item is already in the collection.
        if item in collection.items:
            # Send the exception chain in the denial.
            return InsertionDecision.do_nothing(
                permission_request=permission_request,
            )
        # Handle the case there is an id collision.
        
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = AccountPushRequest(
            id=transaction_request.id,
            item=item,
            collection=collection,
        )
        # --- Forward the approval. ---#
        return InsertionDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        
        
        
        