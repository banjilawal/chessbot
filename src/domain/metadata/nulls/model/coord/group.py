# src/domain/metadata/nulls/model/coord/group.py

"""
Module: domain.metadata.nulls.model.coord.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, NullExceptionGroup
from err import (
    CoordBlueprintNullException, CoordCarrierNullException, CoordNullException
)


class CoordNullGroup(NullExceptionGroup[Coord]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Coord's integrity cycle.

    Attributes:
        model: CoordNullException
        carrier: CoordCarrierNullException
        blueprint: CoordBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CoordNullException] | None = None,
            carrier: Optional[CoordCarrierNullException] | None = None,
            blueprint: Optional[CoordBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CoordNullException]
            carrier: Optional[CoordCarrierNullException]
            blueprint: Optional[CoordBlueprintNullException]
        """
        super().__init__(
            model = model or CoordNullException(),
            carrier = carrier or CoordCarrierNullException(),
            blueprint = blueprint or CoordBlueprintNullException(),
        )
        
    @property
    def model(self) -> CoordNullException:
        return cast(CoordNullException, super().model)
    
    @property
    def carrier(self) -> CoordCarrierNullException:
        return cast(CoordCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CoordBlueprintNullException:
        return cast(CoordBlueprintNullException, super().blueprint)