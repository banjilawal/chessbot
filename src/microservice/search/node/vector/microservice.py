# src/microservice/search/node/vector/microservice.py

"""
Module: microservice.search.node.vector.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import SearchResult
from domain import VectorNode
from err import VectorNodeSearchMicroserviceException
from microservice import SearchMicroservice
from request import VectorNodeSearchRequest
from transit import VectorNodeSearchDispatcher
from util import LoggingLevelRouter


class VectorNodeSearchMicroservice(SearchMicroservice[VectorNodeSearchRequest]):
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
        dispatcher: Optional[VectorNodeSearchDispatcher]

    Provides:

    Super Class:
        SearchMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[VectorNodeSearchDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorNodeSearchDispatcher]
        """
        super().__init__(dispatcher=dispatcher or VectorNodeSearchDispatcher())
        
    @property
    def dispatcher(self) -> VectorNodeSearchDispatcher:
        return cast(VectorNodeSearchDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorNodeSearchRequest) -> SearchResult[List[VectorNode]]:
        """
        Handles VectorNodeSearchRequests.

        Action:
            1.  Send an exception chain in the SearchRequest if the request is
                not fulfilled.
            2.  Otherwise, send the VectorNode in the success result.
        Args:
            request: VectorNodeSearchRequest
        Result:
            SearchResult[VectorNode]
        Raises:
            VectorNodeSearchMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            SearchResult.failure(
                VectorNodeSearchMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchMicroserviceException.MSG,
                    err_code=VectorNodeSearchMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # Handle the case that no matches were found.
        if result.is_empty:
            return SearchResult.empty()
        # --- Forward the work product to the client. ---#
        matches = cast(List[VectorNode], result.payload)
        return SearchResult.success(matches)