# src/bootstrap/fabrication/model/team/loader.py

"""
Module: bootstrap.fabrication.model.team.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Team, TeamBlueprint
from err import TeamBuildLoaderException, TeamBuildRequestNullException
from exchange import TeamBuildRequest, TeamValidationRequest, TeamValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class TeamBuildLoader(ModelBuildLoader[Team]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Team build process by preparing a TeamBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: TeamValidationServer

    Provides:
        -   def execute(request: TeamBuildRequest) -> BuildResult[TeamBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[TeamValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[TeamValidationServer]
        """
        super().__init__(validator=validator or TeamValidationService())
    
    @property
    def validator(self) -> TeamValidationService:
        return cast(TeamValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: TeamBuildRequest) -> BuildResult[TeamBlueprint]:
        """
        Prepare a TeamBlueprint which guarantees a safe Team.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid TeamBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: TeamBuildRequest
        Returns:
            BuildResult[TeamBlueprint]
        Raises:
            TeamBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            item=request,
            target_model=TeamBuildRequest,
            null_exception=TeamBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildLoaderException.MSG,
                    err_code=TeamBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(TeamBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=TeamValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="TeamValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                TeamBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildLoaderException.MSG,
                    err_code=TeamBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(TeamBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)