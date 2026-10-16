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
        method = f"{self.__class__.__name__}.execute"
        
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=VectorBuildRequest,
            null_exception=VectorBuildRequestNullException(),
        )
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
        build_request = cast(VectorBuildRequest, priming.payload)
        blueprint_validation = self.validator.extract_blueprint(
            request=VectorValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="VectorValidationRequest")
            )
        )
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
        blueprint = cast(VectorBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)