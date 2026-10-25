# src/artifact/response/promotion/response.py

"""
Module: artifact.response.promotion.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionResult, Response, ResponseState
from domain import PawnToken, Rank
from exchange import PromotionRequest, Request


class PromotionResponse(Response[PromotionResult]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a Promotion transaction.

    Attributes:
        request: PromotionRequest
        result: Optional[PromotionResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: PromotionResult, request: Request) -> PromotionResponse
        -   def failure(request: Request, exception: Exception) -> PromotionResponse

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            request: PromotionRequest,
            exception: Optional[Exception] | None = None,
            result: Optional[PromotionResult] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: PromotionRequest
            exception: Optional[Exception]
            result: Optional[PromotionResult]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[PromotionResult]:
        return cast(PromotionResult, super().result)
        
    @property
    def request(self) -> PromotionRequest:
        return cast(PromotionRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            isinstance(self.request, PromotionRequest) and
            isinstance(self.result, PromotionResult)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def promoted_pawn(self) -> Optional[PawnToken]:
        result = self.result
        if result is None or result.is_failure:
            return None
        pawn_token = cast(PawnToken, result.payload)
        return pawn_token
    
    @property
    def promotion(self) -> Optional[Rank]:
        pawn_token = self.promoted_pawn
        if pawn_token is None:
            return None
        return pawn_token.rank
        
    @classmethod
    def success(cls, result: PromotionResult, request: Request) -> PromotionResponse:
        req = cast(PromotionRequest, request)
        return cls(
            result=result,
            request=req,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> PromotionResponse:
        req = cast(PromotionRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )