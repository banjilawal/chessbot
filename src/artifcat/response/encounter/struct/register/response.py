# src/artifact/response/encounter/struct/register/response.py

"""
Module: artifact.response.encounter.struct.register.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, EncounterResponse, EncounterResult
from domain import Register, RegisterBlueprint
from exchange import RegisterEncounterRequest, Request

T = TypeVar("T", bound="Register")

class RegisterEncounterResponse(EncounterResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Register's encounter request-response cycle's data and state.

    Attributes:
        request: EncounterRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_register() -> Optional[T]
        -   def valid_blueprint() -> Optional[RegisterBlueprint[T]]

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
            request: RegisterEncounterRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult,
            request: RegisterEncounterRequest[T]
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
    def request(self) -> RegisterEncounterRequest[T]:
        return cast(RegisterEncounterRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[RegisterBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: EncounterResult,
    ) -> RegisterEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            RegisterEncounterRequest[T],
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
    ) -> RegisterEncounterResponse:
        # Downcast the request into a EncounterRequest.
        encounter_request = cast(
            RegisterEncounterRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )
