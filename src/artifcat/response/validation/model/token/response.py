# src/artifact/response/validation/model/token/response.py

"""
Module: artifact.response.validation.model.token.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from exchange import Request, TokenValidationRequest
from domain import Token, TokenBlueprint
from transit import TokenCarrier


class TokenValidationResponse(
    ModelValidationResponse[TokenValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a TokenValidation transaction.

    Attributes:
        request: TokenValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: TokenValidationRequest,
            ) -> ValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        ModelValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: TokenValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: TokenValidationRequest
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
    def request(self) -> TokenValidationRequest:
        return cast(TokenValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Token]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Token)
        ):
            return None
        # --- Extract the model. ---#
        model = cast(Token, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[TokenBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, TokenBlueprint)
        ):
            return None
        # --- Extract the model. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> TokenValidationResponse:
        req = cast(TokenValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> TokenValidationResponse:
        req = cast(TokenValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[TokenCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(TokenCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier