# src/bootstrap/fabrication/model/scalar/loader.py

"""
Module: bootstrap.fabrication.model.scalar.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Scalar, ScalarBlueprint
from err import ScalarBuildLoaderException, ScalarBuildRequestNullException
from exchange import ScalarBuildRequest, ScalarValidationRequest, ScalarValidationServer
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class ScalarBuildLoader(ModelBuildLoader[Scalar]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Scalar build process by preparing a ScalarBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: ScalarValidationServer

    Provides:
        -   def execute(request: ScalarBuildRequest) -> BuildResult[ScalarBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[ScalarValidationServer] | None = None,
    ):
        """
        Args:
            validator: Optional[ScalarValidationServer]
        """
        super().__init__(validator=validator or ScalarValidationServer())
    
    @property
    def validator(self) -> ScalarValidationServer:
        return cast(ScalarValidationServer, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: ScalarBuildRequest) -> BuildResult[ScalarBlueprint]:
        """
        Prepare a ScalarBlueprint which guarantees a safe Scalar.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid ScalarBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: ScalarBuildRequest
        Returns:
            BuildResult[ScalarBlueprint]
        Raises:
            ScalarBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            item=request,
            target_model=ScalarBuildRequest,
            null_exception=ScalarBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildLoaderException.MSG,
                    err_code=ScalarBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(ScalarBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=ScalarValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="ScalarValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                ScalarBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildLoaderException.MSG,
                    err_code=ScalarBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(ScalarBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)