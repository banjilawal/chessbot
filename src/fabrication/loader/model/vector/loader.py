# src/fabrication/loader/model/vector/loader.py

"""
Module: fabrication.loader.model.vector.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Vector, VectorBlueprint
from err import (
    VectorBuildLoaderException, VectorBuildRequestNullException, VectorCarrierEmptyException,
    VectorCarrierNullException
)
from exchange import VectorBuildRequest, VectorValidationRequest, VectorValidationServer
from fabrication import ModelBuildLoader
from transit import VectorCarrier
from util import IdFactory, LoggingLevelRouter


class VectorBuildLoader(ModelBuildLoader[Vector]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Prepare a VectorBlueprint if BuildRequest is correct.

    Attributes:
        validator: VectorValidationServer

    Provides:
        -   def execute(request: VectorBuildRequest) -> BuildResult[VectorBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[VectorValidationServer] | None = None,
    ):
        """
        Args:
            validator: Optional[VectorValidationServer]
        """
        super().__init__(validator=validator or VectorValidationServer())
    
    @property
    def validator(self) -> VectorValidationServer:
        return cast(VectorValidationServer, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorBuildRequest) -> BuildResult[VectorBlueprint]:
        """
        Prepare a VectorBlueprint which guarantees a safe Vector.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid VectorBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: VectorBuildRequest
        Returns:
            BuildResult[VectorBlueprint]
        Raises:
            VectorBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=VectorBuildRequest,
            null_exception=VectorBuildRequestNullException(),
        )
        # Send the exception chain on failure.
        if priming.is_failure:
            return BuildResult.failure(
                VectorBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuildLoaderException.MSG,
                    err_code=VectorBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(VectorBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=VectorValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="VectorValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                VectorBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuildLoaderException.MSG,
                    err_code=VectorBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(VectorBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)