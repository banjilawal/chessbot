# src/domain/metadata/nulls/model/board/group.py

"""
Module: domain.metadata.nulls.model.board.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, NullExceptionGroup
from err import (
    BoardBlueprintNullException, BoardCarrierNullException, BoardNullException
)


class BoardNullGroup(NullExceptionGroup[Board]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Board's integrity cycle.

    Attributes:
        model: BoardNullException
        carrier: BoardCarrierNullException
        blueprint: BoardBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[BoardNullException] | None = None,
            carrier: Optional[BoardCarrierNullException] | None = None,
            blueprint: Optional[BoardBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[BoardNullException]
            carrier: Optional[BoardCarrierNullException]
            blueprint: Optional[BoardBlueprintNullException]
        """
        super().__init__(
            model = model or BoardNullException(),
            carrier = carrier or BoardCarrierNullException(),
            blueprint = blueprint or BoardBlueprintNullException(),
        )
        
    @property
    def model(self) -> BoardNullException:
        return cast(BoardNullException, super().model)
    
    @property
    def carrier(self) -> BoardCarrierNullException:
        return cast(BoardCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BoardBlueprintNullException:
        return cast(BoardBlueprintNullException, super().blueprint)