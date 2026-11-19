# src/transit/dispatcher/crud/search/account/dispatcher.py

"""
Module: transit.dispatcher.crud.search.account.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import SearchResult
from domain import Account
from err import AccountSearchDispatcherException
from exchange import AccountSearchRequest
from operation import AccountSearcher
from transit import SearchDispatcher
from util import LoggingLevelRouter


class AccountSearchDispatcher(SearchDispatcher[AccountSearchRequest, SearchResult]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Direct jobs towards a worker then forward the results to clients.

    Attributes:
        worker: AccountSearcher

    Provides:

    Super Class:
        SearchDispatcher
    """
    
    def __init__(self, worker: Optional[AccountSearcher] | None = None):
        """
        Args:
           worker: Optional[AccountSearcher]
        """
        super().__init__(worker=worker or AccountSearcher())
        
    @property
    def worker(self) -> AccountSearcher:
        return cast(AccountSearcher, super().worker)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountSearchRequest) -> SearchResult[List[Account]]:
        """
        Send AccountSearchRequest to a worker.

        Action:
            1.  Send an exception chain in the SearchResult if the worker fails.
            2.  If the search result is empy send a SearchResult.empty otherwise, send
                the success result.
        Args:
            request: AccountSearchRequest
        Result:
            SearchResult[List[Account]]
        Raises:
            AccountSearchDIspatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        result = self.worker.execute(request)
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            return SearchResult.failure(
                AccountSearchDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSearchDispatcherException.MSG,
                    err_code=AccountSearchDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # Handle the case that nothing was found.
        if result.is_empty:
            return SearchResult.empty()
        
        matches = cast(List[Account], result.payload)
        return SearchResult.success(matches)
