# src/artifact/response/validation/model/path/response.py

"""
Module: artifact.response.validation.model.path.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from exchange import Request, PathValidationRequest
from domain import Path, PathBlueprint
from transit import PathCarrier


class PathValidationResponse(ModelValidationResponse[Path]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Path validation request-response cycle's data and state.

    Attributes:
        result: ValidationResult[PathCarrier],
        request: PathValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Path]
        -   def valid_blueprint() -> Optional[PathBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[PathCarrier],
            ) -> PathValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[PathCarrier],
                    exception: Exception,
            ) -> PathValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: PathValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: PathValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> PathValidationRequest:
        return cast(PathValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Path]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PathCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PathCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Path, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Path)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[PathBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PathCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PathCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.has_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, PathBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> PathValidationResponse:
        
        # Downcast the request into a PathValidationRequest.
        validation_request = cast(
            PathValidationRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=validation_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: ValidationResult,
            exception: Exception,
    ) -> PathValidationResponse:
        
        # Downcast the request into a PathValidationRequest.
        validation_request = cast(
            PathValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )