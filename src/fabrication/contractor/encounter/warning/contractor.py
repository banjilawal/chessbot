# src/fabrication/contractor/encounter/warning/contractor.py

"""
Module: fabrication.contractor.encounter.warning.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import EncounterWarning, EncounterWarningBlueprint
from err import EncounterWarningSubcontractorException, EncounterBlueprintNullException
from fabrication import EncounterSubcontractor
from util import IdFactory, LoggingLevelRouter

class EncounterWarningSubcontractor(EncounterSubcontractor[EncounterWarning]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a concrete Encounter.

    Attributes:

    Provides:
            -   def execute(blueprint: EncounterWarningBlueprint) -> BuildResult[EncounterWarning]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: EncounterWarningBlueprint) -> BuildResult[EncounterWarning]:
        """
        Routes a EncounterWarningBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[EncounterWarning]
        Returns:
            BuildResult[EncounterWarning]
        Raises:
            EncounterWarningSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=EncounterWarningBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                EncounterWarningSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningSubcontractorException.MSG,
                    err_code=EncounterWarningSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(EncounterWarningBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="EncounterWarning")
        
        # --- Send the work product to the caller. ---#
        model = EncounterWarning(
            id=id,
            victim=fingerprint.victim,
            location=fingerprint.location,
            attacker_reward=fingerprint.attacker_reward,
            attacker_maneuver=fingerprint.attacker_maneuver,
        )
        return BuildResult.success(model)