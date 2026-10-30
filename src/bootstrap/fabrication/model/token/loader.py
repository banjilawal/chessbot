# src/bootstrap/fabrication/model/token/loader.py

"""
Module: bootstrap.fabrication.model.token.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Token, TokenBlueprint
from err import TokenBuildLoaderException, TokenBuildRequestNullException
from exchange import TokenBuildRequest, TokenValidationRequest, TokenValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class TokenBuildLoader(ModelBuildLoader[Token]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Token build process by preparing a TokenBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: TokenValidationServer

    Provides:
        -   def execute(request: TokenBuildRequest) -> BuildResult[TokenBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[TokenValidationServer]
        """
        super().__init__(validator=validator or TokenValidationService())
    
    @property
    def validator(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenBuildRequest) -> BuildResult[TokenBlueprint]:
        """
        Prepare a TokenBlueprint which guarantees a safe Token.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid TokenBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: TokenBuildRequest
        Returns:
            BuildResult[TokenBlueprint]
        Raises:
            TokenBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=TokenBuildRequest,
            null_exception=TokenBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildLoaderException.MSG,
                    err_code=TokenBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(TokenBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=TokenValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                TokenBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildLoaderException.MSG,
                    err_code=TokenBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(TokenBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)