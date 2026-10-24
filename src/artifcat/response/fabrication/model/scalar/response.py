# src/artifact/response/fabrication/model/scalar/response.py

"""
Module: artifact.response.fabrication.model.scalar.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Scalar
from exchange import Request, ScalarBuildRequest
from transit import ScalarCarrier


class ScalarBuildResponse(ModelBuildResponse[ScalarBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a ScalarBuild transaction.

    Attributes:
        request: ScalarBuildRequest
        model: Optional[Scalar]
        carrier: Optional[ScalarCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> ScalarBuildResponse
        -   def failure(request: Request, exception: Exception) -> ScalarBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: ScalarBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: ScalarBuildRequest
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
    def request(self) -> ScalarBuildRequest:
        return cast(ScalarBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Scalar)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Scalar]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Scalar, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[ScalarCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(ScalarCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> ScalarBuildResponse:
        req = cast(ScalarBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ScalarBuildResponse:
        req = cast(ScalarBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )