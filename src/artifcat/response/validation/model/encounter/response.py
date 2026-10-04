# src/artifact/response/validation/model/encounter/response.py

"""
Module: artifact.response.validation.model.encounter.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from exchange import Request, EncounterValidationRequest
from domain import Encounter, EncounterBlueprint
from transit import EncounterCarrier


class EncounterValidationResponse(ModelValidationResponse[Encounter]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Encounter validation request-response cycle's data and state.

    Attributes:
        result: ValidationResult[EncounterCarrier],
        request: EncounterValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Encounter]
        -   def valid_blueprint() -> Optional[EncounterBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[EncounterCarrier],
            ) -> EncounterValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[EncounterCarrier],
                    exception: Exception,
            ) -> EncounterValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: EncounterValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: EncounterValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> EncounterValidationRequest:
        return cast(EncounterValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Encounter]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(EncounterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, EncounterCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Encounter, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Encounter)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[EncounterBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(EncounterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, EncounterCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.has_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, EncounterBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> EncounterValidationResponse:
        
        # Downcast the request into a EncounterValidationRequest.
        validation_request = cast(
            EncounterValidationRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=validation_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: ValidationResult,
            exception: Exception,
    ) -> EncounterValidationResponse:
        
        # Downcast the request into a EncounterValidationRequest.
        validation_request = cast(
            EncounterValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )