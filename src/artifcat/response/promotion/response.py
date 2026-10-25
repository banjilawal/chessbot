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
from domain import Elevatable, PawnToken, Rank
from err import EmptyDependencyListException
from exchange import PromotionRequest


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
        -   def success(result: PromotionResult, request: T) -> PromotionResponse
        -   def failure(request: T, exception: Exception) -> PromotionResponse

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            request: PromotionRequest,
            exception: Optional[Exception],
            result: Optional[PromotionResult],
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
            isinstance(self.result, PromotionResult) and
            self.promoted_pawn is not None
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def promoted_pawn(self) -> Optional[PawnToken]:
        if (
                super().is_failure or
                not isinstance(self.result, PromotionResult)
        ):
            return None
        return self.result.promoted_pawn
    
    @property
    def promotion(self) -> Optional[Rank]:
        if self.promoted_pawn is None:
            return None
        rank = self.promoted_pawn.rank
        if not isinstance(rank, Elevatable):
            return None
        return rank
        
    @classmethod
    def success(cls, result: PromotionResult, request: Request) -> PromotionResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> PromotionResponse:
        return cls(
            request=request,
            exception=exception,
            state=ResponseState.FAILURE,
        )