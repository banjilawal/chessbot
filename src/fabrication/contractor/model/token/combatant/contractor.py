# src/fabrication/contractor/model/token/combatant.contractor.py

"""
Module: fabrication.contractor.model.token.combatant.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import BuildResult
from domain import CombatantToken, CombatantTokenBlueprint
from err import TokenBlueprintNullException
from fabrication import TokenSubcontractor
from util import LoggingLevelRouter

class CombatantTokenSubcontractor(TokenSubcontractor[CombatantToken]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Token.

    Attributes:

    Provides:
            -   def execute(blueprint: CombatantTokenBlueprint) -> BuildResult[CombatantToken]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CombatantTokenBlueprint) -> BuildResult[CombatantToken]:
        """
        Routes a CombatantTokenBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[CombatantToken]
        Returns:
            BuildResult[CombatantToken]
        Raises:
            CombatantTokenSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=CombatantTokenBlueprint,
            null_exception=TokenBlueprintNullException(),
        )
        if validation.is_failure:
            return ValidationResult.failure(
                CombatantTokenSubcontractorException(
                
                )
            )