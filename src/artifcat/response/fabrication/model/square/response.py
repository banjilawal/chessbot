# src/artifact/response/fabrication/model/square/response.py

"""
Module: artifact.response.fabrication.model.square.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Square
from exchange import Request, SquareBuildRequest
from transit import SquareCarrier


class SquareBuildResponse(ModelBuildResponse[SquareBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a SquareBuild transaction.

    Attributes:
        request: SquareBuildRequest
        model: Optional[Square]
        carrier: Optional[SquareCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> SquareBuildResponse
        -   def failure(request: Request, exception: Exception) -> SquareBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: SquareBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: SquareBuildRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[BuildResult]:
        return cast(BuildResult, super().result)
        
    @property
    def request(self) -> SquareBuildRequest:
        return cast(SquareBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Square)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Square]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Square, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[SquareCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(SquareCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> SquareBuildResponse:
        req = cast(SquareBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> SquareBuildResponse:
        req = cast(SquareBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )