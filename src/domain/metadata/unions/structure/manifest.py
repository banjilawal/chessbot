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
from typing import Generic, Type, TypeVar

from domain import Blueprint, DomainObjectTypeUnions, Structure
from transit import EntityCarrier

T = TypeVar("T", bound="Structure")

@dataclass
class StructureTypeUnions(DomainObjectTypeUnions[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Structure uses in the domain.

    Attributes:
        structure: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
    Provides:

    Super Class:
        DomainObjectTypeUnions
    """
    structure: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]