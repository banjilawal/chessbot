# src/bootstrap/fabrication/model/square/loader.py

"""
Module: bootstrap.fabrication.model.square.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Square, SquareBlueprint
from err import SquareBuildLoaderException, SquareBuildRequestNullException
from exchange import SquareBuildRequest, SquareValidationRequest, SquareValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class SquareBuildLoader(ModelBuildLoader[Square]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Square build process by preparing a SquareBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: SquareValidationServer

    Provides:
        -   def execute(request: SquareBuildRequest) -> BuildResult[SquareBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[SquareValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[SquareValidationServer]
        """
        super().__init__(validator=validator or SquareValidationService())
    
    @property
    def validator(self) -> SquareValidationService:
        return cast(SquareValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: SquareBuildRequest) -> BuildResult[SquareBlueprint]:
        """
        Prepare a SquareBlueprint which guarantees a safe Square.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid SquareBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: SquareBuildRequest
        Returns:
            BuildResult[SquareBlueprint]
        Raises:
            SquareBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=SquareBuildRequest,
            null_exception=SquareBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildLoaderException.MSG,
                    err_code=SquareBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(SquareBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=SquareValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="SquareValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                SquareBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildLoaderException.MSG,
                    err_code=SquareBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(SquareBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)