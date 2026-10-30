# src/artifact/response/validation/context/vector/response.py

"""
Module: artifact.response.validation.context.vector.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ContextValidationResponse, ResponseState, ValidationResult
from exchange import Request, VectorContextValidationRequest
from domain import Vector, VectorBlueprint
from transit import VectorCarrier


class VectorContextValidationResponse(
    ContextValidationResponse[VectorContextValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a VectorValidation transaction.

    Attributes:
        request: VectorContextValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: VectorContextValidationRequest,
            ) -> ContextValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ContextValidationResponse

    Super Class:
        ContextValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: VectorContextValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: VectorContextValidationRequest
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
    def request(self) -> VectorContextValidationRequest:
        return cast(VectorContextValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Vector]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Vector)
        ):
            return None
        # --- Extract the context. ---#
        context = cast(Vector, carrier.entity)
        return context
    
    @property
    def valid_blueprint(self) -> Optional[VectorBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, VectorBlueprint)
        ):
            return None
        # --- Extract the context. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> VectorContextValidationResponse:
        req = cast(VectorContextValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> VectorContextValidationResponse:
        req = cast(VectorContextValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[VectorCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(VectorCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier