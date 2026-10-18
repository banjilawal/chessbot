# src/fabrication/contractor/model/encounter/stalemate/contractor.py

"""
Module: fabrication.contractor.model.encounter.stalemate.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import StalemateEncounter, StalemateEncounterBlueprint
from err import StalemateEncounterSubcontractorException, EncounterBlueprintNullException
from fabrication import EncounterSubcontractor
from util import IdFactory, LoggingLevelRouter

class StalemateEncounterSubcontractor(EncounterSubcontractor[StalemateEncounter]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a StalemateEncounter.

    Attributes:

    Provides:
            -   def execute(blueprint: StalemateEncounterBlueprint) -> BuildResult[StalemateEncounter]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: StalemateEncounterBlueprint) -> BuildResult[StalemateEncounter]:
        """
        Routes a StalemateEncounterBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[StalemateEncounter]
        Returns:
            BuildResult[StalemateEncounter]
        Raises:
            StalemateEncounterSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=StalemateEncounterBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                StalemateEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=StalemateEncounterSubcontractorException.MSG,
                    err_code=StalemateEncounterSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(StalemateEncounterBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="StalemateEncounter")
        
        # --- Send the work product to the caller. ---#
        model = StalemateEncounter(
            id=id,
            victim=fingerprint.victim,
            location=fingerprint.location,
            attacker_reward=fingerprint.attacker_reward,
            attacker_maneuver=fingerprint.attacker_maneuver,
        )
        return BuildResult.success(model)