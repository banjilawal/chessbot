# src/domain/metadata/types/model/board/manifest.py

"""
Module: domain.metadata.types.model.board.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Board, BoardBlueprint, BoardCarrier, BoardSearchContext


@dataclass
class BoardAssociationManifest(ModelAssociationManifest[Board]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Board uses in the domain.

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
    search_context: Type[BoardSearchContext] = BoardSearchContext