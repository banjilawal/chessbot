# src/domain/metadata/null/context/board/null.py

"""
Module: domain.metadata.null.context.board.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, ContextNullWarningSet
from err import (
    BoardContextBlueprintNullException, BoardContextCarrierNullException, BoardContextNullException
)


class BoardContextNullWarningSet(ContextNullWarningSet[BoardContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Board's integrity cycle.

    Attributes:
        model: BoardContextNullException
        carrier: BoardContextCarrierNullException
        blueprint: BoardContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[BoardContextNullException] | None = None,
            carrier: Optional[BoardContextCarrierNullException] | None = None,
            blueprint: Optional[BoardContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[BoardContextNullException]
            carrier: Optional[BoardContextCarrierNullException]
            blueprint: Optional[BoardContextBlueprintNullException]
        """
        super().__init__(
            model=model or BoardContextNullException(),
            carrier=carrier or BoardContextCarrierNullException(),
            blueprint=blueprint or BoardContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> BoardContextNullException:
        return cast(BoardContextNullException, super().model)
    
    @property
    def carrier(self) -> BoardContextCarrierNullException:
        return cast(BoardContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BoardContextBlueprintNullException:
        return cast(BoardContextBlueprintNullException, super().blueprint)