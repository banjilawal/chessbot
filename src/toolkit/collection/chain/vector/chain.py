# src/toolkit/collection/chain/vector/chain.py

"""
Module: toolkit.collection.chain.vector.chain
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from collection import Chain
from err import SearchResultEmptyException
from node import VectorNode
from result import DeletionResult, InsertionResult, SearchResult
from util import LoggingLevelRouter


class VectorChain(Chain[VectorNode]):
    
    def __init__(
            self,
            head: Optional[VectorNode] = VectorNode(),
            tail: Optional[VectorNode] = VectorNode(),
    ):
        super().__init__(head=head, tail=tail)
        
    @property
    def head(self) -> VectorNode:
        return cast(VectorNode, super().head)
    
    @property
    def tail(self) -> VectorNode:
        return cast(VectorNode, super().tail)
        
    @LoggingLevelRouter.monitor
    def get_at_offset(self, index: int) -> SearchResult[List[VectorNode]]:
        method = f"{self.__class__.__name__}.get_by_index"
        
        # Handle the case that, the index is not a safe number.
        search = super().get_at_offset(index)
        # Send the exception in the result.
        if search.is_failure:
            return SearchResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        if search.is_empty:
            return SearchResult.empty()
        node = cast(VectorNode, search.payload[0])
        return SearchResult.success([node])
    
    @LoggingLevelRouter.monitor
    def remove_at_offset(self, offset: int) -> DeletionResult[VectorNode]:
        method = f"{self.__class__.__name__}.remove_by_index"
        
        # Hand off get the node to the finder
        search = self.get_at_offset(offset)
        
        # Handle the case that, the search fails.
        if search.is_failure:
            # Send the exception in the result.
            return DeletionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        # Handle the case that there is nothing at the index.
        if search.is_empty:
            return DeletionResult.nothing_to_delete()
        
        node = cast(VectorNode, search.payload[0])
        node.previous.next = node.next
        node.next.previous  = node.previous
        self._size = self._size - 1
        
        node.previous = None
        node.next = None
        
        return DeletionResult.success(node)
    
    @LoggingLevelRouter.monitor
    def find_node(self, node: VectorNode) -> SearchResult[List[VectorNode]]:
        method = f"{self.__class__.__name__}.find_node"
        
        while self.iterator.has_next:
            cursor = cast(VectorNode, self.iterator.next())
            if cursor == node:
                return SearchResult.success([node])
        return SearchResult.empty()
        
    
    def add_node(
            self,
            node: VectorNode,
            offset: Optional[int] | None = None,
    ) -> InsertionResult:
        method = f"{self.__class__.__name__}.execute"
        
        index_validation = self.offset_validator(offset)
        if index_validation.is_failure:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=index_validation.exception
                )
            )
        search = self.find_node(node)
        if search.is_failure:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        if search.is_not_empty:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        previous = self.get_at_offset(offset)
        if previous.is_failure:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=previous.exception
                )
            )
        if previous.is_empty:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=SearchResultEmptyException()
                )
            )
        next = previous.next
        node.previous = previous
        node.next = next
        
        previous.next = node
        next.previous = node
        
        self.size = self.size + 1
        return InsertionResult.success()
    
    def remove_node(
            self,
            node: VectorNode,
    ) -> DeletionResult[VectorNode]:
        method = f"{self.__class__.__name__}.add_node"
        
        search = self.find_node(node)
        if search.is_failure:
            # Send the exception in the result.
            return DeletionResult.failure(
                VectorChainException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainException.MSG,
                    err_code=VectorChainException.ERR_CODE,
                    ex=search.exception
                )
            )
        if search.is_empty:
            return DeletionResult.nothing_to_delete()
        node = cast(VectorNode, search.payload[0])
        previous = node.previous
        next = node.next
        
        previous.next = next
        next.previous = previous
        
        node.next = None
        node.previous = None
        
        self.size = self.size - 1
        return DeletionResult.success(node)
    
    
    @LoggingLevelRouter.monitor
    def trim_to_node(self, node: VectorNode):
        method = f"{self.__class__.__name__}.execute"
        
        counter = 0
        cursor = cast(VectorNode, self.iterator.next())
        while self.iterator.has_next or cursor != node:
            counter = counter + 1
            if cursor != node:
                cursor = cast(VectorNode, self.iterator.next())
        if cursor != node:
            return DeletionResult.nothing_to_delete()
        self.tail.previous = cursor
        cursor.next = self.tail
        self.size = self.size - counter
        return DeletionResult.success(self)
        
    
    def add_node(self, node: Node[T], index: Optional[int] | None = None):
        antecedent: Node[T] = Node[T]()
        precedent: Node[T] = Node[T]()
        cursor: Node[T] = self._head
        counter: int = 0
        
        if index is None or index == -1:
            index = 0
            
        while counter < index:
            
        
        
        

            precedent = self._head
            antecedent = self._head.next
        else:
            
            
            self._head.next.previous = node
            self._head.next = node
        self._size = self._size + 1
        
    def
    
