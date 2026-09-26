# src/client/validation/model/vector/client.py

"""
Module: client.validation.model.vectorclient
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, VectorValidationResponse
from client import ModelValidatorClient, VectorValidationRequest
from domain import Vector
from err import VectorValidatorClientException
from transit import VectorCarrier, VectorValidationDispatcher
from util import LoggingLevelRouter


class VectorValidatorClient(ModelValidatorClient[Vector]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Vector validation Request-Response workflow.

    Attributes:
        dispatcher: VectorValidationDispatcher[T]

    Provides:
        -   def submit(request: VectorValidationRequest[T]) -> VectorValidationResponse[T]

    Super Class:
        ModelValidatorClient
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorValidationDispatcher:
        return cast(VectorValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def transmit(
            self,
            request: VectorValidationRequest
    ) -> VectorValidationResponse:
        """
        Args:
            request: VectorValidationRequest
        Result:
            VectorValidationResponse
        Raises:
            VectorValidatorClientException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorValidationResponse.failure(
                request=request,
                result=result,
                exception=VectorValidationClientException(
                    cls_mthd=mthd,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationClientException.MSG,
                    err_code=VectorValidationClientException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorCarrier, result.payload)
        return VectorValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )