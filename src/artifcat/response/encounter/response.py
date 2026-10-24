# src/artifact/response/encounter/response.py

"""
Module: artifact.response.encounter.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, EncounterResult
from domain import Blueprint
from exchange import Request, EncounterRequest

T = TypeVar("T",)

class EncounterResponse(Response[EncounterResult], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a encounter request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: EncounterResult
        request: EncounterRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

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
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: EncounterResult,
            request: EncounterRequest[T],
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult
            request: EncounterRequest[T]
            exception: Optional[Exception]
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
    def request(self) -> EncounterRequest[T]:
        return cast(EncounterRequest[T], super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            (
                self.valid_model is not None or
                self.valid_blueprint is not None
            )
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[Blueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: EncounterResult,
    ) -> EncounterResponse[T]:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            EncounterRequest[T],
            request,
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
    ) -> EncounterResponse[T]:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            EncounterRequest[T],
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )