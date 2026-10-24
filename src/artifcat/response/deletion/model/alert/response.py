# src/artifact/response/deletion/model/alert/response.py

"""
Module: artifact.response.deletion.model.alert.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelDeletionResponse, ResponseState, DeletionResult
from exchange import Request, AlertDeletionRequest
from domain import Alert, AlertBlueprint
from transit import AlertCarrier


class AlertDeletionResponse(ModelDeletionResponse[Alert]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Alert deletion request-response cycle's data and state.

    Attributes:
        result: DeletionResult[AlertCarrier],
        request: AlertDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Alert]
        -   def valid_blueprint() -> Optional[AlertBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[AlertCarrier],
            ) -> AlertDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[AlertCarrier],
                    exception: Exception,
            ) -> AlertDeletionResponse
            
    Super Class:
        ModelDeletionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: AlertDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: AlertDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> AlertDeletionRequest:
        return cast(AlertDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Alert]:
        # Handle the case that the deletion failed.
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
        # Handle the case that the deletion failed.
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
            result: DeletionResult,
    ) -> AlertDeletionResponse:
        
        # Downcast the request into a AlertDeletionRequest.
        deletion_request = cast(
            AlertDeletionRequest,
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
    ) -> AlertDeletionResponse:
        
        # Downcast the request into a AlertDeletionRequest.
        deletion_request = cast(
            AlertDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )