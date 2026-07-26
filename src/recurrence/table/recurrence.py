# src/recurrence/table/space.py

"""
Module: recurrence.table.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from mapper import SpaceMapFunctionStream


T = TypeVar("T", bound="Space")


class RecurrenceTable(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store a set of space relations to run as a job.

    Attributes:
        space_set: Tuple[Space, ...]
        
    Provides:

    Super Class:
    """
    _space_mapping_function_stream: SpaceMapFunctionStream[T]

    
    def __init__(
            self,
            space_mapping_function_stream: SpaceMapFunctionStream[T]
    ):
        """
        Args:
            space_mapping_function_stream: SpaceMapFunctionStream[T]
        """
        self.__space_mapping_function_stream = space_mapping_function_stream
        
    @property
    def space_mapping_function_stream(self) -> SpaceMapFunctionStream[T]:
        return  self._space_mapping_function_stream

    
    @property
    @abstractmethod
    def number_of_recurrences(self) -> int:
        pass
    
    @property
    @abstractmethod
    def are_no_recurrences(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def recurrences_exist(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def iterator(self) -> iter:
        pass
