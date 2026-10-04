# src/artifact/response/fabrication/response.py

"""
Module: artifact.response.fabrication.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, BuildResponse, BuildResult
from exchange import ModelBuildRequest, Request
from domain import Model, ModelBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class ModelBuildResponse(BuildResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Model's build request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: BuildResult
        request: BuildRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[T]
        -   def valid_blueprint() -> Optional[ModelBlueprint[T]]

        -   def success(
                    request: Request,
                    result: BuildResult[T],
            ) -> BuildResponse[T]

        -   def failure(
                    request: Request,
                    result: BuildResult[T],
                    exception: Exception,
            ) -> BuildResponse[T]

    Super Class:
        BuildResponse
    """
    _carrier: Optional[ModelCarrier[T]]
    
    def __init__(
            self,
            state: ResponseState,
            result: BuildResult,
            request: ModelBuildRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult,
            request: ModelBuildRequest[T],
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> BuildResult:
        return cast(BuildResult, super().result)
        
    @property
    def request(self) -> ModelBuildRequest[T]:
        return cast(ModelBuildRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[ModelBlueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    def state(self) -> ResponseState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.result.is_success and
            self._state == ResponseState.SUCCESS
        )

    @property
    def is_consistent(self) -> bool:
        if self.is_failure:
            return False
        if (
                self.valid_model is None and
                self.valid_blueprint is None
        ):
            return False
        return True
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.is_consistent

    @property
    def is_failure(self) -> bool:
        return (
            self._result.is_failure and
            self._state == ResponseState.FAILURE
        )
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: BuildResult,
    ) -> ModelBuildResponse:
        # Downcast the request into a BuildRequest.
        fabrication_request = cast(
            ModelBuildRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=fabrication_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: BuildResult,
            exception: Exception,
    ) -> ModelBuildResponse:
        # Downcast the request into a BuildRequest.
        fabrication_request = cast(
            ModelBuildRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=fabrication_request,
            state=ResponseState.FAILURE,
        )
