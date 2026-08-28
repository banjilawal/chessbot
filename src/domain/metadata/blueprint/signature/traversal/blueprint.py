# src/domain/metadata/builder/pattern/traversal/builder.py

"""
Module: builder.pattern.traversal.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain.metadata.blueprint import SignatureBlueprint
from err import TraversalSignatureNullException
from topology.recurrence import RecurrenceRegistryCollection

T = TypeVar("T", bound="TraversalSignature")

class TraversalSignatureBlueprint(SignatureBlueprint, ABC, Generic[T]):
    _recurrence_set: RecurrenceRegistryCollection[T]
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: TraversalSignatureNullException,
            recurrence_sets: RecurrenceRegistryCollection[T],
    ):
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception)
        self._recurrence_set = recurrence_sets
        
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TraversalSignatureNullException:
        return cast(TraversalSignatureNullException, super().domain_null_exception)
        
    @property
    def recurrence_sets(self) -> RecurrenceRegistryCollection[T]:
        return self._recurrence_set
