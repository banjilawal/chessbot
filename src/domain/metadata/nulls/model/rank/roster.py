# src/domain/metadata/nulls/model/rank/roster.py

"""
Module: domain.metadata.nulls.model.rank.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Rank
from err import (
    RankBlueprintNullException, RankCarrierNullException, RankStackContextNullException, RankNullException
)


@dataclass
class RankNullExceptionRoster(ModelNullExceptionRoster[Rank]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Rank.

    Attributes:
        model: RankNullException
        carrier: RankCarrierNullException
        blueprint: RankBlueprintNullException
        search_context: RankContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: RankNullException = RankNullException()
    carrier: RankCarrierNullException = RankCarrierNullException()
    blueprint: RankBlueprintNullException = RankBlueprintNullException()
    search_context: RankStackContextNullException = RankStackContextNullException()