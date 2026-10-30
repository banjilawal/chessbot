# src/authorization/permitter/crud/search/search.account//permitter.py

"""
Module: authorization.permitter.crud.search.search.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast


from authorization import SearchPermitter
from collection import AccountStack
from domain import Account
from err import ChessException
from exchange import AccountSearchPermissionRequest, AccountSearchRequest
from util import LoggingLevelRouter


class AccountSearchPermitter(SearchPermitter[AccountSearchPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Forward a decision about an AccountSearchPermissionRequest to an 
            AccountSearchPermitter.

    Attributes:
        loader: SearchPermissionLoader
        
    Provides:
        -   def execute(request: AccountSearchPermissionRequest) -> SearchDecision

    Super Class:
        SearchPermitter
    """

    
    def __init__(
            self, loader: Optional[AccountCrudPermissionLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[SearchPermissionLoader]
        """
        super().__init__(loader=loader or AccountCrudPermissionLoader())
    
    @property
    def loader(self) -> AccountCrudPermissionLoader:
        return cast(AccountCrudPermissionLoader, super().loader)

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountSearchPermissionRequest) -> SearchDecision:
        """
        Grant permission for a stack search.
        
        Action:
            1.  Send an exception chain in the SearchDecision if the request cannot be
                loaded.
            2.  If the item already exists in the collection, return a do_nothing decision.
            3.  Otherwise, send an approval decision.
        Args:
            request: AccountSearchPermissionRequest
        Returns:
           SearchDecision
        Raises:
            AccountSearchPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request cannot be loaded.
        decision = self.loader.execute(candidate=request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return SearchDecision.denial(
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
        permission_request = cast(AccountSearchPermissionRequest, decision.permission_request)
        transaction_request = cast(AccountSearchRequest, decision.approval)
        item = cast(Account, transaction_request.item)
        collection = cast(AccountStack, transaction_request.collection)
        
        # Do nothing when the item is already in the collection.
        if item in collection.items:
            # Send the exception chain in the denial.
            return SearchDecision.do_nothing(
                permission_request=permission_request,
            )
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = AccountSearchRequest(
            id=transaction_request.id,
            item=item,
            collection=collection,
        )
        # --- Forward the approval. ---#
        return SearchDecision.grant(
            approval=transaction_request,
            permission_request=permission_request,
        )
        
        
        
        