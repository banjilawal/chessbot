# src/domain/metadata/nulls/model/square/roster.py

"""
Module: domain.metadata.nulls.model.square.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Square
from err import (
    SquareBlueprintNullException, SquareCarrierNullException, SquareStackContextNullException, SquareNullException
)


@dataclass
class SquareNullExceptionRoster(ModelNullExceptionRoster[Square]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Square.

    Attributes:
        model: SquareNullException
        carrier: SquareCarrierNullException
        blueprint: SquareBlueprintNullException
        search_context: SquareContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: SquareNullException = SquareNullException()
    carrier: SquareCarrierNullException = SquareCarrierNullException()
    blueprint: SquareBlueprintNullException = SquareBlueprintNullException()
    search_context: SquareStackContextNullException = SquareStackContextNullException()