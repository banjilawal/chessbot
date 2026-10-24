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
    RegisterValidationResponse[SquareRegisterValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a SquareRegisterValidation transaction.

    Attributes:
        request: SquareRegisterValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: SquareRegisterValidationRequest,
            ) -> ValidationResponse:

        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        RegisterValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: SquareRegisterValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: SquareRegisterValidationRequest
            result: Optional[ValidationResult]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
    
    @property
    def request(self) -> SquareRegisterValidationRequest:
        return cast(SquareRegisterValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[SquareRegister]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, SquareRegister)
        ):
            return None
        # --- Extract the register. ---#
        model = cast(SquareRegister, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[SquareRegisterBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, SquareRegisterBlueprint)
        ):
            return None
        # --- Extract the register. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> SquareRegisterValidationResponse:
        req = cast(SquareRegisterValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> SquareRegisterValidationResponse:
        req = cast(SquareRegisterValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[SquareRegisterCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(SquareRegisterCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier