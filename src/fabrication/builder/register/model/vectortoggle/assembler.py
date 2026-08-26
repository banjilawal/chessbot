# src/fabrication/builder/register/model/vectorToggleRegister/fabrication/builder.py

"""
Module: fabrication.builder.register.model.vectorToggleRegister.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import RegisterBuilder
from domain.metadata.blueprint import VectorToggleRegisterBlueprint
from domain.structure.register import CartesianToggleRegister
from artifcat import BuildResult
from util import LoggingLevelRouter


class VectorToggleRegisterBuilder(
    RegisterBuilder[CartesianToggleRegister]
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
        RegisterBuilder
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
