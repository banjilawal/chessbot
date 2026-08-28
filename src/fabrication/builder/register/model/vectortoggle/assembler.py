# src/fabrication/builder/register/model/cartesianToggleRegister/fabrication/builder.py

"""
Module: fabrication.builder.register.model.cartesianToggleRegister.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import RegisterBuilder
from domain.metadata.blueprint import CartesianToggleRegisterBlueprint
from domain.structure.register import CartesianToggleRegister
from artifcat import BuildResult
from util import LoggingLevelRouter


class CartesianToggleRegisterBuilder(
    RegisterBuilder[CartesianToggleRegister]
):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a CartesianToggleRegister instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(
                    blueprint: CartesianToggleRegisterBlueprint,
            ) -> BuildResult[CartesianToggleRegister]

    Super Class:
        RegisterBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: CartesianToggleRegisterBlueprint,
    ) -> BuildResult[CartesianToggleRegister]:
        """
        Assemble a CartesianToggleRegister from the Blueprint's contents.

        Args:
            blueprint: CartesianToggleRegisterBlueprint
        Returns:
            BuildResult[CartesianToggleRegister]
        Raises:
        """
        method = f"{self.__class__.__name__}.validate"
        return BuildResult.success(
            CartesianToggleRegister(u=blueprint.u, v=blueprint.v, )
        )
