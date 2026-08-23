# src/domain/metadata/nulls/model/scalar/roster.py

"""
Module: domain.metadata.nulls.model.scalar.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Scalar
from err import (
    ScalarBlueprintNullException, ScalarCarrierNullException, ScalarNullException
)


@dataclass
class ScalarNullExceptionRoster(ModelNullExceptionRoster[Scalar]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Scalar.

    Attributes:
        model: ScalarNullException
        carrier: ScalarCarrierNullException
        blueprint: ScalarBlueprintNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: ScalarNullException = ScalarNullException()
    carrier: ScalarCarrierNullException = ScalarCarrierNullException()
    blueprint: ScalarBlueprintNullException = ScalarBlueprintNullException()