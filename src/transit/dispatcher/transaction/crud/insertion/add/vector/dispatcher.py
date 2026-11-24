# src/transit/dispatcher/crud/insertion/add/vector/dispatcher.py

"""
Module: transit.dispatcher.crud.insertion.add.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionResult
from err import VectorNodeAdderDispatcherException
from operation import VectorNodeAdder
from request import AddVectorNodeRequest
from transit import AddNodeDispatcher

from util import LoggingLevelRouter


class AddVectorNodeDispatcher(AddNodeDispatcher[AddVectorNodeRequest]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: VectorNodeAdder
        
    Provides:

    Super Class:
        AddNodeDispatcher
    """
    
    def __init__(self, worker: Optional[VectorNodeAdder] | None = None):
        """
        Args:
            worker: Optional[VectorNodeAdder]
        """
        super().__init__(worker=worker or VectorNodeAdder())
        
    @property
    def worker(self) -> VectorNodeAdder:
        return cast(VectorNodeAdder, super().worker)
        

    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> InsertionResult:
        """
        Search an VectorStack for context matches.

        Action:
            1.  Send an exception chain in the SearchResult if any of the following
                occur.
                    -   The request is denied.
                    -   An approved request lacks either the VectorSearchRequest or
                        its PermissionRequest.
            2.  If the search result is empy send a SearchResult.empty otherwise, send
                the success result.
        Args:
            request: VectorSearchRequest
        Result:
            SearchResult[List[Vector]]
        Raises:
            VectorSearcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send the exception chain in the result.
            return InsertionResult.failure(
                VectorNodeAdderDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeAdderDispatcherException.MSG,
                    err_code=VectorNodeAdderDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
