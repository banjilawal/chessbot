# src/assembler/register/model/square/py

"""
Module: assembler.register.model.square.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assembler import RegisterAssembler
from blueprint import SquareRegisterBlueprint
from register import SquareRegister
from result import BuildResult
from util import LoggingLevelRouter


class SquareRegisterAssembler(RegisterAssembler[SquareRegister]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new SquareRegister instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    blueprint: SquareRegisterBlueprint,
            ) -> ValidationResult[SquareRegisterBlueprint]

     Super Class:
        RegisterAssembler
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