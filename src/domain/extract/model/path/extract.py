# src/domain/extract/model/path/extract.py

"""
Module: domain.extract.model.path.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelPrimeExtract, Path, PathBlueprint
from transit import PathCarrier


class PathPrimeExtract(ModelPrimeExtract[Path]):
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
        ModelPrimeExtract
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