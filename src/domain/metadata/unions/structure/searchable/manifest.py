# src/domain/metadata/unions/structure/searchable/manifest.py

"""
Module: domain.metadata.unions.structure.searchable.searchable.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, Type, TypeVar

from domain import Blueprint, SearchContext, SearchableStructure, StructureSearchContext, StructureTypeUnions
from transit import EntityCarrier

T = TypeVar("T", bound="SearchableStructure")

@dataclass
class SearchableStructureTypeUnions(StructureTypeUnions[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a SearchableStructure uses in the domain.

    Attributes:
        structure: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
        search_context: StructureSearchContext[T]
        
    Provides:

    Super Class:
        StructureTypeUnions
    """
    structure: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]
    search_context: StructureSearchContext[T]