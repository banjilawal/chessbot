# src/artifact/response/deletion/struct/chart/response.py

"""
Module: artifact.response.deletion.struct.chart.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, DeletionResponse, DeletionResult
from domain import Chart, ChartBlueprint
from exchange import ChartDeletionRequest, Request

T = TypeVar("T", bound="Chart")

class ChartDeletionResponse(DeletionResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Chart's deletion request-response cycle's data and state.

    Attributes:
        request: DeletionRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_chart() -> Optional[T]
        -   def valid_blueprint() -> Optional[ChartBlueprint[T]]

        -   def success(
                    request: Request,
                    result: DeletionResult[T],
            ) -> DeletionResponse[T]

        -   def failure(
                    request: Request,
                    result: DeletionResult[T],
                    exception: Exception,
            ) -> DeletionResponse[T]

    Super Class:
        DeletionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: ChartDeletionRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: ChartDeletionRequest[T]
            exception:Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> DeletionResult:
        return cast(DeletionResult, super().result)
        
    @property
    def request(self) -> ChartDeletionRequest[T]:
        return cast(ChartDeletionRequest[T], super().request)
    
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
            result: DeletionResult,
    ) -> ChartDeletionResponse:
        # Downcast the request into a DeletionRequest.
        deletion_request = cast(
            ChartDeletionRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=deletion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: DeletionResult,
            exception: Exception,
    ) -> ChartDeletionResponse:
        # Downcast the request into a DeletionRequest.
        deletion_request = cast(
            ChartDeletionRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )
