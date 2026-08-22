# src/assembler/register/model/number/assembler.py

"""
Module: assembler.register.model.number.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from fabrication.assembler import RegisterAssembler
from domain.metadata.blueprint import NumberRegisterBlueprint
from domain.structure.register import NumberRegister
from result import BuildResult
from util import LoggingLevelRouter


class NumberRegisterAssembler(RegisterAssembler[NumberRegister]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new NumberRegister instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    blueprint: NumberRegisterBlueprint,
            ) -> ValidationResult[NumberRegisterBlueprint]

     Super Class:
        RegisterAssembler
     """
    
    
    @LoggingLevelRouter.monitor()
    def execute(self, blueprint: NumberRegisterBlueprint,) -> BuildResult[NumberRegister]:
        """
        Assemble a NumberRegister from the Blueprint's contents.

        Args:
            blueprint: NumberRegisterBlueprint
        Returns:
            BuildResult[NumberRegister]
        Raises:
        """
        return BuildResult.success(
            NumberRegister(a=blueprint.a, b=blueprint.b,)
        )
        