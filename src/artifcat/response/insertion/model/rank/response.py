# src/artifact/response/insertion/model/rank/response.py

"""
Module: artifact.response.insertion.model.rank.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, RankInsertionRequest
from domain import Rank, RankBlueprint
from transit import RankCarrier


class RankInsertionResponse(ModelInsertionResponse[Rank]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Rank insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[RankCarrier],
        request: RankInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Rank]
        -   def valid_blueprint() -> Optional[RankBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[RankCarrier],
            ) -> RankInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[RankCarrier],
                    exception: Exception,
            ) -> RankInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: RankInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: RankInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> RankInsertionRequest:
        return cast(RankInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Rank]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(RankCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, RankCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Rank, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Rank)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[RankBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(RankCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, RankCarrier)
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
                not isinstance(blueprint, RankBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> RankInsertionResponse:
        
        # Downcast the request into a RankInsertionRequest.
        insertion_request = cast(
            RankInsertionRequest,
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
    ) -> RankInsertionResponse:
        
        # Downcast the request into a RankInsertionRequest.
        insertion_request = cast(
            RankInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )