# src/operation/crud/search/model/account/worker.py

"""
Module: operation.crud.search.model.account.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import SearchResult
from collection import AccountStack
from domain import Account, AccountType
from err import AccountSearcherException, SearchRouteCoverageException
from exchange import AccountSearchPermissionRequest, AccountSearchRequest
from operation import ModelSearcher
from transit import AccountSearchPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class AccountSearcher(ModelSearcher[AccountSearchRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an AccountSearchRequest

    Attributes:
        permitter: AccountSearchPermissionDispatcher

    Provides:
        -   def execute(request: AccountSearchRequest) -> SearchResult[List[Account]]

    Super Class:
        ModelSearcher
    """
    
    def __init__(
            self,
            permitter: Optional[AccountSearchPermissionDispatcher] | None = None,
    ):
        """
        Args:
            permitter: Optional[AccountSearchPermissionDispatcher]
        """
        super().__init__(permitter=permitter or AccountSearchPermissionDispatcher())
    
    @property
    def permitter(self) -> AccountSearchPermissionDispatcher:
        return cast(AccountSearchPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountSearchRequest) -> SearchResult[List[Account]]:
        """
        Search an AccountStack for context matches.
        
        Action:
            1.  Send an exception chain in the SearchResult if any of the following
                occur.
                    -   The request is denied.
                    -   An approved request lacks either the AccountSearchRequest or
                        its PermissionRequest.
            2.  If the search result is empy send a SearchResult.empty otherwise, send
                the success result.
        Args:
            request: AccountSearchRequest
        Result:
            SearchResult[List[Account]]
        Raises:
            AccountSearcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is denied.
        decision = self.permitter.execute(
            candidate=AccountSearchPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="AccountSearchPermissionRequest")
            )
        )
        if decision.request_is_denied:
            # Send an exception chain in the result.
            return SearchResult.failure(
                AccountSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSearcherException.MSG,
                    err_code=AccountSearcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(
            AccountSearchRequest,
            decision.transaction_request
        )
        # --- Extract the transaction participants. ---#
        context = transaction_request.context
        collection = transaction_request.collection
        
        # Ge the context attributes for routing.
        id = context.id
        firstname = context.firstname
        lastname = context.lastname
        email = context.email
        machine_name = context.machine_name
        account_type = context.account_type
        # Initialize the result.
        result = SearchResult.failure(
            SearchRouteCoverageException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
            )
        )
        # --- Perform transaction and state management work. ---#
        
        # Entry point int finding by account id.
        if id is not None:
            result = self._find_by_id(id=id, collection=collection)
        # Entry point into finding by firstname.
        if firstname is not None:
            result = self._find_by_firstname(firstname=firstname, collection=collection)
        # Entry point into finding by lastname.
        if lastname is not None:
            result = self._find_by_lastname(lastname=lastname, collection=collection)
        # Entry point into finding by email.
        if email is not None:
            result = self._find_by_email(email=email, collection=collection)
        # Entry point into finding by machine_name.
        if machine_name is not None:
            result = self._find_by_machine_name(machine_name=machine_name, collection=collection)
        # Entry point into finding by account_type.
        if account_type is not None:
           result = self._find_by_account_type(account_type=account_type, collection=collection)
        # Handle the case that attribute is not covered.
        if result.is_failure:
            return SearchResult.failure(
                AccountSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSearcherException.MSG,
                    err_code=AccountSearcherException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Perform transaction and state management work. ---#
        
        # Handle the case that no matches were found.
        if result.is_empty:
            return SearchResult.empty()
        # Otherwise send the
        matches =  cast(List[Account], result.payload)
        return SearchResult.success(matches)
          
    def _find_by_id(
            self, id, collection: AccountStack
    ) -> SearchResult[List[Account]]:
        """id_context handler"""
        matches: List[Account] = []
        for item in collection.iterator:
            if item.id == id:
                matches.append(item)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_firstname(
            self, firstname: str, collection: AccountStack) -> SearchResult:
        """firstname_context handler"""
        matches: List[Account] = []
        for account in collection.human_accounts:
            if account.firstname.upper() == firstname.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_lastname(self, lastname: str, collection: AccountStack) -> SearchResult:
        """lastname_context handler"""
        matches: List[Account] = []
        for account in collection.human_accounts:
            if account.lastname.upper() == lastname.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_email(self, email: str, collection: AccountStack) -> SearchResult:
        """email_context handler"""
        matches: List[Account] = []
        for account in collection.human_accounts:
            if account.email.upper() == email.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_machine_name(self, machine_name: str, collection: AccountStack) -> SearchResult:
        """machine_name_context handler"""
        matches: List[Account] = []
        for account in collection.machine_accounts:
            if account.name.upper() == machine_name.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_account_type(self, account_type: AccountType, collection: AccountStack) -> SearchResult[List[Account]]:
        """account_type_context handler"""
        matches: List[Account] = []
        if account_type == AccountType.HUMAN_ACCOUNT:
            matches = collection.human_accounts
        else:
            matches = collection.machine_accounts
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)

        