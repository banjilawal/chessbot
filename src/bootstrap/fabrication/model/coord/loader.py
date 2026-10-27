# src/bootstrap/fabrication/model/coord/loader.py

"""
Module: bootstrap.fabrication.model.coord.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Coord, CoordBlueprint
from err import CoordBuildLoaderException, CoordBuildRequestNullException
from exchange import CoordBuildRequest, CoordValidationRequest, CoordValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class CoordBuildLoader(ModelBuildLoader[Coord]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Coord build process by preparing a CoordBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: CoordValidationServer

    Provides:
        -   def execute(request: CoordBuildRequest) -> BuildResult[CoordBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[CoordValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[CoordValidationServer]
        """
        super().__init__(validator=validator or CoordValidationService())
    
    @property
    def validator(self) -> CoordValidationService:
        return cast(CoordValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: CoordBuildRequest) -> BuildResult[CoordBlueprint]:
        """
        Prepare a CoordBlueprint which guarantees a safe Coord.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid CoordBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: CoordBuildRequest
        Returns:
            BuildResult[CoordBlueprint]
        Raises:
            CoordBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            item=request,
            target_model=CoordBuildRequest,
            null_exception=CoordBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CoordBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuildLoaderException.MSG,
                    err_code=CoordBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(CoordBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=CoordValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="CoordValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                CoordBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuildLoaderException.MSG,
                    err_code=CoordBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(CoordBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)