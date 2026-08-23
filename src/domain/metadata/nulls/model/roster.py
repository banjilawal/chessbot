# src/domain/metadata/nulls/roster.py

"""
Module: domain.metadata.nulls.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from domain import Model, NullExceptionRoster
from err import (
    BlueprintNullException, ContextNullException, EntityCarrierNullException, ModelNullException,
)

T = TypeVar("T", bound="Model")

@dataclass
class ModelNullExceptionRoster(NullExceptionRoster[T], Generic[T]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Model

    Attributes:
        model: ModelNullException
        carrier: EntityCarrierNullException
        blueprint: BlueprintNullException
        search_context: Optional[ContextNullException] = None

    Provides:

    Super Class:
        NullExceptionRoster
    """
    model: ModelNullException
    carrier: EntityCarrierNullException
    blueprint: BlueprintNullException
    search_context: Optional[ContextNullException] = None