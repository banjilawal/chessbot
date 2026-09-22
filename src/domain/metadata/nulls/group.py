# src/domain/metadata/nulls/roster.py

"""
Module: domain.metadata.nulls.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from domain import DomainDataObject
from err import NullException

T = TypeVar("T")

@dataclass
class NullExceptionGroup(ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a DomainObject

    Attributes:
        model: NullException

    Provides:

    Super Class:
    """
    model: NullException