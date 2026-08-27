# src/fabrication/builder/model/scalar/fabrication/builder.py

"""
Module: fabrication.builder.model.scalar.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import ScalarBlueprint
from domain.model import Scalar
from artifcat import BuildResult
from fabrication.builder import ModelBuilder
from util import LoggingLevelRouter



class ScalarBuilder(ModelBuilder[Scalar]):
    """
    Role
        -  Builder
    
    Responsibilities:
        1.  Create a Scalar instance from the safe blueprint.
    
    Attributes:
    
    Provides:
        - def execute(self, blueprint: ScalarBlueprint,) -> BuildResult[Scalar]
    
    Super Class:
        ModelBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ScalarBlueprint,) -> BuildResult[Scalar]:
        """
        Assemble a Scalar from the Blueprint's contents.

        Args:
            blueprint: ScalarBlueprint
        Returns:
            BuildResult[Scalar]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(Scalar(magnitude=blueprint.magnitude))

