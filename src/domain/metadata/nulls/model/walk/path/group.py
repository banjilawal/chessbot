# src/domain/metadata/nulls/model/walk/path/group.py

"""
Module: domain.metadata.nulls.model.walk.path.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import PathBlueprintNullException, PathCarrierNullException, PathNullException


class PathNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Path's integrity cycle.

    Attributes:
        model: PathNullException
        carrier: PathCarrierNullException
        blueprint: PathBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[PathNullException] | None = None,
            carrier: Optional[PathCarrierNullException] | None = None,
            blueprint: Optional[PathBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PathNullException]
            carrier: Optional[PathCarrierNullException]
            blueprint: Optional[PathBlueprintNullException]
        """
        super().__init__(
            model = model or PathNullException(),
            carrier = carrier or PathCarrierNullException(),
            blueprint = blueprint or PathBlueprintNullException(),
        )
        
    @property
    def model(self) -> PathNullException:
        return cast(PathNullException, super().model)
    
    @property
    def carrier(self) -> PathCarrierNullException:
        return cast(PathCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PathBlueprintNullException:
        return cast(PathBlueprintNullException, super().blueprint)