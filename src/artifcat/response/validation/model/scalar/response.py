# src/client/artifact/response/validation/response.py

"""
Module: client.artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from client import Request, ScalarValidationRequest
from domain import Scalar, ScalarBlueprint
from transit import ScalarCarrier


class ScalarValidationResponse(ModelValidationResponse[Scalar]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Scalar validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult,
        request: ScalarValidationRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[Scalar]
        -   def valid_blueprint() -> Optional[ScalarBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[ScalarCarrier],
            ) -> ScalarValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[ScalarCarrier],
                    exception: Exception,
            ) -> ScalarValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: ScalarValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: ScalarValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ScalarValidationRequest:
        return cast(ScalarValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Scalar]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ScalarCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ScalarCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.is_carrying_model:
            return None
        # --- Extract the model. ---#
        model = cast(Scalar, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Scalar)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[ScalarBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ScalarCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ScalarCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.is_carrying_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, ScalarBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> ScalarValidationResponse:
        
        # Downcast the request into a ScalarValidationRequest.
        validation_request = cast(
            ScalarValidationRequest,
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
    ) -> ScalarValidationResponse:
        
        # Downcast the request into a ScalarValidationRequest.
        validation_request = cast(
            ScalarValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )