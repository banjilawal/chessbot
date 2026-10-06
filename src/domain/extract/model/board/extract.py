# src/domain/extract/model/board/extract.py

"""
Module: domain.extract.model.board.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, BoardBlueprint, ModelPrimeExtract
from transit import BoardCarrier


class BoardPrimeExtract(ModelPrimeExtract[Board]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for BoardValidator.

    Attributes:
        carrier: BoardCarrier
        blueprint: Optional[BoardBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: BoardCarrier,
            safe_blueprint: Optional[BoardBlueprint] | None = None,
    ):
        """
        Args:
            reference: BoardCarrier
            safe_blueprint: Optional[Blueprint[Board]]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> BoardCarrier:
        return cast(BoardCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[BoardBlueprint]:
        return cast(BoardBlueprint, super().blueprint)