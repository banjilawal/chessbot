# src/domain/metadata/types/manifest.py

"""
Module: domain.metadata.types.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from domain import Blueprint, DomainMetadata, DomainObject
from domain.transit import EntityCarrier

T = TypeVar("T", bound="DomainObject")

@dataclass
class TypesManifest(DomainMetadata, Generic[T]):
    model: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]