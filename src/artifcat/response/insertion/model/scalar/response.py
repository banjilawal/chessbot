# src/artifact/response/insertion/model/scalar/response.py

"""
Module: artifact.response.insertion.model.scalar.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, ScalarInsertionRequest
from domain import Scalar, ScalarBlueprint
from transit import ScalarCarrier


class ScalarInsertionResponse(ModelInsertionResponse[Scalar]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Scalar insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[ScalarCarrier],
        request: ScalarInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Scalar]
        -   def valid_blueprint() -> Optional[ScalarBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[ScalarCarrier],
            ) -> ScalarInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[ScalarCarrier],
                    exception: Exception,
            ) -> ScalarInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: ScalarInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: ScalarInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ScalarInsertionRequest:
        return cast(ScalarInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Scalar]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ScalarCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ScalarCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Scalar, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Scalar)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[ScalarBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ScalarCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ScalarCarrier)
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
                not isinstance(blueprint, ScalarBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> ScalarInsertionResponse:
        
        # Downcast the request into a ScalarInsertionRequest.
        insertion_request = cast(
            ScalarInsertionRequest,
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
    ) -> ScalarInsertionResponse:
        
        # Downcast the request into a ScalarInsertionRequest.
        insertion_request = cast(
            ScalarInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )