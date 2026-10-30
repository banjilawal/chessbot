# src/artifact/response/validation/context/maneuver/response.py

"""
Module: artifact.response.validation.context.maneuver.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ContextValidationResponse, ResponseState, ValidationResult
from exchange import Request, ManeuverContextValidationRequest
from domain import Maneuver, ManeuverBlueprint
from transit import ManeuverCarrier


class ManeuverContextValidationResponse(
    ContextValidationResponse[ManeuverContextValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a ManeuverValidation transaction.

    Attributes:
        request: ManeuverContextValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: ManeuverContextValidationRequest,
            ) -> ContextValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ContextValidationResponse

    Super Class:
        ContextValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: ManeuverContextValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: ManeuverContextValidationRequest
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
    def request(self) -> ManeuverContextValidationRequest:
        return cast(ManeuverContextValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Maneuver]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Maneuver)
        ):
            return None
        # --- Extract the context. ---#
        context = cast(Maneuver, carrier.entity)
        return context
    
    @property
    def valid_blueprint(self) -> Optional[ManeuverBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, ManeuverBlueprint)
        ):
            return None
        # --- Extract the context. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> ManeuverContextValidationResponse:
        req = cast(ManeuverContextValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ManeuverContextValidationResponse:
        req = cast(ManeuverContextValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[ManeuverCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(ManeuverCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier