# src/assurance/validator/model/encounter/common/data/table.py

"""
Module: assurance.validator.model.encounter.common.table.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from assurance import RootPropertyTable
from domain import Model, PrimeExtract

T = TypeVar("T", bound="Model")

class ProductEnvelope(ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores a Super class's properties that a ReferenceReferenceTableGenerator
            validates

    Attributes:
        prime_extract: PrimeExtract[T]
        safe_properties: ReferenceSuperClassPropertyTable[T]
    
    Provides:

    Super Class:
    """
    _prime_extract: PrimeExtract[T]
    _safe_properties: RootPropertyTable[T]

    
    
    def __init__(
            self,
            prime_extract: PrimeExtract[T],
            safe_properties: RootPropertyTable[T],
    ):
        """
        Args:
            prime_extract: PrimeExtract[T]
            safe_properties: ReferenceSuperClassPropertyTable[T]
        """
        self._prime_extract = prime_extract
        self._safe_properties = safe_properties
        
    @property
    def prime_extract(self) -> PrimeExtract[T]:
        return self._prime_extract
    
    @property
    def safe(self) -> RootPropertyTable[T]:
        return self._safe_properties

    