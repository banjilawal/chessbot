# src/transit/dispatcher/crud/trim/vector/dispatcher.py

"""
Module: transit.dispatcher.crud.trim.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TrimResult
from collection import VectorChain
from err import VectorChainTrimmerDispatcherException
from operation import VectorChainTrimmer
from request import VectorChainTrimRequest
from transit import ChainTrimDispatcher

from util import LoggingLevelRouter


class VectorChainTrimDispatcher(ChainTrimDispatcher[VectorChainTrimRequest]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: VectorChainTrimmer
        
    Provides:

    Super Class:
        ChainTrimDispatcher
    """
    
    def __init__(self, worker: Optional[VectorChainTrimmer] | None = None):
        """
        Args:
            worker: Optional[VectorChainTrimmer]
        """
        super().__init__(worker=worker or VectorChainTrimmer())
        
    @property
    def worker(self) -> VectorChainTrimmer:
        return cast(VectorChainTrimmer, super().worker)
        

    @LoggingLevelRouter.monitor
    def execute(self, request: VectorChainTrimRequest) -> TrimResult:
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
            return TrimResult.failure(
                VectorChainTrimmerDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainTrimmerDispatcherException.MSG,
                    err_code=VectorChainTrimmerDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        chain = cast(VectorChain, result.payload)
        return TrimResult.success(chain)
