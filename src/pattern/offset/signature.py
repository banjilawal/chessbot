# src/signature/offset/signature.py

"""
Module: signature.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Iterator, TypeVar

from container import VectorSet
from signature import Signature

T = TypeVar("T", bound="Rank")

class OffsetSignature(Signature, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from a Token's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        MovementSignature
    """
    
    _offsets: VectorSet
    
    def __init__(self, offsets: VectorSet,):
        """
        Args:
            offsets: VectorSet
        """
        self._offsets = offsets
        
    @property
    def offsets(self) -> VectorSet:
        return self._offsets
    
    