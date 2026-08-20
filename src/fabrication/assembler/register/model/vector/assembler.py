# src/assembler/register/model/vector/assembler.py

"""
Module: assembler.register.model.vector.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.assembler import RegisterAssembler
from fabrication.blueprint import VectorRegisterBlueprint
from register import VectorRegister
from result import BuildResult
from util import LoggingLevelRouter


class VectorRegisterAssembler(RegisterAssembler[VectorRegister]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a VectorRegister instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: VectorRegisterBlueprint,) -> BuildResult[VectorRegister]

    Super Class:
        RegisterAssembler
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
        
        
