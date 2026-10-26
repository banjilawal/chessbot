# src/domain/bluprint/blueprint.py

"""
Module: domain.bluprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar

from domain.blueprint.state import BlueprintState
from err import NullException

T = TypeVar("T")


class Blueprint(ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an Object.

     Attributes:
        state: BlueprintState
        domain_class: Type[T]
        domain_class_mane: str
        domain_null_exception: NullException

     Provides:

     Super Class:
     """
    
    _state: BlueprintState
    _domain_class: Type[T]
    _domain_null_exception: NullException
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: NullException,
            state: Optional[BlueprintState] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: NullException
            state: Optional[BlueprintState]
        """
        self._domain_class = domain_class
        self._domain_null_exception = domain_null_exception
        self._state = state or BlueprintState.INSECURE_BLUEPRINT
        
    @property
    def state(self) -> BlueprintState:
        return self._state
    
    @property
    def domain_class(self) -> Type[T]:
        return self._domain_class
    
    @property
    def domain_null_exception(self) -> NullException:
        return  self._domain_null_exception
    
    @property
    def domain_class_name(self) -> str:
        return self._domain_class.__class__.__name__
    
    def mark_as_validated(self):
        if self._state == BlueprintState.INSECURE_BLUEPRINT:
            self._state = BlueprintState.VALIDATED_BLUEPRINT

