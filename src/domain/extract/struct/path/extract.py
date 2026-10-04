# src/domain/extract/struct/path/extract.py

"""
Module: domain.extract.struct.path.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StructPrimeExtract, Path, PathBlueprint
from transit import PathCarrier


class PathPrimeExtract(StructPrimeExtract[Path]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for PathValidator.

    Attributes:
        carrier: PathCarrier
        blueprint: Optional[PathBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: PathCarrier,
            blueprint: Optional[PathBlueprint] | None = None,
    ):
        """
        Args:
            carrier: PathCarrier
            blueprint: Optional[Blueprint[Path]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> PathCarrier:
        return cast(PathCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[PathBlueprint]:
        return cast(PathBlueprint, super().blueprint)