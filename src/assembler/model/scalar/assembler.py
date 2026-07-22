# src/assembler/model/scalar/assembler.py

"""
Module: assembler.model.scalar.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import ScalarBlueprint
from model import Scalar
from result import BuildResult
from assembler import ModelAssembler
from util import LoggingLevelRouter



class ScalarAssembler(ModelAssembler[Scalar]):
    """
    Role
        -   Builder
    
    Responsibilities:
        1.  Create a Scalar instance from the safe blueprint.
    
    Attributes:
    
    Provides:
        -   def execute(self, blueprint: ScalarBlueprint,) -> BuildResult[Scalar]
    
    Super Class:
        ModelAssembler
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

