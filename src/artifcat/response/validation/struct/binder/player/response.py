# src/artifact/response/validation/struct/binder/player/response.py

"""
Module: artifact.response.validation.struct.binder.player.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BinderValidationResponse, ResponseState, ValidationResult
from exchange import Request, PlayerBinderValidationRequest
from domain import PlayerBinder, PlayerBinderBlueprint
from transit import PlayerBinderCarrier


class PlayerBinderValidationResponse(
    BinderValidationResponse[PlayerBinder]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a PlayerBinder validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult[PlayerBinderCarrier]
        request: PlayerBinderValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Player]
        -   def valid_blueprint() -> Optional[PlayerBinderBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[PlayerBinderCarrier],
            ) -> PlayerBinderValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[PlayerBinderCarrier],
                    exception: Exception,
            ) -> PlayerBinderValidationResponse
            
    Super Class:
        BinderValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: PlayerBinderValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult[PlayerBinderCarrier]
            request: PlayerBinderValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> PlayerBinderValidationRequest:
        return cast(PlayerBinderValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[PlayerBinder]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PlayerBinderCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PlayerBinderCarrier)
        ):
            return None
        # Handle the case that there is no binder in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the binder. ---#
        binder = cast(PlayerBinder, carrier.entity)
        # Handle the case that the binder is null or the wrong type.
        if (
                binder is None or
                not isinstance(binder, PlayerBinder)
        ):
            return None
        # Finally send the success result.
        return binder
    
    @property
    def valid_blueprint(self) -> Optional[PlayerBinderBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PlayerBinderCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PlayerBinderCarrier)
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
                not isinstance(blueprint, PlayerBinderBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> PlayerBinderValidationResponse:
        # Downcast the request into a PlayerBinderValidationRequest.
        validation_request = cast(
            PlayerBinderValidationRequest,
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
    ) -> PlayerBinderValidationResponse:
        # Downcast the request into a PlayerBinderValidationRequest.
        validation_request = cast(
            PlayerBinderValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )