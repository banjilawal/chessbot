# src/assurance/validator/context/square/validator.py

"""
Module: assurance.validator.context.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import SquareEnvelopeProducer, ValidationFactory
from domain import Square
from err import SquareValidatorException
from transit import SquareCarrier, SquareEnvelopeRouter, RootSquareEnvelope
from util import LoggingLevelRouter


class SquareValidator(ValidationFactory[Square]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an SquareCarrier is safe to use.

    Attributes:
        router: Optional[SquareValidationRouter]
        producer: Optional[SquareEnvelopeProducer]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[SquareCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            router: Optional[SquareEnvelopeRouter] | None = None,
            producer: Optional[SquareEnvelopeProducer] | None = None,
    ):
        """
        Args:
            router: Optional[SquareValidationRouter]
            producer: Optional[SquareEnvelopeProducer]
        """
        super().__init__(
            router=router or SquareEnvelopeRouter(),
            producer=producer or SquareEnvelopeProducer(),
        )
    
    @property
    def router(self) -> SquareEnvelopeRouter:
        return cast(SquareEnvelopeRouter, super().router)
    
    @property
    def producer(self) -> SquareEnvelopeProducer:
        return cast(SquareEnvelopeProducer, super().producer)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[SquareCarrier]:
        """
        Assure a candidate is a safe SquareCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Router fails.
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The producer does not return a product
            2.  Otherwise, send an SquareCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareCarrier]
        Raises:
            SquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self.producer.execute(item=candidate)
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
        
        validation = self.router.execute(envelope=envelope)
        if validation.is_failure:
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        carrier = cast(SquareCarrier, validation.payload)
        return ValidationResult.success(carrier)
    