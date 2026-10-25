# src/artifact/response/insertion/struct/chart/response.py

"""
Module: artifact.response.insertion.struct.chart.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, InsertionResponse, InsertionResult
from domain import Chart, ChartBlueprint
from exchange import ChartInsertionRequest, Request

T = TypeVar("T", bound="Chart")

class ChartInsertionResponse(InsertionResponse[T], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Chart's insertion request-response cycle's data and state.

    Attributes:
        request: InsertionRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_chart() -> Optional[T]
        -   def valid_blueprint() -> Optional[ChartBlueprint[T]]

        -   def success(
                    request: Request,
                    result: InsertionResult[T],
            ) -> InsertionResponse[T]

        -   def failure(
                    request: Request,
                    result: InsertionResult[T],
                    exception: Exception,
            ) -> InsertionResponse[T]

    Super Class:
        InsertionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: ChartInsertionRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: ChartInsertionRequest[T]
            exception:Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> InsertionResult:
        return cast(InsertionResult, super().result)
        
    @property
    def request(self) -> ChartInsertionRequest[T]:
        return cast(ChartInsertionRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[ChartBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> ChartInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            ChartInsertionRequest[T],
            request
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
    ) -> ChartInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            ChartInsertionRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )
