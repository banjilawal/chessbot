# src/domain/metadata/unions/structure/searchable/node/manifest.py

"""
Module: domain.metadata.unions.structure.searchable.node.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from domain import Blueprint, Node, NodeContext, SearchableStructureTypeUnions
from transit import EntityCarrier

T = TypeVar("T", bound="Node")


@dataclass
class NodeTypeUnions(SearchableStructureTypeUnions[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Node uses in the domain.

    Attributes:
        node: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
        search_context: NodeContext[T]
    Provides:

    Super Class:
        SearchableStructureTypeUnions
    """
    node: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]
    search_context: NodeContext[T]