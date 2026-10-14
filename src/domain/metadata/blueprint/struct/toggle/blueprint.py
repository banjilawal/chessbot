# src/domain/metadata/blueprint/struct/toggle/struct.py

"""
Module: domain.metadata.blueprint.struct.toggle.struct
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, Type, TypeVar, cast

from domain import StructBlueprint, Toggle
from err import ToggleNullException

S = TypeVar("S", bound="Toggle")
M = TypeVar("M")


class ToggleBlueprint(StructBlueprint[S, M], ABC, Generic[S, M]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Toggle.

     Attributes:
         domain_class: Type[S]
         domain_null_exception: ToggleNullException

     Provides:

     Super Class:
        Blueprint
     """
    _max_enabled_toggles: int
    
    def __init__(
            self,
            domain_class: Type[S],
            max_enabled_toggles: Optional[int] | None = None,
            domain_null_exception: Optional[ToggleNullException] | None= None,
    ):
        """
        Args:
            domain_class: Type[S]
            max_enabled_toggles: Optional[int]
            domain_null_exception: ToggleNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or ToggleNullException()
        )
        self._max_enabled_toggles = max_enabled_toggles or 1
    
    @property
    def domain_class(self) -> Type[S]:
        return cast(Type[S], super().domain_class)
    
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
    def to_dict(self) -> Dict[str, M]:
        pass

    
        
        
