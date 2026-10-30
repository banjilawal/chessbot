# src/fabrication/builder/model/encounter/builder.py

"""
Module: fabrication.builder.model.encounter.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Encounter, EncounterBlueprint
from err import EncounterBuilderException
from exchange import EncounterBuildRequest
from fabrication import BuildFactory, EncounterBuildLoader
from transit import EncounterBuildRouter
from util import LoggingLevelRouter


class EncounterBuilder(BuildFactory[Encounter]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create different Encounter products from the different types of blueprints.

    Attributes:
       loader: EncounterBuildLoader
       router: EncounterBuildRouter

    Provides:
        -   def execute(blueprint: EncounterBlueprint) -> BuildResult[Encounter]

    Super Class:
        BuildFactory
    """
    
    def __init__(
            self,
            loader: Optional[EncounterBuildLoader] | None = None,
            router: Optional[EncounterBuildRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[EncounterBuildLoader]
            router: Optional[EncounterBuildRouter]
        """
        super().__init__(
            loader=loader or EncounterBuildLoader(),
            router=router or EncounterBuildRouter(),
        )
    
    @property
    def loader(self) -> EncounterBuildLoader:
        return cast(EncounterBuildLoader, super().loader)
    
    @property
    def router(self) -> EncounterBuildRouter:
        return cast(EncounterBuildRouter, super().router)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: EncounterBuildRequest) -> BuildResult[Encounter]:
        """
        Assemble a Encounter from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if either:
                -   the loader does not produce a blueprint.
                -   the router does not return a product from the blueprint.
            2.  Otherwise, cast the product as a Encounter then send in the success result.
        Args:
            request: EncounterBuildRequest
        Returns:
            BuildResult[Encounter]
        Raises:
            EncounterBuilderException
        """
        method = f"{self.__class__.__name__}"
        
       # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EncounterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuilderException.MSG,
                    err_code=EncounterBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(EncounterBlueprint, bootstrap.authorization_applicant)
        result = self.router.execute(blueprint)
        
        # Handle the case that a product is not routed back.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EncounterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuilderException.MSG,
                    err_code=EncounterBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Send the work product. ---#
        return BuildResult.success(cast(Encounter, result.authorization_applicant))