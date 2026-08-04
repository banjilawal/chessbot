# src/container/chain/chain.py

"""
Module: container.chain.chain
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, Optional, TypeVar, cast

from assurance import NumberValidator
from authorization import DeletionRequest
from node import Node
from result import DeletionResult, SearchResult
from util import LoggingLevelRouter

T = TypeVar("T")


class LinkedList(ABC, Generic[T]):
    _number_validator: NumberValidator
    
    _head: Node[T]
    _tail: Node[T]
    _size: int
    
    def __init__(self, number_validator: Optional[NumberValidator] | None = None):
        self._number_validator = number_validator or NumberValidator()
        self._head = Node[T]()
        self._tail = Node[T]()
        
        self._head.previous = None
        self._tail.next = None
        
        self._head.next = self._tail
        self._tail.previous = self._head
        self._size = 0
        
    @property
    def head(self) -> Node:
        return self._head
    
    @property
    def tail(self) -> Node:
        return self._tail
    
    @property
    def size(self) -> int:
        return self._size
    
    @property
    def is_empty(self) -> bool:
        return (
                self._head.next == self._tail and
                self._tail.previous == self._head and
                self._size == 0
        )
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
        
    @LoggingLevelRouter.monitor
    def find_by_index(self, index: int) -> SearchResult[List[Node[T]]]:
        method = f"{self.__class__.__name__}.get_by_index"
        
        # Handle the case that, the index is not a safe number.
        validation = self._number_validator.execute(index)
        # Send the exception in the result.
        if validation.is_failure:
            return SearchResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # Handle the case that, the index is out of bounds.
        if index > self.size:
            # Send the exception in the result.
            return SearchResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=IndexOutOfBoundsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=IndexOutOfBoundsException.MSG,
                        err_code=IndexOutOfBoundsException.ERR_CODE,
                    )
                )
            )
        counter: int = 0
        cursor = self._head
        
        if self.is_empty:
            return SearchResult.empty()
        
        if index == 0 or index == -1:
            node = self._head.next
            return SearchResult[[node]]
        
        if index == self._size - 1:
            node = self._tail.previous
            return SearchResult[[node]]
        
        while counter < index and cursor.next is not None:
            cursor = cursor.next
            counter = counter + 1
        return SearchResult.success([cursor])
    
    @LoggingLevelRouter.monitor
    def remove_by_index(self, index: int) -> DeletionResult[Node[T]]:
        method = f"{self.__class__.__name__}.remove_by_index"
        
        # Hand off get the node to the finder
        search = self.find_by_index(index)
        
        # Handle the case that, the search fails.
        if search.is_failure:
            # Send the exception in the result.
            return DeletionResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=search.exception
                )
            )
        # Handle the case that there is nothing at the index.
        if search.is_empty:
            return DeletionResult.nothing_to_delete()
        
        node = cast(Node[T], search.payload[0])
        node.previous.next = node.next
        node.next.previous  = node.previous
        self._size = self._size - 1
        
        node.previous = None
        node.next = None
        
        return DeletionResult.success(node)
        
        

        
        
        
    
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
    
