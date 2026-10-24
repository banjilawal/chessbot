# src/artifact/response/validation/model/alert/response.py

"""
Module: artifact.response.validation.model.alert.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from exchange import Request, AlertValidationRequest
from domain import Alert, AlertBlueprint
from transit import AlertCarrier


class AlertValidationResponse(
    ModelValidationResponse[AlertValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a AlertValidation transaction.

    Attributes:
        request: AlertValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: AlertValidationRequest,
            ) -> ValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        ModelValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: AlertValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: AlertValidationRequest
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
    def request(self) -> AlertValidationRequest:
        return cast(AlertValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Alert]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Alert)
        ):
            return None
        # --- Extract the model. ---#
        model = cast(Alert, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[AlertBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, AlertBlueprint)
        ):
            return None
        # --- Extract the model. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> AlertValidationResponse:
        req = cast(AlertValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> AlertValidationResponse:
        req = cast(AlertValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[AlertCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(AlertCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier