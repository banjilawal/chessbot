# src/client/artifact/response/fabrication/response.py

"""
Module: client.artifact.response.fabrication.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelBuildResponse, ResponseState, BuildResult
from client import Request, AttackBuildRequest
from domain import Encounter, AttackBlueprint
from transit import AttackCarrier


class AttackBuildResponse(ModelBuildResponse[Encounter]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Attack build request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: BuildResult,
        request: AttackBuildRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[Attack]
        -   def valid_blueprint() -> Optional[AttackBlueprint]

        -   def success(
                    request: Request,
                    result: BuildResult,
            ) -> AttackBuildResponse

        -   def failure(
                    request: Request,
                    result: BuildResult,
                    exception: Exception,
            ) -> AttackBuildResponse
            
    Super Class:
        ModelBuildResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: BuildResult,
            request: AttackBuildRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult,
            request: AttackBuildRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> AttackBuildRequest:
        return cast(AttackBuildRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Encounter]:
        # Handle the case that the fabrication failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(AttackCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, AttackCarrier)
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
    def valid_blueprint(self) -> Optional[AttackBlueprint]:
        # Handle the case that the fabrication failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(AttackCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, AttackCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.is_carrying_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, AttackBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: BuildResult,
    ) -> AttackBuildResponse:
        
        # Downcast the request into a AttackBuildRequest.
        fabrication_request = cast(
            AttackBuildRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=fabrication_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: BuildResult,
            exception: Exception,
    ) -> AttackBuildResponse:
        
        # Downcast the request into a AttackBuildRequest.
        fabrication_request = cast(
            AttackBuildRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=fabrication_request,
            state=ResponseState.FAILURE,
        )