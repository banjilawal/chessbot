# src/fabrication/contractor/square/home/contractor.py

"""
Module: fabrication.contractor.square.home.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import HomeSquare, HomeSquareBlueprint
from err import HomeSquareSubcontractorException, HomeSquareNullException, SquareBlueprintNullException
from fabrication import SquareSubcontractor
from util import IdFactory, LoggingLevelRouter

class HomeSquareSubcontractor(SquareSubcontractor[HomeSquare]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a HomeSquare.

    Attributes:

    Provides:
            -   def execute(blueprint: HomeSquareBlueprint) -> BuildResult[HomeSquare]

    Super Class:
        SquareSubcontractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: HomeSquareBlueprint) -> BuildResult[HomeSquare]:
        """
        Routes a HomeSquareBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[HomeSquare]
        Returns:
            BuildResult[HomeSquare]
        Raises:
            HomeSquareSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=HomeSquareBlueprint,
            null_exception=SquareBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                HomeSquareSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareSubcontractorException.MSG,
                    err_code=HomeSquareSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(HomeSquareBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="HomeSquare")
        
        # --- Send the work product to the caller. ---#
        model = HomeSquare(
            id=id,
            name=fingerprint.name,
            coord=fingerprint.coord,
            formation=fingerprint.formation,
        )
        model.occupant = fingerprint.occupant
        model.state = fingerprint.validation_state
        return BuildResult.success(model)