# src/domain/extract/context/board/extract.py

"""
Module: domain.extract.context.board.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, BoardContextBlueprint, ContextPrimeExtract
from transit import BoardContextCarrier


class BoardContextPrimeExtract(ContextPrimeExtract[BoardContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for BoardValidator.

    Attributes:
        contextCarrier: BoardContextCarrier
        blueprint: Optional[BoardContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: BoardContextCarrier,
            blueprint: Optional[BoardContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: BoardContextCarrier
            blueprint: Optional[ContextBlueprint[Board]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> BoardContextCarrier:
        return cast(BoardContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[BoardContextBlueprint]:
        return cast(BoardContextBlueprint, super().blueprint)