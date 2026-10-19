# src/fabrication/contractor/rank/bishop/contractor.py

"""
Module: fabrication.contractor.rank.bishop.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import Bishop, BishopBlueprint
from err import BishopSubcontractorException, RankBlueprintNullException
from fabrication import RankSubcontractor
from util import  LoggingLevelRouter

class BishopSubcontractor(RankSubcontractor[Bishop]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a Bishop.

    Attributes:

    Provides:
            -   def execute(blueprint: BishopBlueprint) -> BuildResult[Bishop]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: BishopBlueprint) -> BuildResult[Bishop]:
        """
        Routes a BishopBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[Bishop]
        Returns:
            BuildResult[Bishop]
        Raises:
            BishopSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=BishopBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                BishopSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopSubcontractorException.MSG,
                    err_code=BishopSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(BishopBlueprint, validation.payload)

        # --- Send the work product to the caller. ---#
        model = Bishop(persona=fingerprint.persona)
        return BuildResult.success(model)