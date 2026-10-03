# src/assurance/data/data/token/table.py

"""
Module: transit.delivery.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from assurance import SafeRootTokenProperties, ValidationReference
from domain import Token, TokenPrimeExtract


class RootTokenValidatorProduct(ValidationReference[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Token super class properties that are reference.

    Attributes:
            prime_extract: TokenPrimeExtract
            safe_properties: TokenReferencePropertyTable

    Provides:

    Super Class:
        ValidationReferenceTable
    """
    
    def __init__(
            self,
            prime_extract: TokenPrimeExtract,
            safe_properties: SafeRootTokenProperties,
    ):
        """
            prime_extract: TokenPrimeExtract
            safe_properties: TokenReferencePropertyTable
        """
        super().__init__(
            prime_extract=prime_extract,
            safe_properties=safe_properties,
        )
    
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return cast(TokenPrimeExtract, super().prime_extract)
    
    @property
    def safe(self) -> SafeRootTokenProperties:
        return cast(SafeRootTokenProperties, super().safe)


