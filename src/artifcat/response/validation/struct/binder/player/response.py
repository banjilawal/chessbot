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
    BinderValidationResponse[PlayerBinderValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a PlayerBinderValidation transaction.

    Attributes:
        request: PlayerBinderValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: PlayerBinderValidationRequest,
            ) -> ValidationResponse:

        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        BinderValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: PlayerBinderValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: PlayerBinderValidationRequest
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
    def request(self) -> PlayerBinderValidationRequest:
        return cast(PlayerBinderValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[PlayerBinder]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, PlayerBinder)
        ):
            return None
        # --- Extract the binder. ---#
        model = cast(PlayerBinder, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[PlayerBinderBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, PlayerBinderBlueprint)
        ):
            return None
        # --- Extract the binder. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> PlayerBinderValidationResponse:
        req = cast(PlayerBinderValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> PlayerBinderValidationResponse:
        req = cast(PlayerBinderValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[PlayerBinderCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(PlayerBinderCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier