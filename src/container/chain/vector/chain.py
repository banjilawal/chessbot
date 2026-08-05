# src/container/chain/vector/chain.py

"""
Module: container.chain.vector.chain
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from container import LinkedList
from err import SearchResultEmptyException
from model import Vector
from node import VectorNode
from result import DeletionResult, InsertionResult, SearchResult
from util import LoggingLevelRouter


class VectorLinkedList(LinkedList[Vector]):
    
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
    def find_by_index(self, index: int) -> SearchResult[List[VectorNode]]:
        method = f"{self.__class__.__name__}.get_by_index"
        
        # Handle the case that, the index is not a safe number.
        search = super().find_by_index(index)
        # Send the exception in the result.
        if search.is_failure:
            return SearchResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
                    ex=search.exception
                )
            )
        if search.is_empty:
            return SearchResult.empty()
        node = cast(VectorNode, search.payload[0])
        return SearchResult.success([node])
    
    @LoggingLevelRouter.monitor
    def remove_by_index(self, index: int) -> DeletionResult[VectorNode]:
        method = f"{self.__class__.__name__}.remove_by_index"
        
        # Hand off get the node to the finder
        search = self.find_by_index(index)
        
        # Handle the case that, the search fails.
        if search.is_failure:
            # Send the exception in the result.
            return DeletionResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
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
        
        cursor = self.head
        while cursor.next is not None:
            if cursor == node:
                return SearchResult.success([node])
            cursor = cursor.next
        return SearchResult.empty()
        
    
    def add_node(
            self,
            node: VectorNode,
            index: Optional[int] | None = None,
    ) -> InsertionResult:
        method = f"{self.__class__.__name__}.add_node"
        
        if index is None:
            index = 0
        if abs(index) > self.size:
            return InsertionResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
                    ex=ListIndexOutOfBoundsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ListIndexOutOfBoundsException.MSG,
                        err_code=ListIndexOutOfBoundsException.ERR_CODE,
                    )
                )
            )
        if index < 1:
            index = self.size - (1 + index)
        
        search = self.find_node(node)
        if search.is_failure:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
                    ex=search.exception
                )
            )
        if search.is_not_empty:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
                    ex=search.exception
                )
            )
        previous = self.find_by_index(index)
        if previous.is_failure:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
                    ex=previous.exception
                )
            )
        if previous.is_empty:
            # Send the exception in the result.
            return InsertionResult.failure(
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
                    ex=SearchResultEmptyException()
                )
            )
        node.next = previous.next
        node.previous = previous
        
        previous.next.previous = node
        previous.next = node
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
                VectorLinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorLinkedListException.MSG,
                    err_code=VectorLinkedListException.ERR_CODE,
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
        return DeletionResult.success(Node)
    
    
        
        
        

        
        
        
    
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
    
