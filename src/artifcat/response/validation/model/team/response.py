# src/client/artifact/response/validation/response.py

"""
Module: client.artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from client import Request, TeamValidationRequest
from domain import Team, TeamBlueprint
from transit import TeamCarrier


class TeamValidationResponse(ModelValidationResponse[Team]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Team validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult,
        request: TeamValidationRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[Team]
        -   def valid_blueprint() -> Optional[TeamBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[TeamCarrier],
            ) -> TeamValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[TeamCarrier],
                    exception: Exception,
            ) -> TeamValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: TeamValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: TeamValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> TeamValidationRequest:
        return cast(TeamValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Team]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TeamCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TeamCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Team, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Team)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[TeamBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TeamCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TeamCarrier)
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
                not isinstance(blueprint, TeamBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> TeamValidationResponse:
        
        # Downcast the request into a TeamValidationRequest.
        validation_request = cast(
            TeamValidationRequest,
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
    ) -> TeamValidationResponse:
        
        # Downcast the request into a TeamValidationRequest.
        validation_request = cast(
            TeamValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )