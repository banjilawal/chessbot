# src/artifact/response/validation/context/encounter/response.py

"""
Module: artifact.response.validation.context.encounter.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ContextValidationResponse, ResponseState, ValidationResult
from exchange import Request, EncounterContextValidationRequest
from domain import Encounter, EncounterBlueprint
from transit import EncounterCarrier


class EncounterContextValidationResponse(
    ContextValidationResponse[EncounterContextValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a EncounterValidation transaction.

    Attributes:
        request: EncounterContextValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: EncounterContextValidationRequest,
            ) -> ContextValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ContextValidationResponse

    Super Class:
        ContextValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: EncounterContextValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: EncounterContextValidationRequest
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
    def request(self) -> EncounterContextValidationRequest:
        return cast(EncounterContextValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Encounter]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Encounter)
        ):
            return None
        # --- Extract the context. ---#
        context = cast(Encounter, carrier.entity)
        return context
    
    @property
    def valid_blueprint(self) -> Optional[EncounterBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, EncounterBlueprint)
        ):
            return None
        # --- Extract the context. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> EncounterContextValidationResponse:
        req = cast(EncounterContextValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> EncounterContextValidationResponse:
        req = cast(EncounterContextValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[EncounterCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(EncounterCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier