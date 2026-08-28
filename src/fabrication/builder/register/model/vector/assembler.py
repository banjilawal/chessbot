# src/fabrication/builder/register/model/vector/fabrication/builder.py

"""
Module: fabrication.builder.register.model.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import RegisterBuilder
from domain.metadata.blueprint import VectorRegisterBlueprint
from domain.structure.searchable.register import VectorRegister
from artifcat import BuildResult
from util import LoggingLevelRouter


class VectorRegisterBuilder(RegisterBuilder[VectorRegister]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a VectorRegister instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: VectorRegisterBlueprint,) -> BuildResult[VectorRegister]

    Super Class:
        RegisterBuilder
    """
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorRegisterBlueprint,) -> BuildResult[VectorRegister]:
        """
        Assemble a VectorRegister from the Blueprint's contents.

        Args:
            blueprint: VectorRegisterBlueprint
        Returns:
            BuildResult[VectorRegister]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            VectorRegister(u=blueprint.u, v=blueprint.v)
        )
        
        
