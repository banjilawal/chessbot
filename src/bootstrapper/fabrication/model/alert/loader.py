# src/bootstrap/fabrication/model/alert/loader.py

"""
Module: bootstrap.fabrication.model.alert.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Alert, AlertBlueprint
from err import AlertBuildLoaderException, AlertBuildRequestNullException
from exchange import AlertBuildRequest, AlertValidationRequest, AlertValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class AlertBuildLoader(ModelBuildLoader[Alert]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Initialize the Alert build process by preparing a AlertBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: AlertValidationServer

    Provides:
        -   def execute(request: AlertBuildRequest) -> BuildResult[AlertBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[AlertValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[AlertValidationServer]
        """
        super().__init__(validator=validator or AlertValidationService())
    
    @property
    def validator(self) -> AlertValidationService:
        return cast(AlertValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: AlertBuildRequest) -> BuildResult[AlertBlueprint]:
        """
        Prepare a AlertBlueprint which guarantees a safe Alert.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid AlertBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: AlertBuildRequest
        Returns:
            BuildResult[AlertBlueprint]
        Raises:
            AlertBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=AlertBuildRequest,
            null_exception=AlertBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AlertBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertBuildLoaderException.MSG,
                    err_code=AlertBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(AlertBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=AlertValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="AlertValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                AlertBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertBuildLoaderException.MSG,
                    err_code=AlertBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(AlertBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)