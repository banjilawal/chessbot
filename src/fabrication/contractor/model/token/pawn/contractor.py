# src/fabrication/contractor/model/token/pawn.contractor.py

"""
Module: fabrication.contractor.model.token.pawn.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import PawnToken, PawnTokenBlueprint
from err import PawnTokenSubcontractorException, HomeSquareNullException, TokenBlueprintNullException
from fabrication import TokenSubcontractor
from util import IdFactory, LoggingLevelRouter

class PawnTokenSubcontractor(TokenSubcontractor[PawnToken]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Token.

    Attributes:

    Provides:
            -   def execute(blueprint: PawnTokenBlueprint) -> BuildResult[PawnToken]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: PawnTokenBlueprint) -> BuildResult[PawnToken]:
        """
        Routes a PawnTokenBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[PawnToken]
        Returns:
            BuildResult[PawnToken]
        Raises:
            PawnTokenSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=PawnTokenBlueprint,
            null_exception=TokenBlueprintNullException(),
        )
        if validation.is_failure:
            return BuildResult.failure(
                PawnTokenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenSubcontractorException.MSG,
                    err_code=PawnTokenSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(PawnTokenBlueprint, validation.payload)
        id = fingerprint.id or IdFactory.next_id(class_name="PawnToken")
        
        home_square = fingerprint.home_square
        if home_square is None:
            return BuildResult.failure(
                PawnTokenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenSubcontractorException.MSG,
                    err_code=PawnTokenSubcontractorException.ERR_CODE,
                    ex=HomeSquareNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeSquareNullException.MSG,
                        err_code=HomeSquareNullException.ERR_CODE,
                    ),
                )
            )
        
        model = PawnToken(
            id=id,
            team=fingerprint.team,
            home_square=home_square,
            footstep=fingerprint.footstep,
            formation=fingerprint.formation,
        )
        return BuildResult.success(model)