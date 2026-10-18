# src/transit/route/fabrication/encounter/router.py

"""
Module: transit.route.fabrication.encounter.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import (
    EncounterWarningBlueprint, CheckmateEncounterBlueprint, KillEncounterBlueprint,
    Encounter, EncounterBlueprint, StalemateEncounterBlueprint
)
from err import (
    EncounterBlueprintNullException, MissingEncounterBuildRouteException,
    EncounterBuildRouterException
)
from fabrication import (
    EncounterWarningSubcontractor, CheckmateEncounterSubcontractor,
    BuildRouter, KillEncounterSubcontractor, StalemateEncounterSubcontractor
)
from util import LoggingLevelRouter


class EncounterBuildRouter(BuildRouter[Encounter]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes EncounterBlueprint subclasses to the appropriate assembler.

    Attributes:
        kill_subcontractor: KillEncounterSubcontractor
        warning_subcontractor: EncounterWarningSubcontractor
        checkmate_subcontractor: CheckmateEncounterSubcontractor
        stalemate_subcontractor: StalemateEncounterSubcontractor
        
    Provides:
            -   def execute(blueprint: EncounterBlueprint) -> BuildResult[Encounter]

    Super Class:
        BuildRouter
    """
    
    _kill_subcontractor: KillEncounterSubcontractor
    _warning_subcontractor: EncounterWarningSubcontractor
    _checkmate_subcontractor: CheckmateEncounterSubcontractor
    _stalemate_subcontractor: StalemateEncounterSubcontractor

    
    def __init__(
            self,
            kill_subcontractor: Optional[KillEncounterSubcontractor] | None = None,
            warning_subcontractor: Optional[EncounterWarningSubcontractor] | None = None,
            checkmate_subcontractor: Optional[CheckmateEncounterSubcontractor] | None = None,
            stalemate_subcontractor: Optional[CheckmateEncounterSubcontractor] | None = None,
    ):
        """
        Args:
            kill_subcontractor: Optional[KillEncounterSubcontractor]
            warning_subcontractor: Optional[EncounterWarningSubcontractor]
            checkmate_subcontractor: Optional[CheckmateEncounterSubcontractor]
            stalemate_subcontractor: Optional[CheckmateEncounterSubcontractor]
        """
        super().__init__()
        self._kill_subcontractor = kill_subcontractor or KillEncounterSubcontractor()
        self._warning_subcontractor = warning_subcontractor or EncounterWarningSubcontractor()
        self._checkmate_subcontractor = checkmate_subcontractor or CheckmateEncounterSubcontractor()
        self._stalemate_subcontractor = stalemate_subcontractor or StalemateEncounterSubcontractor()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: EncounterBlueprint) -> BuildResult[Encounter]:
        """
        Routes an EncounterBlueprint to a Subcontractor for construction.

        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                -   The blueprint is null or the wrong type.
                -   No subcontractor exists for the blueprint.
                -   The subcontractor fails.
            2.  Otherwise, cast the subcontract's product to an Encounter then send in the
                success result.
        Args:
             blueprint: Blueprint[Encounter]
        Returns:
            BuildResult[Encounter]
        Raises:
            EncounterBuildRouterException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the case that the router cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=EncounterBlueprint,
            null_exception=EncounterBlueprintNullException(),
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EncounterBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuildRouterException.MSG,
                    err_code=EncounterBuildRouterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Otherwise get the payload.
        fingerprint = cast(EncounterBlueprint, validation.payload)
        
        # Initialize the default failure result
        result = BuildResult.failure(
            MissingEncounterBuildRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=MissingEncounterBuildRouteException.MSG,
                err_code=MissingEncounterBuildRouteException.ERR_CODE,
            )
        )
        # --- Route to the appropriate encounter_build subcontractor. ---#
        if isinstance(fingerprint, KillEncounterBlueprint):
            result = self._kill_subcontractor.execute(fingerprint)
        if isinstance(fingerprint, CheckmateEncounterBlueprint):
            result = self._checkmate_subcontractor.execute( fingerprint)
        if isinstance(fingerprint, EncounterWarningBlueprint):
            result = self._warning_subcontractor.execute(fingerprint)
        if isinstance(fingerprint, StalemateEncounterBlueprint):
            result = self._stalemate_subcontractor.execute(fingerprint)
        
        # Handle the case that the subcontractor does make a product.
        if result.is_failure:
            # Handle the case that no route exists for the fingerprint.
            return BuildResult.failure(
                EncounterBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuildRouterException.MSG,
                    err_code=EncounterBuildRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        model = cast(Encounter, result.payload)
        return BuildResult.success(model)
        
        
        