# src/fabrication/contractor/rank/queen/contractor.py

"""
Module: fabrication.contractor.rank.queen.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import Queen, QueenBlueprint
from err import QueenSubcontractorException, RankBlueprintNullException
from fabrication import RankSubcontractor
from util import  LoggingLevelRouter

class QueenSubcontractor(RankSubcontractor[Queen]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a Queen.

    Attributes:

    Provides:
            -   def execute(blueprint: QueenBlueprint) -> BuildResult[Queen]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: QueenBlueprint) -> BuildResult[Queen]:
        """
        Routes a QueenBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[Queen]
        Returns:
            BuildResult[Queen]
        Raises:
            QueenSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=QueenBlueprint,
            null_exception=RankBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                QueenSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QueenSubcontractorException.MSG,
                    err_code=QueenSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(QueenBlueprint, validation.payload)

        # --- Send the work product to the caller. ---#
        model = Queen(persona=fingerprint.persona)
        return BuildResult.success(model)