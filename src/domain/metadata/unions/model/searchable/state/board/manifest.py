# src/domain/metadata/unions/model/searchable/state/board/manifest.py

"""
Module: domain.metadata.unions.model.searchable.state.board.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Board, BoardBlueprint, BoardCarrier, BoardSearchSearchContext


@dataclass
class BoardTypeUnions(ModelTypeUnions[Board]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Board uses in the domain.

    Attributes:
        model: Type[Board] = Board
        carrier: Type[BoardCarrier] = BoardCarrier
        blueprint: Type[BoardBlueprint] = BoardBlueprint
        search_context: Type[BoardSearchContext] = BoardSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Board] = Board
    carrier: Type[BoardCarrier] = BoardCarrier
    blueprint: Type[BoardBlueprint] = BoardBlueprint
    search_context: Type[BoardSearchSearchContext] = BoardSearchSearchContext