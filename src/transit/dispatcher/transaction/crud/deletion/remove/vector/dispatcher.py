# src/transit/dispatcher/crud/deletion/remove/vector/dispatcher.py

"""
Module: transit.dispatcher.crud.deletion.remove.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import DeletionResult
from err import VectorNodeRemoverDispatcherException
from operation import VectorNodeRemover
from request import RemoveVectorNodeRequest
from transit import RemoveNodeDispatcher

from util import LoggingLevelRouter


class RemoveVectorNodeDispatcher(RemoveNodeDispatcher[RemoveVectorNodeRequest]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: VectorNodeRemover
        
    Provides:

    Super Class:
        RemoveNodeDispatcher
    """
    
    def __init__(self, worker: Optional[VectorNodeRemover] | None = None):
        """
        Args:
            worker: Optional[VectorNodeRemover]
        """
        super().__init__(worker=worker or VectorNodeRemover())
        
    @property
    def worker(self) -> VectorNodeRemover:
        return cast(VectorNodeRemover, super().worker)
        

    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveVectorNodeRequest) -> DeletionResult:
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
            return DeletionResult.failure(
                VectorNodeRemoverDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeRemoverDispatcherException.MSG,
                    err_code=VectorNodeRemoverDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return DeletionResult.success()
