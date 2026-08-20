# src/assurance/manifest/nulls/manifest.py

"""
Module: assurance.manifest.nulls.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from err import BlueprintNullException, EntityCarrierNullException, ModelNullException

T = TypeVar("T", bound="Model")

@dataclass(frozen=True)
class NullExceptionManifest(ABC, Generic[T]):
    model: ModelNullException = ModelNullException()
    carrier: EntityCarrierNullException = EntityCarrierNullException()
    blueprint: BlueprintNullException = BlueprintNullException()