# src/fabrication/contractor/model/token/king.contractor.py

"""
Module: fabrication.contractor.model.token.king.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import KingToken, KingTokenBlueprint
from err import KingTokenSubcontractorException, HomeSquareNullException, TokenBlueprintNullException
from fabrication import TokenSubcontractor
from util import IdFactory, LoggingLevelRouter

class KingTokenSubcontractor(TokenSubcontractor[KingToken]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Token.

    Attributes:

    Provides:
            -   def execute(blueprint: KingTokenBlueprint) -> BuildResult[KingToken]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: KingTokenBlueprint) -> BuildResult[KingToken]:
        """
        Routes a KingTokenBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[KingToken]
        Returns:
            BuildResult[KingToken]
        Raises:
            KingTokenSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=KingTokenBlueprint,
            null_exception=TokenBlueprintNullException(),
        )
        if validation.is_failure:
            return BuildResult.failure(
                KingTokenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenSubcontractorException.MSG,
                    err_code=KingTokenSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(KingTokenBlueprint, validation.payload)
        id = fingerprint.id or IdFactory.next_id(class_name="KingToken")
        
        home_square = fingerprint.home_square
        if home_square is None:
            return BuildResult.failure(
                KingTokenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenSubcontractorException.MSG,
                    err_code=KingTokenSubcontractorException.ERR_CODE,
                    ex=HomeSquareNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeSquareNullException.MSG,
                        err_code=HomeSquareNullException.ERR_CODE,
                    ),
                )
            )
        
        model = KingToken(
            id=id,
            alert=formation.alert,
            team=fingerprint.team,
            home_square=home_square,
            footstep=fingerprint.footstep,
            formation=fingerprint.formation,
        )
        return BuildResult.success(model)