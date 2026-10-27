# src/domain/bluprint/context/blueprint.py

"""
Module: domain.bluprint.context.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, Type, TypeVar, cast

from domain import Blueprint, BlueprintState, Context
from domain.blueprint.context.state import FlagState
from err import ContextNullException

T = TypeVar("T", bound="Context")


class ContextBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Context.
         
     Attributes:
        max_size: int
        flag_state: FlagState

        domain_class: Type[T]
        domain_null_exception: ContextNullException
        
    Provides:
        is_empty: bool
        is_valid_size: bool
        is_over_capacity: bool
        is_consistent: bool
        is_not_consistent: bool

        -   def to_dict() -> Dict[str, Any]
   
     Super Class:
        Blueprint
     """
    
    _max_size: int
    _flag_state: FlagState
    _id: Optional[int]
    _name: Optional[str]

    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: ContextNullException,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_size: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ContextNullException
            id: Optional[int]
            name: Optional[str]
            max_size: Optional[int]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._id = id
        self._name = name
        self._max_size = max_size or 1
        self._flag_state = FlagState.UNKNOWN
        
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ContextNullException:
        return  cast(ContextNullException, super().domain_null_exception)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def max_size(self) -> int:
        return self._max_size
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def flag_state(self) -> FlagState:
        return self._flag_state
    
    @flag_state.setter
    def flag_state(self, other: FlagState):
        if (
                not self.is_valid_size and
                self._flag_state != FlagState.VALID_SIZE
        ):
            self._flag_state = other
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def exceeds_capacity(self) -> bool:
        return self.size > self.max_size
    
    @property
    def is_valid_size(self) -> bool:
        return 1 <= self.size < self.max_size + 1
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @property
    def is_consistent(self) -> bool:
        return (
                self.is_valid_size and
                self._flag_state == FlagState.VALID_SIZE
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.is_consistent
