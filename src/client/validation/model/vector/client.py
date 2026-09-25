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
        - Client

    Responsibilities:
        1.  Submit a request to a ModelValidationDispatcher

    Attributes:
        dispatcher: VectorValidationDispatcher
        
    Provides:
        -   def submit(
                    self,
                    request: VectorValidationRequest
            ) -> ValidationResult[VectorCarrier]:

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
        if result.is_failure:
            return ValidationResult.failure(
                VectorValidatorClientException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorClientException.MSG,
                    err_code=VectorValidatorClientException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(VectorCarrier, result.payload)
        return ValidationResult.success(carrier)