# src/assurance/validator/model/encounter/common/safe/table.py

"""
Module: assurance.validator.model.encounter.common.table.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from assurance import SafePropertyTable
from domain import Model, PrimeExtract

T = TypeVar("T", bound="Model")

class ValidationReference(ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores a Super class's properties that a SafeReferenceTableGenerator
            validates

    Attributes:
        prime_extract: PrimeExtract[T]
        safe_properties: SafeSuperClassPropertyTable[T]
    
    Provides:

    Super Class:
    """
    _prime_extract: PrimeExtract[T]
    _safe_properties: SafePropertyTable[T]

    
    
    def __init__(
            self,
            prime_extract: PrimeExtract[T],
            safe_properties: SafePropertyTable[T],
    ):
        """
        Args:
            prime_extract: PrimeExtract[T]
            safe_properties: SafeSuperClassPropertyTable[T]
        """
        self._prime_extract = prime_extract
        self._safe_properties = safe_properties
        
    @property
    def prime_extract(self) -> PrimeExtract[T]:
        return self._prime_extract
    
    @property
    def safe_properties(self) -> SafePropertyTable[T]:
        return self._safe_properties

    