# src/operation/crud/trim/vector/worker.py

"""
Module: operation.crud.trim.vector.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import TrimResult
from domain import VectorNode
from operation import ChainTrimmer, VectorNodeSearcher
from request import VectorNodeSearchRequest
from transit import VectorNodeSearchPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class VectorChainTrimmer(ChainTrimmer[VectorChaimTrimRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an VectorNodeSearchRequest

    Attributes:
        permitter: VectorNodeSearchPermissionDispatcher

    Provides:
        -   def execute(request: VectorNodeSearchRequest) -> SearchResult[List[Vector]]

    Super Class:
        ModelSearcher
    """
    _searcher: VectorNodeSearcher
    
    def __init__(
            self,
            searcher: Optional[VectorNodeSearcher] | None = None,
            permitter: Optional[VectorNodeSearchPermissionDispatcher] | None = None,
    ):
        """
        Args:
            searcher: Optional[VectorNodeSearcher]
            permitter: Optional[VectorNodeSearchPermissionDispatcher]
        """
        super().__init__(
            searcher=searcher or VectorNodeSearcher(),
            permitter=permitter or VectorNodeSearchPermissionDispatcher(),
        )
        
    @property
    def searcher(self) -> VectorNodeSearcher:
        return cast(VectorNodeSearcher, super().searcher)
    
    @property
    def permitter(self) -> VectorNodeSearchPermissionDispatcher:
        return cast(VectorNodeSearchPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorChaimTrimRequest) -> TrimResult:
        """
        Search an VectorChain for context matches.
        
        Action:
            1.  Send an exception chain in the SearchResult if any of the following
                occur.
                    -   The request is denied.
                    -   An approved request lacks either the VectorNodeSearchRequest or
                        its PermissionRequest.
            2.  If the search result is empy send a SearchResult.empty otherwise, send
                the success result.
        Args:
            request: VectorNodeSearchRequest
        Result:
            SearchResult[List[Vector]]
        Raises:
            VectorChainTrimmerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is denied.
        decision = self.permitter.execute(
            candidate=VectorNodeSearchPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="VectorNodeSearchPermissionRequest")
            )
        )
        if decision.request_is_denied:
            # Send an exception chain in the result.
            return SearchResult.failure(
                VectorChainTrimmerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainTrimmerException.MSG,
                    err_code=VectorChainTrimmerException.ERR_CODE,
                    ex=decision.exception,
                )
            )

        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(VectorNodeSearchRequest, decision.transaction_request)
        # --- Extract the transaction participants. ---#
        context = transaction_request.context
        collection = transaction_request.collection

        # --- Perform transaction and state management work. ---#
        search = self.searcher.execute(
            request=VectorNodeSearchRequest(
                context=context,
                collection=collection,
                id=IdFactory.next_id(class_name="Request"),
            )
        )
        if search.is_failure:
            return TrimResult.failure(
                VectorChainTrimmerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainTrimmerException.MSG,
                    err_code=VectorChainTrimmerException.ERR_CODE,
                    ex=search.exception,
                )
            )
        if search.is_empty:
            return TrimResult.nothing_to_trim()
        matches = cast(List[VectorNode], search.payload)
        node = matches[0]
        node.next = collection.tail
        collection.tail.previous = node
        
        counter = 0
        cursor = collection.iterator
        while cursor.has_next:
            counter = counter + 1
            cursor = cursor.next
        collection.size = counter
        # --- Forward the work product to the caller. ---#
        return TrimResult.success(collection)


        