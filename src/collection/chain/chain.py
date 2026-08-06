# src/collection/chain/chain.py

"""
Module: collection.chain.chain
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, Type, TypeVar, cast

from assurance import NumberValidator
from node import Node
from result import BuildResult, DeletionResult, InsertionResult, SearchResult, ValidationResult
from util import LoggingLevelRouter
from util.decorator.logging import logging_monitor

T = TypeVar("T")


class LinkedList(ABC, Generic[T]):
    _number_validator: NumberValidator
    _iterator: LinkedListIterator
    
    _head: Node[T]
    _tail: Node[T]
    _size: int
    
    def __init__(
            self,
            head: Optional[Node[T]] | None = None,
            tail: Optional[Node[T]] | None = None,
            number_validator: Optional[NumberValidator] | None = None
    ):
        self._number_validator = number_validator or NumberValidator()
        self._head = head or Node[T]()
        self._tail = tail or Node[T]()
        
        self._head.previous = None
        self._tail.next = None
        
        self._head.next = self._tail
        self._tail.previous = self._head
        self._size = 0
        self._iterator = LinkedListIterator(self)
        
    @property
    def head(self) -> Node:
        return self._head
    
    @property
    def tail(self) -> Node:
        return self._tail
    
    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, other: int):
        self._size = self._size + other
    
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
    
    @property
    def iterator(self) -> LinkedListIterator:
        return self._iterator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def add_node(self, node: Node[T]) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def remove_node(self, node: Node[T]) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def find_node(self, node: Node[T]) -> InsertionResult:
        pass
        
    @LoggingLevelRouter.monitor
    def find_by_index(self, index: int) -> SearchResult[List[Node[T]]]:
        method = f"{self.__class__.__name__}.get_by_index"
        
        counter: int = 0
        cursor = self._head
        node: Node[T] = Node[T]()
        
        if self.is_empty:
            return SearchResult.empty()
        
        if index is None or index == 0:
            return SearchResult[[self._head.next]]

        if index == -1 or index == self._size - 1:
            return SearchResult[[self._tail.previous]]
            
        while counter < index and cursor.next is not None:
            cursor = cursor.next
            counter = counter + 1
        return SearchResult.success([cursor])
    
    
    @LoggingLevelRouter.monitor
    def delete_at_index(self, index: int) -> DeletionResult[Node[T]]:
        method = f"{self.__class__.__name__}.execute"
        
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
    
    @LoggingLevelRouter.monitor
    def trim_head(self, offset: int) -> BuildResult[LinkedList[T]]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = self.index_validator(offset)
        # Handle the case that, the search fails.
        if valdation.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=validation.exception
                )
            )
        counter = 0
        cursor = self.iterator.next()
        while self.iterator.has_next and counter < offset:
            counter = counter + 1
            cursor = self.iterator.next()
        self._head.next = cursor
        cursor.previous = self._head
        self._size = self._size - offset
        return BuildResult.success(self)
    
    @LoggingLevelRouter.monitor
    def trim_tail(self, offset: int) -> BuildResult[LinkedList[T]]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = self.index_validator(offset)
        # Handle the case that, the search fails.
        if validation.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=validation.exception
                )
            )
        counter = 0
        cursor = self.iterator.next()
        while self.iterator.has_next and counter < offset:
            counter = counter + 1
            cursor = self.iterator.next()
        self._tail.previous = cursor
        cursor.next = self._tail
        self._size = self._size - offset
        return BuildResult.success(self)

    def index_validator(self, candidate: Any) -> ValidationResult[int]:
        method = f"{self.__class__.__name__}.execute"
        
        if candidate is None:
            return ValidationResult.success(0)
        
        if not isinstance(candidate, int):
            return DeletionResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=search.exception
                )
            )
        index = cast(int, candidate)
        
        # Handle the case that, the index is out of bounds.
        if abs(index) >= self.size:
            # Send the exception in the result.
            return ValidationResult.failure(
                LinkedListException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=LinkedListException.MSG,
                    err_code=LinkedListException.ERR_CODE,
                    ex=ListIndexOutOfBoundsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ListIndexOutOfBoundsException.MSG,
                        err_code=ListIndexOutOfBoundsException.ERR_CODE,
                    )
                )
            )
        if index < 0:
            return ValidationResult.success(self.size - (1 + index))
        
class LinkedListIterator:
    _cursor: Node
    _linked_list: LinkedList
    
    def __init__(self, linked_list: LinkedList):
        self._linked_list = linked_list
        self._cursor = self._linked_list.head
    
    @property
    def has_next(self,) -> bool:
        return self._cursor.next is None
    
    def next(self) -> Node:
        if self.has_next():
            next_node = self._cursor.next
            self._cursor = self._cursor.next
            return self._cursor.next
        else:
            return self._cursor
            
            
            
    
