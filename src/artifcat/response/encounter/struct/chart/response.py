# src/artifact/response/encounter/struct/chart/response.py

"""
Module: artifact.response.encounter.struct.chart.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, EncounterResponse, EncounterResult
from domain import Chart, ChartBlueprint
from exchange import ChartEncounterRequest, Request

T = TypeVar("T", bound="Chart")

class ChartEncounterResponse(EncounterResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Chart's encounter request-response cycle's data and state.

    Attributes:
        request: EncounterRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_chart() -> Optional[T]
        -   def valid_blueprint() -> Optional[ChartBlueprint[T]]

        -   def success(
                    request: Request,
                    result: EncounterResult[T],
            ) -> EncounterResponse[T]

        -   def failure(
                    request: Request,
                    result: EncounterResult[T],
                    exception: Exception,
            ) -> EncounterResponse[T]

    Super Class:
        EncounterResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: EncounterResult,
            request: ChartEncounterRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult,
            request: ChartEncounterRequest[T]
            exception:Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> EncounterResult:
        return cast(EncounterResult, super().result)
        
    @property
    def request(self) -> ChartEncounterRequest[T]:
        return cast(ChartEncounterRequest[T], super().request)
    
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
            result: EncounterResult,
    ) -> ChartEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            ChartEncounterRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=encounter_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: EncounterResult,
            exception: Exception,
    ) -> ChartEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            ChartEncounterRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )
