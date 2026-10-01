# src/assurance/validator/model/encounter/common/reference/table.py

"""
Module: assurance.validator.model.encounter.common.table.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from assurance import ReferencePropertyTable
from domain import Model, PrimeExtract

T = TypeVar("T", bound="Model")

class ValidationReference(ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores a Super class's properties that a ReferenceReferenceTableGenerator
            validates

    Attributes:
        prime_extract: PrimeExtract[T]
        reference_properties: ReferenceSuperClassPropertyTable[T]
    
    Provides:

    Super Class:
    """
    _prime_extract: PrimeExtract[T]
    _reference_properties: ReferencePropertyTable[T]

    
    
    def __init__(
            self,
            prime_extract: PrimeExtract[T],
            reference_properties: ReferencePropertyTable[T],
    ):
        """
        Args:
            prime_extract: PrimeExtract[T]
            reference_properties: ReferenceSuperClassPropertyTable[T]
        """
        self._prime_extract = prime_extract
        self._reference_properties = reference_properties
        
    @property
    def prime_extract(self) -> PrimeExtract[T]:
        return self._prime_extract
    
    @property
    def reference_properties(self) -> ReferencePropertyTable[T]:
        return self._reference_properties

    