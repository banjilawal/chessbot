# src/fabrication/contractor/rank/king/contractor.py

"""
Module: fabrication.contractor.rank.king.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import King, KingBlueprint
from err import KingSubcontractorException, RankBlueprintNullException
from fabrication import RankSubcontractor
from util import  LoggingLevelRouter

class KingSubcontractor(RankSubcontractor[King]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a King.

    Attributes:

    Provides:
            -   def execute(blueprint: KingBlueprint) -> BuildResult[King]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: KingBlueprint) -> BuildResult[King]:
        """
        Routes a KingBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[King]
        Returns:
            BuildResult[King]
        Raises:
            KingSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=KingBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                KingSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingSubcontractorException.MSG,
                    err_code=KingSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(KingBlueprint, validation.payload)

        # --- Send the work product to the caller. ---#
        model = King(persona=fingerprint.persona)
        return BuildResult.success(model)