# src/artifact/response/validation/struct/register/coord/response.py

"""
Module: artifact.response.validation.struct.register.coord.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RegisterValidationResponse, ResponseState, ValidationResult
from exchange import Request, CoordRegisterValidationRequest
from domain import CoordRegister, CoordRegisterBlueprint
from transit import CoordRegisterCarrier


class CoordRegisterValidationResponse(
    RegisterValidationResponse[CoordRegisterValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a CoordRegisterValidation transaction.

    Attributes:
        request: CoordRegisterValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: CoordRegisterValidationRequest,
            ) -> ValidationResponse:

        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        RegisterValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: CoordRegisterValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: CoordRegisterValidationRequest
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
    def request(self) -> CoordRegisterValidationRequest:
        return cast(CoordRegisterValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[CoordRegister]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, CoordRegister)
        ):
            return None
        # --- Extract the register. ---#
        model = cast(CoordRegister, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[CoordRegisterBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, CoordRegisterBlueprint)
        ):
            return None
        # --- Extract the register. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> CoordRegisterValidationResponse:
        req = cast(CoordRegisterValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> CoordRegisterValidationResponse:
        req = cast(CoordRegisterValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[CoordRegisterCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(CoordRegisterCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier