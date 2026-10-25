# src/artifact/response/insertion/model/board/response.py

"""
Module: artifact.response.insertion.model.board.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, BoardInsertionRequest
from domain import Board, BoardBlueprint
from transit import BoardCarrier


class BoardInsertionResponse(ModelInsertionResponse[Board]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Board insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[BoardCarrier],
        request: BoardInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Board]
        -   def valid_blueprint() -> Optional[BoardBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[BoardCarrier],
            ) -> BoardInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[BoardCarrier],
                    exception: Exception,
            ) -> BoardInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: BoardInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: BoardInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> BoardInsertionRequest:
        return cast(BoardInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Board]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(BoardCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, BoardCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Board, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Board)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[BoardBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(BoardCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, BoardCarrier)
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
                not isinstance(blueprint, BoardBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> BoardInsertionResponse:
        
        # Downcast the request into a BoardInsertionRequest.
        insertion_request = cast(
            BoardInsertionRequest,
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
    ) -> BoardInsertionResponse:
        
        # Downcast the request into a BoardInsertionRequest.
        insertion_request = cast(
            BoardInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )