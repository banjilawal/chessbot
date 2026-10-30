# src/artifact/response/validation/context/scalar/response.py

"""
Module: artifact.response.validation.context.scalar.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ContextValidationResponse, ResponseState, ValidationResult
from exchange import Request, ScalarContextValidationRequest
from domain import Scalar, ScalarBlueprint
from transit import ScalarCarrier


class ScalarContextValidationResponse(
    ContextValidationResponse[ScalarContextValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a ScalarValidation transaction.

    Attributes:
        request: ScalarContextValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: ScalarContextValidationRequest,
            ) -> ContextValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ContextValidationResponse

    Super Class:
        ContextValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: ScalarContextValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: ScalarContextValidationRequest
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
    def request(self) -> ScalarContextValidationRequest:
        return cast(ScalarContextValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Scalar]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Scalar)
        ):
            return None
        # --- Extract the context. ---#
        context = cast(Scalar, carrier.entity)
        return context
    
    @property
    def valid_blueprint(self) -> Optional[ScalarBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, ScalarBlueprint)
        ):
            return None
        # --- Extract the context. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> ScalarContextValidationResponse:
        req = cast(ScalarContextValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ScalarContextValidationResponse:
        req = cast(ScalarContextValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[ScalarCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(ScalarCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier