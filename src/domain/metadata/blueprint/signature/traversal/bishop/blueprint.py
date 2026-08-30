# src/domain/metadata/builder/pattern/traversal/bishop/builder/pattern.py

"""
Module: builder.pattern.traversal.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import  annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import TraversalSignatureBlueprint
from err import BishopSignatureNullException
from topology.pattern import BishopSignature
from topology.recurrence import BishopRecurrenceRegistries


class BishopSignatureBlueprint(TraversalSignatureBlueprint[BishopSignature]):
    
    def __init__(
            self,
            recurrence_sets: BishopRecurrenceRegistries,
            domain_null_exception: Optional[BishopSignatureNullException],
            domain_class: Type[BishopSignature] = BishopSignature,
    ):
        """
        Args:
            recurrence_sets: BishopRecurrenceSets,
            domain_null_exception: Optional[BishopSignatureNullException],
            domain_class: Type[BishopSignature] = BishopSignature,
        """
        super().__init__(
            domain_class=domain_class,
            recurrence_sets=recurrence_sets,
            domain_null_exception=domain_null_exception or BishopSignatureNullException(),
        )
        
    @property
    def domain_class(self) -> Type[BishopSignature]:
        return cast(Type[BishopSignature], super().domain_class)
    
    @property
    def domain_null_exception(self) -> BishopSignatureNullException:
        return cast(BishopSignatureNullException, super().domain_null_exception)
    
    @property
    def recurrence_sets(self) -> BishopRecurrenceRegistries:
        return cast(BishopRecurrenceRegistries, super().recurrence_sets)