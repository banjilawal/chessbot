# src/artifact/response/encounter/struct/binder/response.py

"""
Module: artifact.response.encounter.struct.binder.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, EncounterResponse, EncounterResult
from domain import Binder, BinderBlueprint
from exchange import BinderEncounterRequest, Request

T = TypeVar("T", bound="Binder")

class BinderEncounterResponse(EncounterResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Binder's encounter request-response cycle's data and state.

    Attributes:
        request: EncounterRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_binder() -> Optional[T]
        -   def valid_blueprint() -> Optional[BinderBlueprint[T]]

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
            request: BinderEncounterRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult,
            request: BinderEncounterRequest[T]
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
    def request(self) -> BinderEncounterRequest[T]:
        return cast(BinderEncounterRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[BinderBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: EncounterResult,
    ) -> BinderEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            BinderEncounterRequest[T],
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
    ) -> BinderEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            BinderEncounterRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )
