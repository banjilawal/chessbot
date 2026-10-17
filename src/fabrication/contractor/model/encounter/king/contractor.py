# src/fabrication/contractor/model/encounter/king/contractor.py

"""
Module: fabrication.contractor.model.encounter.king.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import KingEncounter, KingEncounterBlueprint
from err import KingEncounterSubcontractorException, HomeSquareNullException, EncounterBlueprintNullException
from fabrication import EncounterSubcontractor
from util import IdFactory, LoggingLevelRouter

class KingEncounterSubcontractor(EncounterSubcontractor[KingEncounter]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Encounter.

    Attributes:

    Provides:
            -   def execute(blueprint: KingEncounterBlueprint) -> BuildResult[KingEncounter]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: KingEncounterBlueprint) -> BuildResult[KingEncounter]:
        """
        Routes a KingEncounterBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[KingEncounter]
        Returns:
            BuildResult[KingEncounter]
        Raises:
            KingEncounterSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=KingEncounterBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                KingEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterSubcontractorException.MSG,
                    err_code=KingEncounterSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(KingEncounterBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="KingEncounter")
        
        # Handle the case that the fingerprint does not contain a home_square.
        home_square = fingerprint.home_square
        if home_square is None:
            # Send the exception chain on failure.
            return BuildResult.failure(
                KingEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterSubcontractorException.MSG,
                    err_code=KingEncounterSubcontractorException.ERR_CODE,
                    ex=HomeSquareNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeSquareNullException.MSG,
                        err_code=HomeSquareNullException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product to the caller. ---#
        model = KingEncounter(
            id=id,
            team=fingerprint.team,
            home_square=home_square,
            alert=fingerprint.alert,
            footstep=fingerprint.footstep,
            formation=fingerprint.formation,
        )
        return BuildResult.success(model)