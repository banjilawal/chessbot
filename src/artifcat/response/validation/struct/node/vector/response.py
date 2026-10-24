# src/artifact/response/validation/struct/node/vector/response.py

"""
Module: artifact.response.validation.struct.node.vector.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import NodeValidationResponse, ResponseState, ValidationResult
from exchange import Request, VectorNodeValidationRequest
from domain import VectorNode, VectorNodeBlueprint
from transit import VectorNodeCarrier


class VectorNodeValidationResponse(
    NodeValidationResponse[VectorNodeValidationRequest]
):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a VectorNodeValidation transaction.

    Attributes:
        request: VectorNodeValidationRequest
        result: Optional[ValidationResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(
                    result: ValidationResult,
                    request: VectorNodeValidationRequest,
            ) -> ValidationResponse:

        -   def failure(request: ValidationResult, exception: Exception) -> ValidationResponse

    Super Class:
        NodeValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: VectorNodeValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: VectorNodeValidationRequest
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
    def request(self) -> VectorNodeValidationRequest:
        return cast(VectorNodeValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[VectorNode]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, VectorNode)
        ):
            return None
        # --- Extract the node. ---#
        model = cast(VectorNode, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[VectorNodeBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, VectorNodeBlueprint)
        ):
            return None
        # --- Extract the node. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> VectorNodeValidationResponse:
        req = cast(VectorNodeValidationRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> VectorNodeValidationResponse:
        req = cast(VectorNodeValidationRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[VectorNodeCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(VectorNodeCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier