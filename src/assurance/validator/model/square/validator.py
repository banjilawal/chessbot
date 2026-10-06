# src/assurance/validator/model/square/assurance/validator/model.py

"""
Module: assurance.validator.model.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    ModelValidator, SquareEnvelopeProducer, SquareEnvelopeRouter, SquareLoader,
    SquareValidatorToolkit
)
from domain import Square
from err import SquareValidatorException
from transit import RootSquareEnvelope, SquareCarrier
from util import LoggingLevelRouter


class SquareValidator(ModelValidator[Square]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareCarrier is safe to use.

    Attributes:
        loader: SquareLoader
        envelope_router: SquareEnvelopeRouter
        envelope_producer: SquareEnvelopeProducer

    Provides:
        -   def execute(candidate: SquareValidationRequest) -> ValidationResult[SquareCarrier]:

    Super Class:
        ModelValidator
    """
    _envelope_router: SquareEnvelopeRouter
    _envelope_producer: SquareEnvelopeProducer

    
    
    def __init__(
            self,
            loader: Optional[SquareLoader] | None = None,
            envelope_router: Optional[SquareEnvelopeRouter] | None = None,
            envelope_producer: Optional[SquareEnvelopeProducer] | None = None,
    ):
        """
        Args:
            loader: Optional[SquareLoader]
            envelope_router: Optional[SquareEnvelopeRouter]
            envelope_producer: Optional[SquareEnvelopeProducer]
        """
        super().__init__(loader=loader or SquareLoader())
        self._envelope_router = envelope_router or SquareEnvelopeRouter()
        self._envelope_producer = envelope_producer or SquareEnvelopeProducer()
        
    @property
    def loader(self) -> SquareLoader:
        return cast(SquareLoader, super().loader)
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareCarrier]:
        """
        Certify a SquareCarrier's payload is either a Square or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if either:
                    -   The Producer cannot generate a RootSquareEnvelope
                    -   A SquareCarrier could not be routed.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareCarrier]
        Raises:
            SquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self._envelope_producer.execute(candidate=candidate)
        if product.is_failure:
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=product.exception,
                )
            )
        envelope = cast(RootSquareEnvelope, product.payload)
        
        routing = self._envelope_router.execute(envelope=envelope)
        if routing.is_failure:
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=routing.exception,
                )
            )
        carrier = cast(SquareCarrier, routing.payload)
        return ValidationResult.success(carrier)