# src/domain/metadata/unions/board/manifest.py

"""
Module: domain.metadata.unions.board.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Board, BoardBlueprint, TypeUnion
from transit import BoardCarrier


@dataclass
class BoardTypeUnion(TypeUnion[Board]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Board uses in the domain.

    Attributes:
        model: Type[Board] = Board
        carrier: Type[BoardCarrier] = BoardCarrier
        blueprint: Type[BoardBlueprint] = BoardBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Board] = Board
    carrier: Type[BoardCarrier] = BoardCarrier
    blueprint: Type[BoardBlueprint] = BoardBlueprint