# src/assurance/validator/model/encounter/common/property.table.py

"""
Module: assurance.validator.model.encounter.common.property.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import EncounterSafePropertyTable
from domain import EncounterPrimeExtract


class EncounterProductEnvelope:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores EncounterProductEnvelopeGenerator success data.

    Attributes:
        prime_extract: EncounterPrimeExtract
        safe_property_table: SafeSuperEncounterPropertyTable

    Provides:

    Super Class:
    """
    _prime_extract: EncounterPrimeExtract
    _safe_property_table: EncounterSafePropertyTable
    
    def __init__(
            self,
            prime_extract: EncounterPrimeExtract,
            safe_property_table: EncounterSafePropertyTable
    ):
        """
            prime_extract: EncounterPrimeExtract
            safe_property_table: SafeSuperEncounterPropertyTable
        """
        self._prime_extract = prime_extract
        self._safe_property_table = safe_property_table
        
    @property
    def prime_extract(self) -> EncounterPrimeExtract:
        return self._prime_extract
    
    @property
    def safe(self) -> EncounterSafePropertyTable:
        return self._safe_property_table
    