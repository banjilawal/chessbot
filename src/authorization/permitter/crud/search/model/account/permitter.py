# src/authorization/permitter/crud/search/model/account/permitter.py

"""
Module: authorization.permitter.crud.search.model.account.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountSearchDecision
from authorization import ModelSearchPermitter
from bootstrap import AccountSearchAuthorizationLoader
from err import ChessException
from exchange import AccountSearchPermissionRequest, AccountSearchRequest
from util import LoggingLevelRouter


class AccountSearchPermitter(
    ModelSearchPermitter[AccountSearchPermissionRequest]
):
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
        permission_form = cast(AccountSearchPermissionRequest, bootstrap.permission_request)
        applicant = cast(AccountSearchRequest, bootstrap.transaction_request)
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        context = applicant.context
        collection = applicant.collection
        
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = AccountSearchRequest(
            id=applicant_id,
            context=context,
            collection=collection,
        )
        permission_request = AccountSearchPermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
        )
        # --- Forward the approval. ---#
        return AccountSearchDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        