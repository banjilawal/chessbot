# src/assurance/safe/reference/token/table.py

"""
Module: assurance.safe.reference.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from assurance import TokenSafePropertyTable, ValidationReference
from domain import Token, TokenPrimeExtract


class TokenValidationReference(ValidationReference[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Token super class properties that are safe.

    Attributes:
            prime_extract: TokenPrimeExtract
            safe_properties: TokenSafePropertyTable

    Provides:

    Super Class:
        ValidationReferenceTable
    """
    
    def __init__(
            self,
            prime_extract: TokenPrimeExtract,
            safe_properties: TokenSafePropertyTable,
    ):
        """
            prime_extract: TokenPrimeExtract
            safe_properties: TokenSafePropertyTable
        """
        super().__init__(
            prime_extract=prime_extract,
            safe_properties=safe_properties,
        )
    
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return cast(TokenPrimeExtract, super().prime_extract)
    
    @property
    def safe_properties(self) -> TokenSafePropertyTable:
        return cast(TokenSafePropertyTable, super().safe_properties)


