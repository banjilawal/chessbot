# src/assurance/reference/reference/encounter/table.py

"""
Module: assurance.reference.reference.encounter.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from assurance import EncounterReferencePropertyTable, ValidationReference
from domain import Encounter, EncounterPrimeExtract


class EncounterValidationReference(ValidationReference[Encounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Encounter super class properties that are reference.

    Attributes:
            prime_extract: EncounterPrimeExtract
            reference_properties: EncounterReferencePropertyTable

    Provides:

    Super Class:
        ValidationReferenceTable
    """
    
    def __init__(
            self,
            prime_extract: EncounterPrimeExtract,
            reference_properties: EncounterReferencePropertyTable,
    ):
        """
            prime_extract: EncounterPrimeExtract
            reference_properties: EncounterReferencePropertyTable
        """
        super().__init__(
            prime_extract=prime_extract,
            reference_properties=reference_properties,
        )
        
    @property
    def prime_extract(self) -> EncounterPrimeExtract:
        return cast(EncounterPrimeExtract, super().prime_extract)
    
    @property
    def reference_properties(self) -> EncounterReferencePropertyTable:
        return cast(EncounterReferencePropertyTable, super().reference_properties)
    

    