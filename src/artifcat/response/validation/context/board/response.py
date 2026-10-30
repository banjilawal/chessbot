# src/artifact/response/validation/context/board/response.py

"""
Module: artifact.response.validation.context.board.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ContextValidationResponse, ResponseState, ValidationResult
from exchange import Request, BoardContextValidationRequest
from domain import Board, BoardBlueprint
from transit import BoardCarrier


class BoardContextValidationResponse(
    ContextValidationResponse[BoardContextValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a BoardValidation transaction.

    Attributes:
        request: BoardContextValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: BoardContextValidationRequest,
            ) -> ContextValidationResponse:
            
        -   def failure(request: ValidationResult, exception: Exception) -> ContextValidationResponse

    Super Class:
        ContextValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: BoardContextValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: BoardContextValidationRequest
            result: Optional[ValidationResult]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def request(self) -> BoardContextValidationRequest:
        return cast(BoardContextValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Board]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Board)
        ):
            return None
        # --- Extract the context. ---#
        context = cast(Board, carrier.entity)
        return context
    
    @property
    def valid_blueprint(self) -> Optional[BoardBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, BoardBlueprint)
        ):
            return None
        # --- Extract the context. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> BoardContextValidationResponse:
        req = cast(BoardContextValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> BoardContextValidationResponse:
        req = cast(BoardContextValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[BoardCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(BoardCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier