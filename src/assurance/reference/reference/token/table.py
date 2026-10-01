# src/assurance/reference/reference/token/table.py

"""
Module: assurance.reference.reference.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from assurance import TokenReferencePropertyTable, ValidationReference
from domain import Token, TokenPrimeExtract


class TokenValidationReference(ValidationReference[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Token super class properties that are reference.

    Attributes:
            prime_extract: TokenPrimeExtract
            reference_properties: TokenReferencePropertyTable

    Provides:

    Super Class:
        ValidationReferenceTable
    """
    
    def __init__(
            self,
            prime_extract: TokenPrimeExtract,
            reference_properties: TokenReferencePropertyTable,
    ):
        """
            prime_extract: TokenPrimeExtract
            reference_properties: TokenReferencePropertyTable
        """
        super().__init__(
            prime_extract=prime_extract,
            reference_properties=reference_properties,
        )
    
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return cast(TokenPrimeExtract, super().prime_extract)
    
    @property
    def reference_properties(self) -> TokenReferencePropertyTable:
        return cast(TokenReferencePropertyTable, super().reference_properties)


