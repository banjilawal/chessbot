# src/assurance/validator/model/attack/common/property.table.py

"""
Module: assurance.validator.model.attack.common.property.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import SafeSuperAttackPropertyTable
from domain import AttackPrimeExtract


class CommonAttackPropertyTable:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores CommonAttackPropertyTableGenerator success data.

    Attributes:
        prime_extract: AttackPrimeExtract
        safe_property_table: SafeSuperAttackPropertyTable

    Provides:

    Super Class:
    """
    _prime_extract: AttackPrimeExtract
    _safe_property_table: SafeSuperAttackPropertyTable
    
    def __init__(
            self,
            prime_extract: AttackPrimeExtract,
            safe_property_table: SafeSuperAttackPropertyTable
    ):
        """
            prime_extract: AttackPrimeExtract
            safe_property_table: SafeSuperAttackPropertyTable
        """
        self._prime_extract = prime_extract
        self._safe_property_table = safe_property_table
        
    @property
    def prime_extract(self) -> AttackPrimeExtract:
        return self._prime_extract
    
    @property
    def safe(self) -> SafeSuperAttackPropertyTable:
        return self._safe_property_table
    