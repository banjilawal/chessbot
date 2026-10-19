# src/fabrication/contractor/rank/pawn/contractor.py

"""
Module: fabrication.contractor.rank.pawn.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import Pawn, PawnBlueprint
from err import PawnSubcontractorException, RankBlueprintNullException
from fabrication import RankSubcontractor
from util import  LoggingLevelRouter

class PawnSubcontractor(RankSubcontractor[Pawn]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a Pawn.

    Attributes:

    Provides:
            -   def execute(blueprint: PawnBlueprint) -> BuildResult[Pawn]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: PawnBlueprint) -> BuildResult[Pawn]:
        """
        Routes a PawnBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[Pawn]
        Returns:
            BuildResult[Pawn]
        Raises:
            PawnSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=PawnBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                PawnSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnSubcontractorException.MSG,
                    err_code=PawnSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(PawnBlueprint, validation.payload)

        # --- Send the work product to the caller. ---#
        model = Pawn(persona=fingerprint.persona)
        return BuildResult.success(model)