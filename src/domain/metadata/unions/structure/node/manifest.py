# src/domain/metadata/unions/structurenode/manifest.py

"""
Module: domain.metadata.unions.structure.node.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, Type, TypeVar

from domain import Blueprint, StructureTypeUnions, EntityCarrier, Node, SearchContext

T = TypeVar("T", bound="Node")


@dataclass
class NodeTypeUnions(StructureTypeUnions[T], ABC, Generic[T]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data unions a Node uses in the domain.

    Attributes:
        node: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
        search_context: Optional[SearchContext[T]]
    Provides:

    Super Class:
        DomainObjectManifest
    """
    node: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]
    search_context: Optional[SearchContext[T]] = None