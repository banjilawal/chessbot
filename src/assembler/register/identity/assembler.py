# src/assembler/register/identity/py

"""
Module: assembler.register.identity.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from assembler import RegisterAssembler
from blueprint import IdentityRegisterBlueprint
from register import IdentityRegister
from result import BuildResult
from util import LoggingLevelRouter


class IdentityRegisterAssembler(RegisterAssembler[IdentityRegister]):
    """
    Role
        -   Build Process Owner

    Responsibilities:
        1.  Create an IdentityRegister instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: IdentityRegisterBlueprint,) -> BuildResult[IdentityRegister]

    Super Class:
        RegisterAssembler
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: IdentityRegisterBlueprint) -> BuildResult[IdentityRegister]:
        """
        Assemble an IdentityRegister from the Blueprint's contents.

        Args:
            blueprint: IdentityRegisterBlueprint
        Returns:
            BuildResult[IdentityRegister]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            IdentityRegister(id=blueprint.id, name=blueprint.name)
        )