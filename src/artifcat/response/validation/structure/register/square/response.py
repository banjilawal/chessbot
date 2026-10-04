# src/artifact/response/validation/struct/register/square/response.py

"""
Module: artifact.response.validation.struct.register.square.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RegisterValidationResponse, ResponseState, ValidationResult
from exchange import Request, SquareRegisterValidationRequest
from domain import SquareRegister, SquareRegisterBlueprint
from transit import SquareRegisterCarrier


class SquareRegisterValidationResponse(
    RegisterValidationResponse[SquareRegister]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a SquareRegister validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult[SquareRegisterCarrier]
        request: SquareRegisterValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Square]
        -   def valid_blueprint() -> Optional[SquareRegisterBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[SquareRegisterCarrier],
            ) -> SquareRegisterValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[SquareRegisterCarrier],
                    exception: Exception,
            ) -> SquareRegisterValidationResponse
            
    Super Class:
        RegisterValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: SquareRegisterValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult[SquareRegisterCarrier]
            request: SquareRegisterValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> SquareRegisterValidationRequest:
        return cast(SquareRegisterValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[SquareRegister]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(SquareRegisterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, SquareRegisterCarrier)
        ):
            return None
        # Handle the case that there is no register in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the register. ---#
        register = cast(SquareRegister, carrier.entity)
        # Handle the case that the register is null or the wrong type.
        if (
                register is None or
                not isinstance(register, SquareRegister)
        ):
            return None
        # Finally send the success result.
        return register
    
    @property
    def valid_blueprint(self) -> Optional[SquareRegisterBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(SquareRegisterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, SquareRegisterCarrier)
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
                not isinstance(blueprint, SquareRegisterBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> SquareRegisterValidationResponse:
        # Downcast the request into a SquareRegisterValidationRequest.
        validation_request = cast(
            SquareRegisterValidationRequest,
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
    ) -> SquareRegisterValidationResponse:
        # Downcast the request into a SquareRegisterValidationRequest.
        validation_request = cast(
            SquareRegisterValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )