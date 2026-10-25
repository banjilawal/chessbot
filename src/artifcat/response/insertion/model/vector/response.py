# src/artifact/response/insertion/model/vector/response.py

"""
Module: artifact.response.insertion.model.vector.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, VectorInsertionRequest
from domain import Vector, VectorBlueprint
from transit import VectorCarrier


class VectorInsertionResponse(ModelInsertionResponse[Vector]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Vector insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[VectorCarrier],
        request: VectorInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Vector]
        -   def valid_blueprint() -> Optional[VectorBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[VectorCarrier],
            ) -> VectorInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[VectorCarrier],
                    exception: Exception,
            ) -> VectorInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: VectorInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: VectorInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> VectorInsertionRequest:
        return cast(VectorInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Vector]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(VectorCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, VectorCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Vector, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Vector)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[VectorBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(VectorCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, VectorCarrier)
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
                not isinstance(blueprint, VectorBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> VectorInsertionResponse:
        
        # Downcast the request into a VectorInsertionRequest.
        insertion_request = cast(
            VectorInsertionRequest,
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
    ) -> VectorInsertionResponse:
        
        # Downcast the request into a VectorInsertionRequest.
        insertion_request = cast(
            VectorInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )