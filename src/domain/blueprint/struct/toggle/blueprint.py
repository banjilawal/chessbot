# src/domain/bluprint/struct/toggle/struct.py

"""
Module: domain.bluprint.struct.toggle.struct
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, Type, TypeVar, cast

from domain import StructBlueprint, Toggle
from err import ToggleNullException

T = TypeVar("T", bound="Toggle")
M = TypeVar("M")


class ToggleBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Toggle.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: ToggleNullException

     ProvideT:

     Super class:
        Blueprint
     """
    _max_enabled_toggleT: int
    
    def __init__(
            self,
            domain_class: Type[T],
            max_enabled_toggleT: Optional[int] | None = None,
            domain_null_exception: Optional[ToggleNullException] | None= None,
    ):
        """
        ArgT:
            domain_class: Type[T]
            max_enabled_toggleT: Optional[int]
            domain_null_exception: ToggleNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or ToggleNullException()
        )
        self._max_enabled_toggles = max_enabled_toggles or 1
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ToggleNullException:
        return cast(ToggleNullException, super().domain_null_exception)
        
    @property
    def max_enabled_toggles(self) -> int:
        return self._max_enabled_toggles
        
    @property
    def no_active_toggles(self) -> bool:
        return self.active_toggles == 0
    
    @property
    def excess_active_toggles(self) -> bool:
        return self.active_toggles > self._max_enabled_toggles
    
    @property
    def active_toggles(self) -> int:
        return len(self.to_dict)
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

    
        
        
