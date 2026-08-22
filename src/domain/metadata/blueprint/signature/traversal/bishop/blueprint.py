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
            null_exception: Optional[BishopSignatureNullException],
            model_class: Type[BishopSignature] = BishopSignature,
    ):
        """
        Args:
            recurrence_sets: BishopRecurrenceSets,
            null_exception: Optional[BishopSignatureNullException],
            model_class: Type[BishopSignature] = BishopSignature,
        """
        super().__init__(
            model_class=model_class,
            recurrence_sets=recurrence_sets,
            null_exception=null_exception or BishopSignatureNullException(),
        )
        
    @property
    def model_class(self) -> Type[BishopSignature]:
        return cast(Type[BishopSignature], super().model_class)
    
    @property
    def null_exception(self) -> BishopSignatureNullException:
        return cast(BishopSignatureNullException, super()._null_exception)
    
    @property
    def recurrence_sets(self) -> BishopRecurrenceRegistries:
        return cast(BishopRecurrenceRegistries, super().recurrence_sets)