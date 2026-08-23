# src/domain/metadata/nulls/model/board/roster.py

"""
Module: domain.metadata.nulls.model.board.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Board
from err import (
    BoardBlueprintNullException, BoardCarrierNullException, BoardContextNullException, BoardNullException
)


@dataclass
class BoardNullExceptionRoster(ModelNullExceptionRoster[Board]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Board.

    Attributes:
        model: BoardNullException
        carrier: BoardCarrierNullException
        blueprint: BoardBlueprintNullException
        search_context: BoardContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: BoardNullException = BoardNullException()
    carrier: BoardCarrierNullException = BoardCarrierNullException()
    blueprint: BoardBlueprintNullException = BoardBlueprintNullException()
    search_context: BoardContextNullException = BoardContextNullException()