# src/assurance/manifest/types/manifest.py

"""
Module: assurance.manifest.types.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from fabrication import Blueprint
from transit import EntityCarrier

T = TypeVar("T", bound="Model")

@dataclass(frozen=True)
class TypesManifest(ABC, Generic[T]):
    model: Type[T]
    carrier: Type[EntityCarrier[T]]
    blueprint: Type[Blueprint[T]]