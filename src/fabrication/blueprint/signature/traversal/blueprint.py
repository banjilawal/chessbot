# src/builder/pattern/traversal/builder.py

"""
Module: builder.pattern.traversal.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from fabrication.blueprint import SignatureBlueprint
from err import TraversalSignatureNullException
from topology.recurrence import RecurrenceRegistryCollection

T = TypeVar("T", bound="TraversalSignature")

class TraversalSignatureBlueprint(SignatureBlueprint, ABC, Generic[T]):
    _recurrence_set: RecurrenceRegistryCollection[T]
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: TraversalSignatureNullException,
            recurrence_sets: RecurrenceRegistryCollection[T],
    ):
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._recurrence_set = recurrence_sets
        
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> TraversalSignatureNullException:
        return cast(TraversalSignatureNullException, super().null_exception)
        
    @property
    def recurrence_sets(self) -> RecurrenceRegistryCollection[T]:
        return self._recurrence_set
