# src/assembler/register/model/vectorToggleRegister/py

"""
Module: assembler.register.model.vectorToggleRegister.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assembler import RegisterAssembler
from blueprint import VectorToggleRegisterBlueprint
from register import VectorToggleRegister
from result import BuildResult
from util import LoggingLevelRouter


class VectorToggleRegisterAssembler(
    RegisterAssembler[VectorToggleRegister]
):
    """
    Role
        -   Build Process Owner

    Responsibilities:
        1.  Create a VectorToggleRegister instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(
                    blueprint: VectorToggleRegisterBlueprint,
            ) -> BuildResult[VectorToggleRegister]

    Super Class:
        RegisterAssembler
    """
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: VectorToggleRegisterBlueprint,
    ) -> BuildResult[VectorToggleRegister]:
        """
        Assemble a VectorToggleRegister from the Blueprint's contents.

        Args:
            blueprint: VectorToggleRegisterBlueprint
        Returns:
            BuildResult[VectorToggleRegister]
        Raises:
        """
        method = f"{self.__class__.__name__}.validate"
        return BuildResult.success(
            VectorToggleRegister(
                a=blueprint.a,
                b=blueprint.b,
            )
        )
