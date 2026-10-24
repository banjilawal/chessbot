# src/artifact/response/fabrication/model/footstep/response.py

"""
Module: artifact.response.fabrication.model.footstep.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Footstep
from exchange import Request, FootstepBuildRequest
from transit import FootstepCarrier


class FootstepBuildResponse(ModelBuildResponse[FootstepBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a FootstepBuild transaction.

    Attributes:
        request: FootstepBuildRequest
        model: Optional[Footstep]
        carrier: Optional[FootstepCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> FootstepBuildResponse
        -   def failure(request: Request, exception: Exception) -> FootstepBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: FootstepBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: FootstepBuildRequest
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
    def request(self) -> FootstepBuildRequest:
        return cast(FootstepBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Footstep)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Footstep]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Footstep, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[FootstepCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(FootstepCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> FootstepBuildResponse:
        req = cast(FootstepBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> FootstepBuildResponse:
        req = cast(FootstepBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )