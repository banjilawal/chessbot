# src/pattern/traversal/traversal.py

"""
Module: pattern.traversal.category.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from _testcapi import Generic
from abc import abstractmethod
from typing import Optional, Tuple, TypeVar

from container import VectorSet

from pattern import Signature, SignatureGenerator
from recurrence import RecurrenceRegistryCollection
from result import ComputationResult
from util import LoggingLevelRouter
from validator import PrimingValidator

T = TypeVar("T", bound="Rank")

class TraversalSignature(Signature, Generic[T]):
    """
    Role:
        -   Iteration


    Responsibilities:
        1.  Stepping function which gives the next vector in a series.

    Attributes:
        recurrence_registry_collection: RecurrenceRegistryCollection[T]

    Provides:

    Super Class:
    """
    _recurrence_registries: RecurrenceRegistryCollection
    
    def __init__(self, recurrence_registries: RecurrenceRegistryCollection[T], ):
        """
        Args:
            recurrence_registries: RecurrenceRegistryCollection[T]
        """
        super().__init__()
        self._recurrence_registries = recurrence_registries

    @property
    def recurrence_registries(self) -> RecurrenceRegistryCollection[T]:
        return self._recurrence_registries
