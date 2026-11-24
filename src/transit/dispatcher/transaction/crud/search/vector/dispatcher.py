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
from domain import VectorNode
from err import VectorNodeSearchDispatcherException
from operation import VectorNodeSearcher
from request import VectorNodeSearchRequest
from transit import SearchDispatcher
from util import LoggingLevelRouter


class VectorNodeSearchDispatcher(SearchDispatcher[VectorNodeSearchRequest]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute VectorNodeSearchRequests among workers then send the result to
            correct client.

    Attributes:
        worker: VectorNodeSearcher

    Provides:
        -   def  execute(request: VectorNodeSearchRequest) -> SearchResult[List[VectorNode]]

    Super Class:
        SearchDispatcher
    """
    
    def __init__(self, worker: Optional[VectorNodeSearcher] | None = None):
        """
        Args:
           worker: Optional[VectorNodeSearcher]
        """
        super().__init__(worker=worker or VectorNodeSearcher())
        
    @property
    def worker(self) -> VectorNodeSearcher:
        return cast(VectorNodeSearcher, super().worker)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorNodeSearchRequest) -> SearchResult[List[VectorNode]]:
        """
        Send VectorNodeSearchRequest to a worker.

        Action:
            1.  Send an exception chain in the SearchResult if the worker fails.
            2.  If the search result is empy send a SearchResult.empty otherwise, send
                the success result.
        Args:
            request: VectorNodeSearchRequest
        Result:
            SearchResult[List[Account]]
        Raises:
            VectorNodeSearchDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return SearchResult.failure(
                VectorNodeSearchDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchDispatcherException.MSG,
                    err_code=VectorNodeSearchDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # Handle the case that nothing was found.
        if result.is_empty:
            return SearchResult.empty()
        # --- Forward the work product to the caller. ---#
        matches = cast(List[VectorNode], result.payload)
        return SearchResult.success(matches)
