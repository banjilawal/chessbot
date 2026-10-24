# src/artifact/response/fabrication/model/coord/response.py

"""
Module: artifact.response.fabrication.model.coord.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Coord
from exchange import Request, CoordBuildRequest
from transit import CoordCarrier


class CoordBuildResponse(ModelBuildResponse[CoordBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a CoordBuild transaction.

    Attributes:
        request: CoordBuildRequest
        model: Optional[Coord]
        carrier: Optional[CoordCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> CoordBuildResponse
        -   def failure(request: Request, exception: Exception) -> CoordBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: CoordBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: CoordBuildRequest
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
    def request(self) -> CoordBuildRequest:
        return cast(CoordBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Coord)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Coord]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Coord, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[CoordCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(CoordCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> CoordBuildResponse:
        req = cast(CoordBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> CoordBuildResponse:
        req = cast(CoordBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )