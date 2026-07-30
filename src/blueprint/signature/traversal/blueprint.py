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

from blueprint import SignatureBlueprint
from err import TraversalSignatureNullException
from recurrence import RecurrenceSet

T = TypeVar("T", bound="TraversalSignature")

class TraversalSignatureBlueprint(SignatureBlueprint, ABC, Generic[T]):
    _recurrence_table_group: RecurrenceSet[T]
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: TraversalSignatureNullException,
            recurrence_sets: RecurrenceSet[T],
    ):
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._recurrence_table_group = recurrence_sets
        
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> TraversalSignatureNullException:
        return cast(TraversalSignatureNullException, super().null_exception)
        
    @property
    def recurrence_sets(self) -> RecurrenceSet[T]:
        return self._recurrence_table_group
