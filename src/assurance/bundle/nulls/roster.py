# src/assurance/manifest/nulls/roster.py

"""
Module: assurance.manifest.nulls.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from err import BlueprintNullException, EntityCarrierNullException, ModelNullException
from model import Model

T = TypeVar("T", bound="Model")

@dataclass
class NullRoster(ABC, Generic[T]):
    model: ModelNullException
    carrier: EntityCarrierNullException
    blueprint: BlueprintNullException