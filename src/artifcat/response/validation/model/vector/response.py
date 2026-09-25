# src/client/artifact/response/validation/response.py

"""
Module: client.artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelValidationResponse, ResponseState, ValidationResult
from client.request import VectorValidationRequest
from domain import Vector, VectorBlueprint
from transit import VectorCarrier


class VectorValidationResponse(ModelValidationResponse[Vector]):
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: VectorValidationRequest,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: VectorValidationRequest,
        """
        super().__init__(state=state, result=result, request=request)
        
    @property
    def request(self) -> VectorValidationRequest:
        return cast(VectorValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Vector]:
        if self.result.is_failure:
            return None
        carrier = cast(VectorCarrier, self.result.payload)
        if (
                carrier is None or
                not isinstance(carrier, VectorCarrier)
        ): return None
        if not carrier.is_carrying_model:
            return None
        model = cast(Vector, carrier.entity)
        if (
            model is None or
            not isinstance(model, Vector)
        ):
            return None
        return model
    
    @property
    def valid_blueprint(self) -> Optional[VectorBlueprint]:
        if self.result.is_failure:
            return None
        carrier = cast(VectorCarrier, self.result.payload)
        if (
                carrier is None or
                not isinstance(carrier, VectorCarrier)
        ): return None
        if not carrier.is_carrying_blueprint:
            return None
        blueprint = carrier.extract_blueprint()
        if (
                blueprint is None or
                not isinstance(blueprint, VectorBlueprint)
        ):
            return None
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
            result: ValidationResult, 
            request: VectorValidationRequest,
    ) -> VectorValidationResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.FAILURE,
        )