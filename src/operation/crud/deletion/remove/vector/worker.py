# src/operation/crud/search/node/vector/worker.py

"""
Module: operation.crud.search.node.vector.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import DeletionResult
from domain import VectorNode
from operation import NodeRemover, VectorNodeSearcher
from request import RemoveVectorNodeRequest, VectorNodeSearchRequest
from util import IdFactory, LoggingLevelRouter


class VectorNodeRemover(NodeRemover[RemoveVectorNodeRequest]):
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
    def execute(self, request: RemoveVectorNodeRequest) -> DeletionResult[VectorNode]:
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
            VectorNodeRemoverException
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
                VectorNodeRemoverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeRemoverException.MSG,
                    err_code=VectorNodeRemoverException.ERR_CODE,
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
            return DeletionResult.failure(
                VectorNodeRemoverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeRemoverException.MSG,
                    err_code=VectorNodeRemoverException.ERR_CODE,
                    ex=search.exception,
                )
            )
        if search.is_empty:
            return DeletionResult.nothing_to_delete()
        matches = cast(List[VectorNode], search.payload)
        node = matches[0]
        previous = node.previous
        after = node.next
        previous.next = after
        after.previous = previous
        
        node.previous = None
        node.next = None
        # --- Forward the work product to the caller. ---#
        return DeletionResult.success(node)




        