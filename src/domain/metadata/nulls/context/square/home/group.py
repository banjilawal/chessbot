# src/domain/metadata/nulls/context/square/home/group.py

"""
Module: domain.metadata.nulls.context.square.home.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import SquareContextNullGroup
from err import (
    HomeSquareContextBlueprintNullException, HomeSquareContextCarrierNullException, HomeSquareContextNullException
)


class HomeSquareContextNullGroup(SquareContextNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a HomeSquare's integrity cycle.

    Attributes:
        context: HomeSquareContextNullException
        carrier: HomeSquareContextCarrierNullException
        blueprint: HomeSquareContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[HomeSquareContextNullException] | None = None,
            carrier: Optional[HomeSquareContextCarrierNullException] | None = None,
            blueprint: Optional[HomeSquareContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[HomeSquareContextNullException]
            carrier: Optional[HomeSquareContextCarrierNullException]
            blueprint: Optional[HomeSquareContextBlueprintNullException]
        """
        super().__init__(
            context = context or HomeSquareContextNullException(),
            carrier = carrier or HomeSquareContextCarrierNullException(),
            blueprint = blueprint or HomeSquareContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> HomeSquareContextNullException:
        return cast(HomeSquareContextNullException, super().context)
    
    @property
    def carrier(self) -> HomeSquareContextCarrierNullException:
        return cast(HomeSquareContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> HomeSquareContextBlueprintNullException:
        return cast(HomeSquareContextBlueprintNullException, super().blueprint)