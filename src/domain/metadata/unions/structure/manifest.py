# src/domain/metadata/unions/structure/manifest.py

"""
Module: domain.metadata.unions.structure.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, Type, TypeVar

from domain import Blueprint, DomainObjectTypeUnions, EntityCarrier, SearchContext, Structure

T = TypeVar("T", bound="Structure")

@dataclass
class StructureTypeUnions(DomainObjectTypeUnions[T], ABC, Generic[T]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data unions a Structure uses in the domain.

    Attributes:
        structure: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
        search_context: Optional[StackSearchContext[T]]
    Provides:

    Super Class:
        DomainObjectUnions
    """
    structure: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]
    search_context: Optional[SearchContext[T]] = None