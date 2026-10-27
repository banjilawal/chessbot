# src/bootstrap/fabrication/model/path/loader.py

"""
Module: bootstrap.fabrication.model.path.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Path, PathBlueprint
from err import PathBuildLoaderException, PathBuildRequestNullException
from exchange import PathBuildRequest, PathValidationRequest, PathValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class PathBuildLoader(ModelBuildLoader[Path]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Path build process by preparing a PathBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: PathValidationServer

    Provides:
        -   def execute(request: PathBuildRequest) -> BuildResult[PathBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[PathValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[PathValidationServer]
        """
        super().__init__(validator=validator or PathValidationService())
    
    @property
    def validator(self) -> PathValidationService:
        return cast(PathValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: PathBuildRequest) -> BuildResult[PathBlueprint]:
        """
        Prepare a PathBlueprint which guarantees a safe Path.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid PathBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: PathBuildRequest
        Returns:
            BuildResult[PathBlueprint]
        Raises:
            PathBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            item=request,
            target_model=PathBuildRequest,
            null_exception=PathBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PathBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathBuildLoaderException.MSG,
                    err_code=PathBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(PathBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=PathValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="PathValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                PathBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathBuildLoaderException.MSG,
                    err_code=PathBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(PathBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)