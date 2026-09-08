# src/domain/metadata/nulls/model/square/home/group.py

"""
Module: domain.metadata.nulls.model.square.home.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import SquareNullGroup
from err import HomeSquareBlueprintNullException, HomeSquareCarrierNullException, HomeSquareNullException


class HomeSquareNullGroup(SquareNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a HomeSquare's integrity cycle.

    Attributes:
        model: HomeSquareNullException
        carrier: HomeSquareCarrierNullException
        blueprint: HomeSquareBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[HomeSquareNullException] | None = None,
            carrier: Optional[HomeSquareCarrierNullException] | None = None,
            blueprint: Optional[HomeSquareBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[HomeSquareNullException]
            carrier: Optional[HomeSquareCarrierNullException]
            blueprint: Optional[HomeSquareBlueprintNullException]
        """
        super().__init__(
            model = model or HomeSquareNullException(),
            carrier = carrier or HomeSquareCarrierNullException(),
            blueprint = blueprint or HomeSquareBlueprintNullException(),
        )
        
    @property
    def model(self) -> HomeSquareNullException:
        return cast(HomeSquareNullException, super().model)
    
    @property
    def carrier(self) -> HomeSquareCarrierNullException:
        return cast(HomeSquareCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> HomeSquareBlueprintNullException:
        return cast(HomeSquareBlueprintNullException, super().blueprint)