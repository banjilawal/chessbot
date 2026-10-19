# src/fabrication/contractor/encounter/kill/contractor.py

"""
Module: fabrication.contractor.encounter.kill.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import KillEncounter, KillEncounterBlueprint
from err import KillEncounterSubcontractorException, EncounterBlueprintNullException
from fabrication import EncounterSubcontractor
from util import IdFactory, LoggingLevelRouter

class KillEncounterSubcontractor(EncounterSubcontractor[KillEncounter]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a KillEncounter.

    Attributes:

    Provides:
            -   def execute(blueprint: KillEncounterBlueprint) -> BuildResult[KillEncounter]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: KillEncounterBlueprint) -> BuildResult[KillEncounter]:
        """
        Routes a KillEncounterBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[KillEncounter]
        Returns:
            BuildResult[KillEncounter]
        Raises:
            KillEncounterSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=KillEncounterBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                KillEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterSubcontractorException.MSG,
                    err_code=KillEncounterSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(KillEncounterBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="KillEncounter")
        
        # --- Send the work product to the caller. ---#
        model = KillEncounter(
            id=id,
            victim=fingerprint.victim,
            location=fingerprint.location,
            attacker_reward=fingerprint.attacker_reward,
            attacker_maneuver=fingerprint.attacker_maneuver,
        )
        return BuildResult.success(model)