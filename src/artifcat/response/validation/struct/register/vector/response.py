# src/artifact/response/validation/struct/register/vector/response.py

"""
Module: artifact.response.validation.struct.register.vector.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RegisterValidationResponse, ResponseState, ValidationResult
from exchange import Request, VectorRegisterValidationRequest
from domain import VectorRegister, VectorRegisterBlueprint
from transit import VectorRegisterCarrier


class VectorRegisterValidationResponse(
    RegisterValidationResponse[VectorRegisterValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a VectorRegisterValidation transaction.

    Attributes:
        request: VectorRegisterValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: VectorRegisterValidationRequest,
            ) -> ValidationResponse:

        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        RegisterValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: VectorRegisterValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: VectorRegisterValidationRequest
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
    def request(self) -> VectorRegisterValidationRequest:
        return cast(VectorRegisterValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[VectorRegister]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, VectorRegister)
        ):
            return None
        # --- Extract the register. ---#
        model = cast(VectorRegister, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[VectorRegisterBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, VectorRegisterBlueprint)
        ):
            return None
        # --- Extract the register. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> VectorRegisterValidationResponse:
        req = cast(VectorRegisterValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> VectorRegisterValidationResponse:
        req = cast(VectorRegisterValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[VectorRegisterCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(VectorRegisterCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier