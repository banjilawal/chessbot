# src/artifact/response/promotion/response.py

"""
Module: artifact.response.promotion.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Response, ResponseState, PromotionResult
from domain import PawnToken, Rank
from exchange import Request, PromotionRequest

class PromotionResponse(Response[PromotionResult]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a promotion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: PromotionResult
        request: PromotionRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

        -   def success(
                    request: Request,
                    result: PromotionResult,
            ) -> PromotionResponse

        -   def failure(
                    request: Request,
                    result: PromotionResult,
                    exception: Exception,
            ) -> PromotionResponse

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: PromotionResult,
            request: PromotionRequest,
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: PromotionResult
            request: PromotionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> PromotionResult:
        return cast(PromotionResult, super().result)
        
    @property
    def request(self) -> PromotionRequest:
        return cast(PromotionRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            self.promoted_pawn is not None and
            self.elevated_rank is not None
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def promoted_pawn(self) -> Optional[PawnToken]:
        if self.is_failure:
            return None
        pawn = cast(PawnToken, self.result.payload)
        return pawn
    
    @property
    def elevated_rank(self) -> Optional[Rank]:
        if self.promoted_pawn is None:
            return None
        pawn = self.promoted_pawn
        return pawn.rank
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: PromotionResult,
    ) -> PromotionResponse:
        # Downcast the request into a PromotionRequest.
        promotion_request = cast(
            PromotionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=promotion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: PromotionResult,
            exception: Exception,
    ) -> PromotionResponse:
        # Downcast the request into a PromotionRequest.
        promotion_request = cast(
            PromotionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=promotion_request,
            state=ResponseState.FAILURE,
        )