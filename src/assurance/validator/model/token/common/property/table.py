# src/assurance/validator/model/token/common/property.table.py

"""
Module: assurance.validator.model.token.common.property.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import TokenSafePropertyTable
from domain import TokenPrimeExtract


class TokenValidationReference:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores TokenValidationReferenceGenerator success data.

    Attributes:
        prime_extract: TokenPrimeExtract
        safe_property_table: SafeSuperTokenPropertyTable

    Provides:

    Super Class:
    """
    _prime_extract: TokenPrimeExtract
    _safe_property_table: TokenSafePropertyTable
    
    def __init__(
            self,
            prime_extract: TokenPrimeExtract,
            safe_property_table: TokenSafePropertyTable
    ):
        """
            prime_extract: TokenPrimeExtract
            safe_property_table: SafeSuperTokenPropertyTable
        """
        self._prime_extract = prime_extract
        self._safe_property_table = safe_property_table
        
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return self._prime_extract
    
    @property
    def safe(self) -> TokenSafePropertyTable:
        return self._safe_property_table
    