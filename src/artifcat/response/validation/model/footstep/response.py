# src/artifact/response/validation/model/footstep/response.py

"""
Module: artifact.response.validation.model.footstep.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from exchange import Request, FootstepValidationRequest
from domain import Footstep, FootstepBlueprint
from transit import FootstepCarrier


class FootstepValidationResponse(
    ModelValidationResponse[Footstep]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Footstep validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult[FootstepCarrier]
        request: FootstepValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Coord]
        -   def valid_blueprint() -> Optional[FootstepBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[FootstepCarrier],
            ) -> FootstepValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[FootstepCarrier],
                    exception: Exception,
            ) -> FootstepValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: FootstepValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult[FootstepCarrier]
            request: FootstepValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> FootstepValidationRequest:
        return cast(FootstepValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Footstep]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(FootstepCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, FootstepCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Footstep, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
                model is None or
                not isinstance(model, Footstep)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[FootstepBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(FootstepCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, FootstepCarrier)
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
                not isinstance(blueprint, FootstepBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> FootstepValidationResponse:
        # Downcast the request into a FootstepValidationRequest.
        validation_request = cast(
            FootstepValidationRequest,
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
    ) -> FootstepValidationResponse:
        # Downcast the request into a FootstepValidationRequest.
        validation_request = cast(
            FootstepValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )