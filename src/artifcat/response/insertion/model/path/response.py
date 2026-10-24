# src/artifact/response/insertion/model/path/response.py

"""
Module: artifact.response.insertion.model.path.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, PathInsertionRequest
from domain import Path, PathBlueprint
from transit import PathCarrier


class PathInsertionResponse(ModelInsertionResponse[Path]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Path insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[PathCarrier],
        request: PathInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Path]
        -   def valid_blueprint() -> Optional[PathBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[PathCarrier],
            ) -> PathInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[PathCarrier],
                    exception: Exception,
            ) -> PathInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: PathInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: PathInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> PathInsertionRequest:
        return cast(PathInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Path]:
        # Handle the case that the insertion failed.
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
        # Handle the case that the insertion failed.
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
            result: InsertionResult,
    ) -> PathInsertionResponse:
        
        # Downcast the request into a PathInsertionRequest.
        insertion_request = cast(
            PathInsertionRequest,
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
    ) -> PathInsertionResponse:
        
        # Downcast the request into a PathInsertionRequest.
        insertion_request = cast(
            PathInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )