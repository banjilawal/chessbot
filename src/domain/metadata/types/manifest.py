# src/domain/metadata/types/manifest.py

"""
Module: domain.metadata.types.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from domain import DomainObject

T = TypeVar("T", bound="DomainObject")

@dataclass
class DomainObjectAssociationManifest(ABC, Generic[T]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types associated with a domain object.

    Attributes:
        model: Type[T]
    Provides:

    Super Class:
    """
    model: Type[T]