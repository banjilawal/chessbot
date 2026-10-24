# src/artifact/response/insertion/model/maneuver/response.py

"""
Module: artifact.response.insertion.model.maneuver.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, ManeuverInsertionRequest
from domain import Maneuver, ManeuverBlueprint
from transit import ManeuverCarrier


class ManeuverInsertionResponse(ModelInsertionResponse[Maneuver]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Maneuver insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[ManeuverCarrier],
        request: ManeuverInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Maneuver]
        -   def valid_blueprint() -> Optional[ManeuverBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[ManeuverCarrier],
            ) -> ManeuverInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[ManeuverCarrier],
                    exception: Exception,
            ) -> ManeuverInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: ManeuverInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: ManeuverInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ManeuverInsertionRequest:
        return cast(ManeuverInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Maneuver]:
        # Handle the case that the insertion failed.
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
        # Handle the case that the insertion failed.
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
            result: InsertionResult,
    ) -> ManeuverInsertionResponse:
        
        # Downcast the request into a ManeuverInsertionRequest.
        insertion_request = cast(
            ManeuverInsertionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=insertion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: InsertionResult,
            exception: Exception,
    ) -> ManeuverInsertionResponse:
        
        # Downcast the request into a ManeuverInsertionRequest.
        insertion_request = cast(
            ManeuverInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )