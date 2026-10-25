# src/artifact/response/insertion/struct/register/response.py

"""
Module: artifact.response.insertion.struct.register.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, InsertionResponse, InsertionResult
from domain import Register, RegisterBlueprint
from exchange import RegisterInsertionRequest, Request

T = TypeVar("T", bound="Register")

class RegisterInsertionResponse(InsertionResponse[T], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Register's insertion request-response cycle's data and state.

    Attributes:
        request: InsertionRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_register() -> Optional[T]
        -   def valid_blueprint() -> Optional[RegisterBlueprint[T]]

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
            request: RegisterInsertionRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: RegisterInsertionRequest[T]
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
    def request(self) -> RegisterInsertionRequest[T]:
        return cast(RegisterInsertionRequest[T], super().request)
    
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
            result: InsertionResult,
    ) -> RegisterInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            RegisterInsertionRequest[T],
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
    ) -> RegisterInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            RegisterInsertionRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )
