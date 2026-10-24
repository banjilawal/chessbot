# src/artifact/response/search/model/scalar/response.py

"""
Module: artifact.response.search.model.scalar.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, ScalarSearchRequest
from domain import Scalar, ScalarBlueprint
from transit import ScalarCarrier


class ScalarSearchResponse(ModelSearchResponse[Scalar]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Scalar search request-response cycle's data and state.

    Attributes:
        result: SearchResult[ScalarCarrier],
        request: ScalarSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Scalar]
        -   def valid_blueprint() -> Optional[ScalarBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[ScalarCarrier],
            ) -> ScalarSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[ScalarCarrier],
                    exception: Exception,
            ) -> ScalarSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: ScalarSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: ScalarSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ScalarSearchRequest:
        return cast(ScalarSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Scalar]:
        # Handle the case that the search failed.
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
        # Handle the case that the search failed.
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
            result: SearchResult,
    ) -> ScalarSearchResponse:
        
        # Downcast the request into a ScalarSearchRequest.
        search_request = cast(
            ScalarSearchRequest,
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
    ) -> ScalarSearchResponse:
        
        # Downcast the request into a ScalarSearchRequest.
        search_request = cast(
            ScalarSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )