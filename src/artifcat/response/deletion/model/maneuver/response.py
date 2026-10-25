# src/artifact/response/deletion/model/maneuver/response.py

"""
Module: artifact.response.deletion.model.maneuver.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelDeletionResponse, ResponseState, DeletionResult
from exchange import Request, ManeuverDeletionRequest
from domain import Maneuver, ManeuverBlueprint
from transit import ManeuverCarrier


class ManeuverDeletionResponse(ModelDeletionResponse[Maneuver]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Maneuver deletion request-response cycle's data and state.

    Attributes:
        result: DeletionResult[ManeuverCarrier],
        request: ManeuverDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Maneuver]
        -   def valid_blueprint() -> Optional[ManeuverBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[ManeuverCarrier],
            ) -> ManeuverDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[ManeuverCarrier],
                    exception: Exception,
            ) -> ManeuverDeletionResponse
            
    Super Class:
        ModelDeletionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: ManeuverDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: ManeuverDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ManeuverDeletionRequest:
        return cast(ManeuverDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Maneuver]:
        # Handle the case that the deletion failed.
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
        if not carrier.has_model:
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
        # Handle the case that the deletion failed.
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
        if not carrier.has_blueprint:
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
            result: DeletionResult,
    ) -> ManeuverDeletionResponse:
        
        # Downcast the request into a ManeuverDeletionRequest.
        deletion_request = cast(
            ManeuverDeletionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=deletion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: DeletionResult,
            exception: Exception,
    ) -> ManeuverDeletionResponse:
        
        # Downcast the request into a ManeuverDeletionRequest.
        deletion_request = cast(
            ManeuverDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )