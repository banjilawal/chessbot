# src/domain/metadata/nulls/context/coord/group.py

"""
Module: domain.metadata.nulls.context.coord.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, ContextNullGroup
from err import (
    CoordContextBlueprintNullException, CoordContextCarrierNullException, CoordContextNullException
)


class CoordContextNullGroup(ContextNullGroup[CoordContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Coord's integrity cycle.

    Attributes:
        model: CoordContextNullException
        carrier: CoordContextCarrierNullException
        blueprint: CoordContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CoordContextNullException] | None = None,
            carrier: Optional[CoordContextCarrierNullException] | None = None,
            blueprint: Optional[CoordContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CoordContextNullException]
            carrier: Optional[CoordContextCarrierNullException]
            blueprint: Optional[CoordContextBlueprintNullException]
        """
        super().__init__(
            model=model or CoordContextNullException(),
            carrier=carrier or CoordContextCarrierNullException(),
            blueprint=blueprint or CoordContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> CoordContextNullException:
        return cast(CoordContextNullException, super().model)
    
    @property
    def carrier(self) -> CoordContextCarrierNullException:
        return cast(CoordContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CoordContextBlueprintNullException:
        return cast(CoordContextBlueprintNullException, super().blueprint)