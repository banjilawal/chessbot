# src/artifact/response/insertion/model/alert/response.py

"""
Module: artifact.response.insertion.model.alert.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, AlertInsertionRequest
from domain import Alert, AlertBlueprint
from transit import AlertCarrier


class AlertInsertionResponse(ModelInsertionResponse[Alert]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Alert insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[AlertCarrier],
        request: AlertInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Alert]
        -   def valid_blueprint() -> Optional[AlertBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[AlertCarrier],
            ) -> AlertInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[AlertCarrier],
                    exception: Exception,
            ) -> AlertInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: AlertInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: AlertInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> AlertInsertionRequest:
        return cast(AlertInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Alert]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(AlertCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, AlertCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Alert, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Alert)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[AlertBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(AlertCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, AlertCarrier)
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
                not isinstance(blueprint, AlertBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> AlertInsertionResponse:
        
        # Downcast the request into a AlertInsertionRequest.
        insertion_request = cast(
            AlertInsertionRequest,
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
    ) -> AlertInsertionResponse:
        
        # Downcast the request into a AlertInsertionRequest.
        insertion_request = cast(
            AlertInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )