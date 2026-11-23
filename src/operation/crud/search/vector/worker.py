# src/operation/crud/search/vector/worker.py

"""
Module: operation.crud.search.vector.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import SearchResult
from collection import VectorChain
from domain import Context, Vector, VectorNode
from err import VectorSearcherException, SearchRouteCoverageException
from operation import ModelSearcher
from transit import VectorSearchPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class VectorSearcher(ModelSearcher[VectorSearchRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an VectorSearchRequest

    Attributes:
        permitter: VectorSearchPermissionDispatcher

    Provides:
        -   def execute(request: VectorSearchRequest) -> SearchResult[List[Vector]]

    Super Class:
        ModelSearcher
    """
    
    def __init__(
            self,
            permitter: Optional[VectorSearchPermissionDispatcher] | None = None,
    ):
        """
        Args:
            permitter: Optional[VectorSearchPermissionDispatcher]
        """
        super().__init__(permitter=permitter or VectorSearchPermissionDispatcher())
    
    @property
    def permitter(self) -> VectorSearchPermissionDispatcher:
        return cast(VectorSearchPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorSearchRequest) -> SearchResult[List[Vector]]:
        """
        Search an VectorChain for context matches.
        
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
        
        # Handle the case that the request is denied.
        decision = self.permitter.execute(
            candidate=VectorSearchPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="VectorSearchPermissionRequest")
            )
        )
        if decision.request_is_denied:
            # Send an exception chain in the result.
            return SearchResult.failure(
                VectorSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorSearcherException.MSG,
                    err_code=VectorSearcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(
            VectorSearchRequest,
            decision.transaction_request
        )
        # --- Extract the transaction participants. ---#
        context = transaction_request.context
        collection = transaction_request.collection
        
        # Ge the context attributes for routing.

        x = context.x
        y = context.y
        # Initialize the result.
        result = SearchResult.failure(
            SearchRouteCoverageException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
            )
        )
        # --- Perform transaction and state management work. ---#
        
        # Entry point int finding by vector id.
        if context.size == 2:
            result = self._find_by_vector(x=x, y=y, collection=collection)
        # Entry point into finding by x.
        if x is not None and y is None:
            result = self._find_by_x(x=x, collection=collection)
        # Entry point into finding by y.
        if x is None and y is not None:
            result = self._find_by_y(y=y, collection=collection)
        # Entry point into finding by email.
        if x is not None and :
            result = self._find_by_email(email=email, collection=collection)
        # Entry point into finding by machine_name.
        if machine_name is not None:
            result = self._find_by_machine_name(machine_name=machine_name, collection=collection)
        # Entry point into finding by vector_type.
        if vector_type is not None:
           result = self._find_by_vector_type(vector_type=vector_type, collection=collection)
        # Handle the case that attribute is not covered.
        if result.is_failure:
            return SearchResult.failure(
                VectorSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorSearcherException.MSG,
                    err_code=VectorSearcherException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Perform transaction and state management work. ---#
        
        # Handle the case that no matches were found.
        if result.is_empty:
            return SearchResult.empty()
        # Otherwise send the
        matches =  cast(List[Vector], result.payload)
        return SearchResult.success(matches)
          
    def _find_by_id(
            self, id, collection: VectorChain
    ) -> SearchResult[List[Vector]]:
        """id_context handler"""
        matches: List[Vector] = []
        for item in collection.iterator:
            if item.id == id:
                matches.append(item)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_y(
            self, y: int, collection: VectorChain) -> SearchResult:
        """y_context handler"""
        matches: List[VectorNode] = []
        cursor = collection.iterator
        while cursor.has_next:
            node = cast(Vector, cursor)
            vector = node.content
            if vector is not None and vector.y == y:
                matches.append(node)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_x(self, x: int, collection: VectorChain) -> SearchResult:
        """x_context handler"""
        matches: List[VectorNode] = []
        cursor = collection.iterator
        while cursor.has_next:
            node = cast(Vector, cursor)
            vector = node.content
            if vector is not None and vector.x == x:
                matches.append(node)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)
    
    def _find_by_vector(self, x: int, y: int, collection: VectorChain) -> SearchResult:
        """vector_context handler"""
        matches: List[VectorNode] = []
        cursor = collection.iterator
        while cursor.has_next:
            node = cast(Vector, cursor)
            vector = node.content
            if vector is not None and vector.x == x and vector.y == y:
                matches.append(node)
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.succes(matches)


        