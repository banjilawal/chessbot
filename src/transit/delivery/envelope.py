# src/transit/delivery/envelop.py

"""
Module: transit.delivery.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Model, PrimeExtract

T = TypeVar("T", bound="Model")

class ProductEnvelope(ABC, Generic[T]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RootValidator forwarded to client validators.

    Attributes:
        prime_extract: PrimeExtract[T]
    
    Provides:

    Super Class:
    """
    _prime_extract: PrimeExtract[T]
    
    
    def __init__(
            self,
            prime_extract: PrimeExtract[T],
    ):
        """
        Args:
            prime_extract: PrimeExtract[T]
        """
        self._prime_extract = prime_extract
        
    @property
    def prime_extract(self) -> PrimeExtract[T]:
        return self._prime_extract

    