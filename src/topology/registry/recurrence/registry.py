# src/recurrence/topology/registry/registry.py

"""
Module: topology.registry.recurrence.registry
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar

from topology import Recurrence, SpaceMapFunctionStream
from domain.model import Vector

T = TypeVar("T", bound="Space")


class RecurrenceRegistry(ABC, Generic[T]):
    """
    Role:
        - Data Holder
        -  Factory
        -  Switcher

    Responsibilities:
        1.  Create an immuregistry set of recurrence relations for batch vector transformations in a space.

    Attributes:
        space_mapping_function_stream: SpaceMapFunctionStream[T]
        number_of_recurrences: int
        recurrences_exist: bool
        no_recurrences_exist: bool
        type_recurrence_dict:  Dict[Type[T], Recurrence[T]]
        
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
    @abstractmethod
    def origin(self) -> Vector:
        pass
        
    @property
    def space_mapping_function_stream(self) -> SpaceMapFunctionStream[T]:
        return  self._space_mapping_function_stream

    
    @property
    @abstractmethod
    def number_of_recurrences(self) -> int:
        pass
    
    @property
    @abstractmethod
    def recurrences_exist(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def no_recurrences_exist(self) -> bool:
        pass

    @property
    @abstractmethod
    def type_recurrence_dict(self) -> Dict[Type[T], Recurrence[T]]:
        pass