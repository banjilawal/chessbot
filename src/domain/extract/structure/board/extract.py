# src/domain/extract/struct/board/extract.py

"""
Module: domain.extract.struct.board.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import StructPrimeExtract
from domain import Board, BoardBlueprint
from transit import BoardCarrier


class BoardPrimeExtract(StructPrimeExtract[Board]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for BoardValidator.

    Attributes:
        carrier: BoardCarrier
        blueprint: Optional[BoardBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: BoardCarrier,
            blueprint: Optional[BoardBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Board]
            blueprint: Optional[Blueprint[Board]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> BoardCarrier:
        return cast(BoardCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[BoardBlueprint]:
        return cast(BoardBlueprint, super().blueprint)