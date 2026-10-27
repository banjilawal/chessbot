# src/domain/metadata/null/context/path/null.py

"""
Module: domain.metadata.null.context.path.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullWarningSet
from err import (
    PathContextBlueprintNullException, PathContextCarrierNullException, PathContextNullException
)


class PathContextNullWarningSet(ContextNullWarningSet[PathContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Path's integrity cycle.

    Attributes:
        model: PathContextNullException
        carrier: PathContextCarrierNullException
        blueprint: PathContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[PathContextNullException] | None = None,
            carrier: Optional[PathContextCarrierNullException] | None = None,
            blueprint: Optional[PathContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PathContextNullException]
            carrier: Optional[PathContextCarrierNullException]
            blueprint: Optional[PathContextBlueprintNullException]
        """
        super().__init__(
            model=model or PathContextNullException(),
            carrier=carrier or PathContextCarrierNullException(),
            blueprint=blueprint or PathContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> PathContextNullException:
        return cast(PathContextNullException, super().model)
    
    @property
    def carrier(self) -> PathContextCarrierNullException:
        return cast(PathContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PathContextBlueprintNullException:
        return cast(PathContextBlueprintNullException, super().blueprint)