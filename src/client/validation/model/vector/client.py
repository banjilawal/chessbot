# src/client/validation/model/vector/client.py

"""
Module: client.validation.model.vectorclient
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from client import ModelValidatorClient, VectorValidationRequest
from domain import Vector
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
    def submit(
            self,
            request: VectorValidationRequest
    ) -> ValidationResult[VectorCarrier]:
        """
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[VectorCarrier]
        Raises:
            ModelValidatorClientException
        """
        pass