# src/domain/metadata/nulls/model/coord/roster.py

"""
Module: domain.metadata.nulls.model.coord.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Coord
from err import (
    CoordBlueprintNullException, CoordCarrierNullException, CoordContextNullException, CoordNullException
)


@dataclass
class CoordNullExceptionRoster(ModelNullExceptionRoster[Coord]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Coord.

    Attributes:
        model: CoordNullException
        carrier: CoordCarrierNullException
        blueprint: CoordBlueprintNullException
        search_context: CoordContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: CoordNullException = CoordNullException()
    carrier: CoordCarrierNullException = CoordCarrierNullException()
    blueprint: CoordBlueprintNullException = CoordBlueprintNullException()
    search_context: CoordContextNullException = CoordContextNullException()