# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import TokenEnvelopeProducer, ValidationFactory
from domain import Token
from err import TokenValidatorException
from transit import TokenCarrier, TokenValidationRouter, RootTokenEnvelope
from util import LoggingLevelRouter


class TokenValidator(ValidationFactory[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an TokenCarrier is safe to use.

    Attributes:
        router: Optional[TokenValidationRouter]
        producer: Optional[TokenEnvelopeProducer]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            router: Optional[TokenValidationRouter] | None = None,
            producer: Optional[TokenEnvelopeProducer] | None = None,
    ):
        """
        Args:
            router: Optional[TokenValidationRouter]
            producer: Optional[TokenEnvelopeProducer]
        """
        super().__init__(
            router=router or TokenValidationRouter(),
            producer=producer or TokenEnvelopeProducer(),
        )
    
    @property
    def router(self) -> TokenValidationRouter:
        return cast(TokenValidationRouter, super().router)
    
    @property
    def producer(self) -> TokenEnvelopeProducer:
        return cast(TokenEnvelopeProducer, super().producer)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Router fails.
                    -   Team, Formation, Deployment, id, or HomeToken are flagged.
                    -   The producer does not return a product
            2.  Otherwise, send an TokenCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self.producer.execute(candidate=candidate)
        if product.is_failure:
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=product.exception,
                )
            )
        envelope = cast(RootTokenEnvelope, product.payload)
        
        validation = self.router.execute(envelope=envelope)
        if validation.is_failure:
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        carrier = cast(TokenCarrier, validation.payload)
        return ValidationResult.success(carrier)
    