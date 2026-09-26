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
from client import Request, ManeuverBuildRequest
from domain import Maneuver, ManeuverBlueprint
from transit import ManeuverCarrier


class ManeuverBuildResponse(ModelBuildResponse[Maneuver]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Maneuver build request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: BuildResult,
        request: ManeuverBuildRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[Maneuver]
        -   def valid_blueprint() -> Optional[ManeuverBlueprint]

        -   def success(
                    request: Request,
                    result: BuildResult[ManeuverCarrier],
            ) -> ManeuverBuildResponse

        -   def failure(
                    request: Request,
                    result: BuildResult[ManeuverCarrier],
                    exception: Exception,
            ) -> ManeuverBuildResponse
            
    Super Class:
        ModelBuildResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: BuildResult,
            request: ManeuverBuildRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult,
            request: ManeuverBuildRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ManeuverBuildRequest:
        return cast(ManeuverBuildRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Maneuver]:
        # Handle the case that the fabrication failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ManeuverCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ManeuverCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.is_carrying_model:
            return None
        # --- Extract the model. ---#
        model = cast(Maneuver, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Maneuver)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[ManeuverBlueprint]:
        # Handle the case that the fabrication failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ManeuverCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ManeuverCarrier)
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
                not isinstance(blueprint, ManeuverBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: BuildResult,
    ) -> ManeuverBuildResponse:
        
        # Downcast the request into a ManeuverBuildRequest.
        fabrication_request = cast(
            ManeuverBuildRequest,
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
    ) -> ManeuverBuildResponse:
        
        # Downcast the request into a ManeuverBuildRequest.
        fabrication_request = cast(
            ManeuverBuildRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=fabrication_request,
            state=ResponseState.FAILURE,
        )