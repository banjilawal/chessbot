# src/fabrication/contractor/rank/rook/contractor.py

"""
Module: fabrication.contractor.rank.rook.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import Rook, RookBlueprint
from err import RookSubcontractorException, RankBlueprintNullException
from fabrication import RankSubcontractor
from util import  LoggingLevelRouter

class RookSubcontractor(RankSubcontractor[Rook]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a Rook.

    Attributes:

    Provides:
            -   def execute(blueprint: RookBlueprint) -> BuildResult[Rook]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RookBlueprint) -> BuildResult[Rook]:
        """
        Routes a RookBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[Rook]
        Returns:
            BuildResult[Rook]
        Raises:
            RookSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=RookBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                RookSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookSubcontractorException.MSG,
                    err_code=RookSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(RookBlueprint, validation.payload)

        # --- Send the work product to the caller. ---#
        model = Rook(persona=fingerprint.persona)
        return BuildResult.success(model)