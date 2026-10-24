# src/artifact/response/validation/model/vector/response.py

"""
Module: artifact.response.validation.model.vector.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from exchange import Request, VectorValidationRequest
from domain import Vector, VectorBlueprint
from transit import VectorCarrier


class VectorValidationResponse(ModelValidationResponse[VectorValidationRequest]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Vector validation request-response cycle's data and state.

    Attributes:
        result: ValidationResult[VectorCarrier],
        request: VectorValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Vector]
        -   def valid_blueprint() -> Optional[VectorBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[VectorCarrier],
            ) -> VectorValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[VectorCarrier],
                    exception: Exception,
            ) -> VectorValidationResponse
            
    Super Class:
        ModelValidationResponse
    """
    def __init__(
            self,
            state: ResponseState,
            request: VectorValidationRequest,
            result: Optional[ValidationResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: VectorValidationRequest
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
    def request(self) -> VectorValidationRequest:
        return cast(VectorValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Vector]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_model or
                carrier.entity is None or
                not isinstance(carrier.entity, Vector)
        ):
            return None
        # --- Extract the model. ---#
        model = cast(Vector, carrier.entity)
        return model
    
    @property
    def valid_blueprint(self) -> Optional[VectorBlueprint]:
        carrier = self.carrier
        if (
                carrier is None or
                not carrier.has_blueprint or
                carrier.entity is None or
                not isinstance(carrier.entity, VectorBlueprint)
        ):
            return None
        # --- Extract the model. ---#
        blueprint = carrier.extract_blueprint()
        return blueprint
    
    @classmethod
    def success(
            cls,
            result: ValidationResult,
            request: VectorValidationRequest,
    ) -> VectorValidationResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: VectorValidationRequest,
            exception: Exception,
    ) -> VectorValidationResponse:
        return cls(
            request=request,
            exception=exception,
            state=ResponseState.FAILURE,
        )
    
    @property
    def carrier(self) -> Optional[VectorCarrier]:
        result = self.result
        if (
                result is None or
                not isinstance(result, ValidationResult)
        ):
            return None
        carrier = cast(VectorCarrier, result.payload)
        if carrier is None or carrier.is_empty:
            return None
        return carrier