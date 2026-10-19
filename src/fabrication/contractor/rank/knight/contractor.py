# src/fabrication/contractor/rank/knight/contractor.py

"""
Module: fabrication.contractor.rank.knight.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import Knight, KnightBlueprint
from err import KnightSubcontractorException, RankBlueprintNullException
from fabrication import RankSubcontractor
from util import  LoggingLevelRouter

class KnightSubcontractor(RankSubcontractor[Knight]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a Knight.

    Attributes:

    Provides:
            -   def execute(blueprint: KnightBlueprint) -> BuildResult[Knight]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: KnightBlueprint) -> BuildResult[Knight]:
        """
        Routes a KnightBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[Knight]
        Returns:
            BuildResult[Knight]
        Raises:
            KnightSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=KnightBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                KnightSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KnightSubcontractorException.MSG,
                    err_code=KnightSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(KnightBlueprint, validation.payload)

        # --- Send the work product to the caller. ---#
        model = Knight(persona=fingerprint.persona)
        return BuildResult.success(model)