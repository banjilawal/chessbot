# src/domain/metadata/nulls/model/vector/roster.py

"""
Module: domain.metadata.nulls.model.vector.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Vector
from err import (
    VectorBlueprintNullException, VectorCarrierNullException, VectorNullException
)


@dataclass
class VectorNullExceptionRoster(ModelNullExceptionRoster[Vector]):
    """
    Role:
        -  Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Vector.

    Attributes:
        model: VectorNullException
        carrier: VectorCarrierNullException
        blueprint: VectorBlueprintNullException
        search_context: VectorContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: VectorNullException = VectorNullException()
    carrier: VectorCarrierNullException = VectorCarrierNullException()
    blueprint: VectorBlueprintNullException = VectorBlueprintNullException()
    search_context: VectorContextNullException = VectorContextNullException()