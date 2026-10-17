# src/fabrication/contractor/model/token/combatant.contractor.py

"""
Module: fabrication.contractor.model.token.combatant.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult, ValidationResult
from domain import CombatantToken, CombatantTokenBlueprint
from err import CombatantTokenSubcontractorException, HomeSquareNullException, TokenBlueprintNullException
from fabrication import TokenSubcontractor
from util import IdFactory, LoggingLevelRouter

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
            return BuildResult.failure(
                CombatantTokenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenSubcontractorException.MSG,
                    err_code=CombatantTokenSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(CombatantTokenBlueprint, validation.payload)
        id = fingerprint.id or IdFactory.next_id(class_name="CombatantToken")
        
        home_square = fingerprint.home_square
        if home_square is None:
            return BuildResult.failure(
                CombatantTokenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenSubcontractorException.MSG,
                    err_code=CombatantTokenSubcontractorException.ERR_CODE,
                    ex=HomeSquareNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeSquareNullException.MSG,
                        err_code=HomeSquareNullException.ERR_CODE,
                    ),
                )
            )
        
        model = CombatantToken(
            id=id,
            team=fingerprint.team,
            home_square=home_square,
            footstep=fingerprint.footstep,
            formation=fingerprint.formation,
        )
        return BuildResult.success(model)