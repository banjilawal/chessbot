# src/domain/metadata/nulls/model/arena/roster.py

"""
Module: domain.metadata.nulls.model.arena.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Arena
from err import (
    ArenaBlueprintNullException, ArenaCarrierNullException, ArenaSearchContextNullException, ArenaNullException
)


@dataclass
class ArenaNullExceptionRoster(ModelNullExceptionRoster[Arena]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Arena.

    Attributes:
        model: ArenaNullException
        carrier: ArenaCarrierNullException
        blueprint: ArenaBlueprintNullException
        search_context: ArenaContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: ArenaNullException = ArenaNullException()
    carrier: ArenaCarrierNullException = ArenaCarrierNullException()
    blueprint: ArenaBlueprintNullException = ArenaBlueprintNullException()
    search_context: ArenaSearchContextNullException = ArenaSearchContextNullException()