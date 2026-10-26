# src/domain/metadata/nulls/context/path/group.py

"""
Module: domain.metadata.nulls.context.path.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullGroup
from err import (
    PathContextBlueprintNullException, PathContextCarrierNullException, PathContextNullException
)


class PathContextNullGroup(ContextNullGroup[PathContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Path's integrity cycle.

    Attributes:
        context: PathContextNullException
        carrier: PathContextCarrierNullException
        blueprint: PathContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[PathContextNullException] | None = None,
            carrier: Optional[PathContextCarrierNullException] | None = None,
            blueprint: Optional[PathContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[PathContextNullException]
            carrier: Optional[PathContextCarrierNullException]
            blueprint: Optional[PathContextBlueprintNullException]
        """
        super().__init__(
            context = context or PathContextNullException(),
            carrier = carrier or PathContextCarrierNullException(),
            blueprint = blueprint or PathContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> PathContextNullException:
        return cast(PathContextNullException, super().context)
    
    @property
    def carrier(self) -> PathContextCarrierNullException:
        return cast(PathContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PathContextBlueprintNullException:
        return cast(PathContextBlueprintNullException, super().blueprint)