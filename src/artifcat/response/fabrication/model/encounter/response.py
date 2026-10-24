# src/artifact/response/fabrication/model/encounter/response.py

"""
Module: artifact.response.fabrication.model.encounter.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Encounter
from exchange import Request, EncounterBuildRequest
from transit import EncounterCarrier


class EncounterBuildResponse(ModelBuildResponse[EncounterBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a EncounterBuild transaction.

    Attributes:
        request: EncounterBuildRequest
        model: Optional[Encounter]
        carrier: Optional[EncounterCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> EncounterBuildResponse
        -   def failure(request: Request, exception: Exception) -> EncounterBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: EncounterBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: EncounterBuildRequest
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
    def request(self) -> EncounterBuildRequest:
        return cast(EncounterBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Encounter)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Encounter]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Encounter, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[EncounterCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(EncounterCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> EncounterBuildResponse:
        req = cast(EncounterBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> EncounterBuildResponse:
        req = cast(EncounterBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )