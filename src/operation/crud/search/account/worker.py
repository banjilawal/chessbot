# src/operation/crud/search/account/worker.py

"""
Module: operation.crud.search.account.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import SearchResult
from authorization import AccountSearchPermitter
from collection import AccountStack
from domain import Account, AccountType, HumanAccount, MachineAccount
from err import AccountSearcherException
from exchange import AccountSearchPermissionRequest, AccountSearchRequest
from operation import Searcher
from production.endpoint.validation.context.model.account import firstname
from util import IdFactory, LoggingLevelRouter


class AccountSearcher(Searcher[AccountSearchRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an SearchRequest

    Attributes:
        permitter: SearchPermissionPermitter[T]

    Provides:
        -   def execute(self, request: T) -> SearchResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, permitter: Optional[AccountSearchPermitter] | None = None,):
        """
        Args:
            permitter: SearchPermissionPermitter[T]
        """
        super().__init__(permitter=permitter or AccountSearchPermitter())
    
    @property
    def permitter(self) -> AccountSearchPermitter:
        return cast(AccountSearchPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountSearchRequest) -> SearchResult:
        """
        Args:
            request: AccountSearchRequest
        Result:
            SearchResult
        Raises:
            AccountSearcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.permitter.execute(
            request=AccountSearchPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="AccountSearchPermissionRequest")
            )
        )
        if decision.request_is_denied:
            return SearchResult.failure(
                AccountSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSearcherException.MSG,
                    err_code=AccountSearcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = cast(AccountSearchRequest, decision.approval)
        context = approved_request.context
        collection = approved_request.collection
        
        firstname = context.firstname
        
        if context.id is not None:
            return self._find_by_id(id=context.id, collection=collection)
        if firstname is not None:
            return self._find_by_firstname(firstname=firstname, collection=collection)
        if context.lastname is not None:
            return self._find_by_lastname(lastname=context.lastname, collection=collection)
        if context.email is not None:
            return self._find_by_email(email=context.email, collection=collection)
        if context.machine_name is not None:
            return self._find_by_machine_name(machine_name=context.machine_name, collection=collection)
        if context.account_type is not None:
            return self._find_by_account_type(account_type=context.account_type, collection=collection)
          
    def _find_by_id(self, id, collection: AccountStack) -> SearchResult[Account]:
        for item in collection.iterator:
            if item.id == id:
                return SearchResult.success([item])
        return SearchResult.empty()
    
    def _find_by_firstname(self, firstname: str, collection: AccountStack) -> SearchResult[Account]:
        matches: List[Account] = []
        for account in self._humans(collection):
            if account.firstname.upper() == firstname.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)
    
    def _find_by_lastname(self, lastname: str, collection: AccountStack) -> SearchResult[Account]:
        matches: List[Account] = []
        for account in self._humans(collection):
            if account.lastname.upper() == lastname.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)
    
    def _find_by_email(self, email: str, collection: AccountStack) -> SearchResult[Account]:
        matches: List[Account] = []
        for account in self._humans(collection):
            if account.email.upper() == email.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)
    
    def _find_by_machine_name(self, machine_name: str, collection: AccountStack) -> SearchResult[Account]:
        matches: List[Account] = []
        for account in self._machines(collection):
            if account.name.upper() == machine_name.upper():
                matches.append(account)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)
    
    def _find_by_type(self, account_type: AccountType, collection) -> SearchResult[Account]:
        matches: List[Account] = []
        if account_type == AccountType.HUMAN_ACCOUNT:
            matches = self._humans(collection)
        else:
            matches = self._machines(collection)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(matches)
    
    
    def _humans(self, collection: AccountStack) -> List[HumanAccount]:
        matches: List[HumanAccount] = []
        for item in collection.iterator:
            if isinstance(item, HumanAccount):
                matches.append(item)
        return matches
    
    def _machines(self, collection: AccountStack) -> List[MachineAccount]:
        matches: List[MachineAccount] = []
        for item in collection.iterator:
            if isinstance(item, MachineAccount):
                matches.append(item)
        return matches
        