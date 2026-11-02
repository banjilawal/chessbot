# src/authorization/permitter/crud/search/search.account//permitter.py

"""
Module: authorization.permitter.crud.search.search.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountSearchDecision, SearchDecision
from authorization import SearchPermitter
from bootstrap import AccountSearchAuthorizationLoader
from err import ChessException
from exchange import AccountSearchPermissionRequest
from util import LoggingLevelRouter


class AccountSearchPermitter(SearchPermitter[AccountSearchPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Forward a searchDecision about an AccountSearchPermissionRequest to an
            AccountSearchPermitter.

    Attributes:
        loader: SearchAuthorizationLoader
        
    Provides:
        -   def execute(request: AccountSearchPermissionRequest) -> SearchDecision

    Super Class:
        SearchPermitter
    """

    
    def __init__(
            self, loader: Optional[AccountSearchAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[AccountSearchAuthorizationLoader]
        """
        super().__init__(loader=loader or AccountSearchAuthorizationLoader())
        
    @property
    def loader(self) -> AccountSearchAuthorizationLoader:
        return cast(AccountSearchAuthorizationLoader, super().loader)

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountSearchDecision:
        """
        Grant permission for a stack search.
        
        Action:
            1.  Send an exception chain in the SearchDecision if any of the following occur
                    -   The loader cannot bootstrap the process.
                    -   The permission_request or transaction_request are null.
            2.  Otherwise, send an approval searchDecision.
        Args:
            candidate: Any
        Returns:
           SearchDecision
        Raises:
            AccountSearchPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return AccountSearchDecision.denial(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = bootstrap.permission_request
        transaction_request = bootstrap.transaction_request
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return AccountSearchDecision.denial(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=AccountSearchPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return AccountSearchDecision.denial(
                exception=ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=AccountSearchRequestNullException(),
                )
            )
        # --- Prepare and forward the transaction approval. ---#
        return AccountSearchDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )

        