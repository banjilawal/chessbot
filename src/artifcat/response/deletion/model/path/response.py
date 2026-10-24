# src/artifact/response/deletion/model/path/response.py

"""
Module: artifact.response.deletion.model.path.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelDeletionResponse, ResponseState, DeletionResult
from exchange import Request, PathDeletionRequest
from domain import Path, PathBlueprint
from transit import PathCarrier


class PathDeletionResponse(ModelDeletionResponse[Path]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Path deletion request-response cycle's data and state.

    Attributes:
        result: DeletionResult[PathCarrier],
        request: PathDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Path]
        -   def valid_blueprint() -> Optional[PathBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[PathCarrier],
            ) -> PathDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[PathCarrier],
                    exception: Exception,
            ) -> PathDeletionResponse
            
    Super Class:
        ModelDeletionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: PathDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: PathDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> PathDeletionRequest:
        return cast(PathDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Path]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PathCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PathCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Path, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Path)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[PathBlueprint]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PathCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PathCarrier)
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
                not isinstance(blueprint, PathBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: DeletionResult,
    ) -> PathDeletionResponse:
        
        # Downcast the request into a PathDeletionRequest.
        deletion_request = cast(
            PathDeletionRequest,
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
    ) -> PathDeletionResponse:
        
        # Downcast the request into a PathDeletionRequest.
        deletion_request = cast(
            PathDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )