# src/domain/metadata/unions/model/manifest.py

"""
Module: domain.metadata.unions.model.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, Type, TypeVar

from domain import Blueprint, EntityCarrier, Model, ModelSearchContext, DomainObjectTypeUnions

T = TypeVar("T", bound="Model")

@dataclass
class ModelTypeUnions(DomainObjectTypeUnions[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Model uses in the domain.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
        search_context: Optional[StackSearchContext[T]]
    Provides:

    Super Class:
        DomainObjectManifest
    """
    model: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]
    search_context: Optional[ModelSearchContext[T]] = None