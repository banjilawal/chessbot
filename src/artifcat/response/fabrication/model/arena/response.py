# src/artifact/response/fabrication/model/arena/response.py

"""
Module: artifact.response.fabrication.model.arena.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Arena
from exchange import Request, ArenaBuildRequest
from transit import ArenaCarrier


class ArenaBuildResponse(ModelBuildResponse[ArenaBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a ArenaBuild transaction.

    Attributes:
        request: ArenaBuildRequest
        model: Optional[Arena]
        carrier: Optional[ArenaCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> ArenaBuildResponse
        -   def failure(request: Request, exception: Exception) -> ArenaBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: ArenaBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: ArenaBuildRequest
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
    def request(self) -> ArenaBuildRequest:
        return cast(ArenaBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Arena)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Arena]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Arena, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[ArenaCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(ArenaCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> ArenaBuildResponse:
        req = cast(ArenaBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ArenaBuildResponse:
        req = cast(ArenaBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )