# src/fabrication/contractor/model/encounter/checkmate/contractor.py

"""
Module: fabrication.contractor.model.encounter.checkmate.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import CheckmateEncounter, CheckmateEncounterBlueprint
from err import CheckmateEncounterSubcontractorException, EncounterBlueprintNullException
from fabrication import EncounterSubcontractor
from util import IdFactory, LoggingLevelRouter

class CheckmateEncounterSubcontractor(EncounterSubcontractor[CheckmateEncounter]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Encounter.

    Attributes:

    Provides:
            -   def execute(blueprint: CheckmateEncounterBlueprint) -> BuildResult[CheckmateEncounter]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CheckmateEncounterBlueprint) -> BuildResult[CheckmateEncounter]:
        """
        Routes a CheckmateEncounterBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[CheckmateEncounter]
        Returns:
            BuildResult[CheckmateEncounter]
        Raises:
            CheckmateEncounterSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=CheckmateEncounterBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                CheckmateEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CheckmateEncounterSubcontractorException.MSG,
                    err_code=CheckmateEncounterSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(CheckmateEncounterBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="CheckmateEncounter")
        
        # --- Send the work product to the caller. ---#
        model = CheckmateEncounter(
            id=id,
            victim=fingerprint.victim,
            location=fingerprint.location,
            attacker_reward=fingerprint.attacker_reward,
            attacker_maneuver=fingerprint.attacker_maneuver,
        )
        return BuildResult.success(model)