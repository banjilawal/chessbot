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
from client import Request, ManeuverValidationRequest
from domain import Maneuver, ManeuverBlueprint
from transit import ManeuverCarrier


class ManeuverValidationResponse(ModelValidationResponse[Maneuver]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Maneuver validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult,
        request: ManeuverValidationRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[Maneuver]
        -   def valid_blueprint() -> Optional[ManeuverBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[ManeuverCarrier],
            ) -> ManeuverValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[ManeuverCarrier],
                    exception: Exception,
            ) -> ManeuverValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: ManeuverValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: ManeuverValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ManeuverValidationRequest:
        return cast(ManeuverValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Maneuver]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ManeuverCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ManeuverCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Maneuver, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Maneuver)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[ManeuverBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ManeuverCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ManeuverCarrier)
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
                not isinstance(blueprint, ManeuverBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> ManeuverValidationResponse:
        
        # Downcast the request into a ManeuverValidationRequest.
        validation_request = cast(
            ManeuverValidationRequest,
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
    ) -> ManeuverValidationResponse:
        
        # Downcast the request into a ManeuverValidationRequest.
        validation_request = cast(
            ManeuverValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )