# src/microservice/search/model/account/microservice.py

"""
Module: microservice.search.model.account.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import SearchResult
from domain import Account
from err import AccountSearchMicroserviceException
from microservice import SearchMicroservice
from request import AccountSearchRequest
from transit import AccountSearchDispatcher
from util import LoggingLevelRouter


class AccountSearchMicroservice(SearchMicroservice[AccountSearchRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice
        
    About:
        Avoids casting an entity's searchers and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the search-validation security lifecycle.

    Attributes:
        dispatcher: Optional[AccountSearchDispatcher]

    Provides:
        -   def execute(request: AccountSearchRequest) -> SearchResult[List[Account]]

    Super Class:
        SearchMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[AccountSearchDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountSearchDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AccountSearchDispatcher())
        
    @property
    def dispatcher(self) -> AccountSearchDispatcher:
        return cast(AccountSearchDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountSearchRequest) -> SearchResult[List[Account]]:
        """
        Handles AccountSearchRequests.

        Action:
            1.  Send an exception chain in the SearchRequest if the request is
                not fulfilled.
            2.  Otherwise, send the Account in the success result.
        Args:
            request: AccountSearchRequest
        Result:
            SearchResult[Account]
        Raises:
            AccountSearchMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            SearchResult.failure(
                AccountSearchMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSearchMicroserviceException.MSG,
                    err_code=AccountSearchMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # Handle the case that no hits was not found.
        if result.is_empty:
            return SearchResult.empty()
        # --- Forward the work product to the client. ---#
        matches = cast(List[Account], result.payload)
        return SearchResult.success(matches)