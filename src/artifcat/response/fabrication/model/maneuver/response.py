# src/artifact/response/fabrication/model/maneuver/response.py

"""
Module: artifact.response.fabrication.model.maneuver.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Maneuver
from exchange import Request, ManeuverBuildRequest
from transit import ManeuverCarrier


class ManeuverBuildResponse(ModelBuildResponse[ManeuverBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a ManeuverBuild transaction.

    Attributes:
        request: ManeuverBuildRequest
        model: Optional[Maneuver]
        carrier: Optional[ManeuverCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> ManeuverBuildResponse
        -   def failure(request: Request, exception: Exception) -> ManeuverBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: ManeuverBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: ManeuverBuildRequest
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
    def request(self) -> ManeuverBuildRequest:
        return cast(ManeuverBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Maneuver)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Maneuver]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Maneuver, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[ManeuverCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(ManeuverCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> ManeuverBuildResponse:
        req = cast(ManeuverBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ManeuverBuildResponse:
        req = cast(ManeuverBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )