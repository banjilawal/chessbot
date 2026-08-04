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
    
    def add_node(
            self,
            node: VectorNode,
            index: Optional[int] | None = None,
    ) -> InsertionResult:
        method = f"{self.__class__.__name__}.add_node"
        
        next: VectorNode = VectorNode()
        previous: VectorNode = VectorNode()
        
        if index == None or index == 0:
            next = self.head.next
            previous = self.head
            
        if index == self.size - 1 or index == -1:
            previous = self.tail.previous
            next = self.tail
        else
        
        

        
        
        
    
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
    
