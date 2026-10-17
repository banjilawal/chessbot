# src/fabrication/contractor/model/encounter/combatant/contractor.py

"""
Module: fabrication.contractor.model.encounter.combatant.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import CombatantEncounter, CombatantEncounterBlueprint
from err import CombatantEncounterSubcontractorException, HomeSquareNullException, EncounterBlueprintNullException
from fabrication import EncounterSubcontractor
from util import IdFactory, LoggingLevelRouter

class CombatantEncounterSubcontractor(EncounterSubcontractor[CombatantEncounter]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Instantiate a concrete Encounter.

    Attributes:

    Provides:
            -   def execute(blueprint: CombatantEncounterBlueprint) -> BuildResult[CombatantEncounter]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CombatantEncounterBlueprint) -> BuildResult[CombatantEncounter]:
        """
        Routes a CombatantEncounterBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[CombatantEncounter]
        Returns:
            BuildResult[CombatantEncounter]
        Raises:
            CombatantEncounterSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=CombatantEncounterBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                CombatantEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantEncounterSubcontractorException.MSG,
                    err_code=CombatantEncounterSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(CombatantEncounterBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="CombatantEncounter")
        
        # Handle the case that the fingerprint does not contain a home_square.
        home_square = fingerprint.home_square
        if home_square is None:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CombatantEncounterSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantEncounterSubcontractorException.MSG,
                    err_code=CombatantEncounterSubcontractorException.ERR_CODE,
                    ex=HomeSquareNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeSquareNullException.MSG,
                        err_code=HomeSquareNullException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product to the caller. ---#
        model = CombatantEncounter(
            id=id,
            team=fingerprint.team,
            home_square=home_square,
            footstep=fingerprint.footstep,
            formation=fingerprint.formation,
        )
        return BuildResult.success(model)