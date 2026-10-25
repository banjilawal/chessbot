# src/artifact/response/search/model/path/response.py

"""
Module: artifact.response.search.model.path.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, PathSearchRequest
from domain import Path, PathBlueprint
from transit import PathCarrier


class PathSearchResponse(ModelSearchResponse[Path]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Path search request-response cycle's data and state.

    Attributes:
        result: SearchResult[PathCarrier],
        request: PathSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Path]
        -   def valid_blueprint() -> Optional[PathBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[PathCarrier],
            ) -> PathSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[PathCarrier],
                    exception: Exception,
            ) -> PathSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: PathSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: PathSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> PathSearchRequest:
        return cast(PathSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Path]:
        # Handle the case that the search failed.
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
        # Handle the case that the search failed.
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
            result: SearchResult,
    ) -> PathSearchResponse:
        
        # Downcast the request into a PathSearchRequest.
        search_request = cast(
            PathSearchRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=search_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: SearchResult,
            exception: Exception,
    ) -> PathSearchResponse:
        
        # Downcast the request into a PathSearchRequest.
        search_request = cast(
            PathSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )