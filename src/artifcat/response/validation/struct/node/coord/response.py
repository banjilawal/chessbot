# src/artifact/response/validation/struct/node/coord/response.py

"""
Module: artifact.response.validation.struct.node.coord.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import NodeValidationResponse, ResponseState, ValidationResult
from exchange import Request, CoordNodeValidationRequest
from domain import CoordNode, CoordNodeBlueprint
from transit import CoordNodeCarrier


class CoordNodeValidationResponse(
    NodeValidationResponse[CoordNodeValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a CoordNodeValidation transaction.

    Attributes:
        request: CoordNodeValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: CoordNodeValidationRequest,
            ) -> ValidationResponse:

        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        NodeValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: CoordNodeValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: CoordNodeValidationRequest
            result: Optional[ValidationResult]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
    
    @property
    def request(self) -> CoordNodeValidationRequest:
        return cast(CoordNodeValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[CoordNode]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, CoordNode)
        ):
            return None
        # --- Extract the node. ---#
        model = cast(CoordNode, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[CoordNodeBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, CoordNodeBlueprint)
        ):
            return None
        # --- Extract the node. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> CoordNodeValidationResponse:
        req = cast(CoordNodeValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> CoordNodeValidationResponse:
        req = cast(CoordNodeValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[CoordNodeCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(CoordNodeCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier