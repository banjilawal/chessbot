# src/fabrication/builder/register/model/square/fabrication/builder.py

"""
Module: fabrication.builder.register.model.square.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import RegisterBuilder
from domain.metadata.blueprint import SquareRegisterBlueprint
from domain.structure.register import SquareRegister
from artifcat import BuildResult
from util import LoggingLevelRouter


class SquareRegisterBuilder(RegisterBuilder[SquareRegister]):
    """
    Role
        -  Transaction Worker
        -  Integrity Maintenance
        -  Consistency Assurance
        -  Build Process Owner

   Responsibilities:
        1.  Ensure a new SquareRegister instance is born safe and reliable.

     Attributes:

    Provides:
        - def execute(
                    blueprint: SquareRegisterBlueprint,
            ) -> ValidationResult[SquareRegisterBlueprint]

     Super Class:
        RegisterBuilder
     """
    
    
    @LoggingLevelRouter.monitor()
    def execute(self, blueprint: SquareRegisterBlueprint,) -> BuildResult[SquareRegister]:
        """
        Assemble a SquareRegister from the Blueprint's contents.

        Args:
            blueprint: SquareRegisterBlueprint
        Returns:
            BuildResult[SquareRegister]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            SquareRegister(
                origin=blueprint.origin,
                destination=blueprint.destination,
            )
        )