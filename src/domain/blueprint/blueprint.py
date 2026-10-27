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

from domain import LoadState, ValidationState
from err import NullException

T = TypeVar("T")


class Blueprint(ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an Object.

     Attributes:
        state: ValidationState
        
        domain_class: Type[T]
        domain_class_mane: str
        domain_null_exception: NullException

     Provides:
        -   def mark_as_validated(self)

     Super Class:
     """
    

    _domain_class: Type[T]
    _domain_null_exception: NullException
    _validation_state: ValidationState
    _load_state: LoadState
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: NullException,
            validation_state: Optional[ValidationState] | None = None,
            load_state: Optional[LoadState] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: NullException
            validation_state: Optional[ValidationState]
        """
        self._domain_class = domain_class
        self._domain_null_exception = domain_null_exception
        self._validation_state = validation_state or ValidationState.NOT_VALIDATED
        self._load_state = load_state or LoadState.NOT_LOADED
        
    @property
    def validation_state(self) -> ValidationState:
        return self._validation_state
    
    @validation_state.setter
    def validation_state(self, other: ValidationState):
        if (
                self._validation_state != ValidationState.NOT_VALIDATED and
                other == ValidationState.VALIDATED
        ):
            self._validation_state = other
    
    @property
    def load_state(self) -> LoadState:
        return self.load_state
    
    @load_state.setter
    def load_state(self, other: LoadState):
        if (
                self._load_state != LoadState.NOT_LOADED and
                other == LoadState.LOADED
        ):
            self._load_state = other
            
    
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
        if self._validation_state == ValidationState.NOT_VALIDATED:
            self._validation_state = ValidationState.VALIDATED

