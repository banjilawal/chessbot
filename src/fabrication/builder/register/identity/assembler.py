# src/fabrication/builder/register/identity/fabrication/builder.py

"""
Module: fabrication.builder.register.identity.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from fabrication.builder import RegisterBuilder
from domain.metadata.blueprint import IdentityRegisterBlueprint
from domain.structure.register import IdentityRegister
from artifcat import BuildResult
from util import LoggingLevelRouter


class IdentityRegisterBuilder(RegisterBuilder[IdentityRegister]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create an IdentityRegister instance from the safe blueprint.

    Attributes:

    Provides:
        -  def execute(self, blueprint: IdentityRegisterBlueprint,) -> BuildResult[IdentityRegister]

    Super Class:
        RegisterBuilder
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