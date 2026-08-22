# src/assembler/register/model/vectorToggleRegister/assembler.py

"""
Module: assembler.register.model.vectorToggleRegister.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.assembler import RegisterAssembler
from domain.metadata.blueprint import VectorToggleRegisterBlueprint
from domain.structures.register import CartesianToggleRegister
from result import BuildResult
from util import LoggingLevelRouter


class VectorToggleRegisterAssembler(
    RegisterAssembler[CartesianToggleRegister]
):
    """
    Role
        -   Builder

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
    ) -> BuildResult[CartesianToggleRegister]:
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
            CartesianToggleRegister(u=blueprint.u, v=blueprint.v, )
        )
