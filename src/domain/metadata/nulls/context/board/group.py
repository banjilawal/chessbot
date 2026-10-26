# src/domain/metadata/nulls/context/board/group.py

"""
Module: domain.metadata.nulls.context.board.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, ContextNullGroup
from err import (
    BoardContextBlueprintNullException, BoardContextCarrierNullException, BoardContextNullException
)


class BoardContextNullGroup(ContextNullGroup[BoardContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Board's integrity cycle.

    Attributes:
        context: BoardContextNullException
        carrier: BoardContextCarrierNullException
        blueprint: BoardContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[BoardContextNullException] | None = None,
            carrier: Optional[BoardContextCarrierNullException] | None = None,
            blueprint: Optional[BoardContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[BoardContextNullException]
            carrier: Optional[BoardContextCarrierNullException]
            blueprint: Optional[BoardContextBlueprintNullException]
        """
        super().__init__(
            context = context or BoardContextNullException(),
            carrier = carrier or BoardContextCarrierNullException(),
            blueprint = blueprint or BoardContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> BoardContextNullException:
        return cast(BoardContextNullException, super().context)
    
    @property
    def carrier(self) -> BoardContextCarrierNullException:
        return cast(BoardContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BoardContextBlueprintNullException:
        return cast(BoardContextBlueprintNullException, super().blueprint)