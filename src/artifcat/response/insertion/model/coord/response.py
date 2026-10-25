# src/artifact/response/insertion/model/coord/response.py

"""
Module: artifact.response.insertion.model.coord.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, CoordInsertionRequest
from domain import Coord, CoordBlueprint
from transit import CoordCarrier


class CoordInsertionResponse(ModelInsertionResponse[Coord]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Coord insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[CoordCarrier],
        request: CoordInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Coord]
        -   def valid_blueprint() -> Optional[CoordBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[CoordCarrier],
            ) -> CoordInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[CoordCarrier],
                    exception: Exception,
            ) -> CoordInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: CoordInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: CoordInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> CoordInsertionRequest:
        return cast(CoordInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Coord]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(CoordCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, CoordCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Coord, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Coord)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[CoordBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(CoordCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, CoordCarrier)
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
                not isinstance(blueprint, CoordBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> CoordInsertionResponse:
        
        # Downcast the request into a CoordInsertionRequest.
        insertion_request = cast(
            CoordInsertionRequest,
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
    ) -> CoordInsertionResponse:
        
        # Downcast the request into a CoordInsertionRequest.
        insertion_request = cast(
            CoordInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )