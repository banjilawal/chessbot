# src/operation/crud/search/account/worker.py

"""
Module: operation.crud.search.account.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations



from artifcat import SearchResult
from exchange import AccountSearchRequest
from operation import Searcher
from util import LoggingLevelRouter


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
    
    def __init__(self, permitter: AccounSearchPermittter):
        """
        Args:
            permitter: SearchPermissionPermitter[T]
        """
        super().__init__(permitter=permitter[T])
    
    
    @property
    def permitter(self) -> PushPermissionPermitter[T]:
        return cast(PushPermissionPermitter[T], super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> SearchResult:
        """
        Args:
            request: T
        Result:
            SearchResult
        Raises:
            SearcherException
        """
        pass