# src/domain/extract/context/path/extract.py

"""
Module: domain.extract.context.path.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextPrimeExtract, Path, PathContextBlueprint
from transit import PathContextCarrier


class PathContextPrimeExtract(ContextPrimeExtract[PathContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for PathValidator.

    Attributes:
        contextCarrier: PathContextCarrier
        blueprint: Optional[PathContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: PathContextCarrier,
            blueprint: Optional[PathContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: PathContextCarrier
            blueprint: Optional[ContextBlueprint[Path]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> PathContextCarrier:
        return cast(PathContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PathContextBlueprint]:
        return cast(PathContextBlueprint, super().blueprint)