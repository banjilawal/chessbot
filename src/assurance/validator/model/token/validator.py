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
from assurance import (
    TokenEnvelopeProducer, TokenEnvelopeRouter, TokenValidationLoader,
    TokenValidatorToolkit, ModelValidator
)
from domain import Token
from err import TokenValidatorException
from transit import TokenCarrier, RootTokenEnvelope
from util import LoggingLevelRouter


class TokenValidator(ModelValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier is safe to use.

    Attributes:
        loader: TokenValidatorToolkit
        envelope_producer: TokenEnvelopeRouter
        property_table_generator: RootTokenEnvelopeGenerator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    _envelope_validator: TokenEnvelopeRouter
    _envelope_producer: TokenEnvelopeProducer
    
    def __init__(
            self,
            loader: Optional[TokenValidationLoader] | None = None,
            envelope_producer: Optional[TokenEnvelopeProducer] | None = None,
            envelope_validator: Optional[TokenEnvelopeRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[TokenLoader]
            envelope_producer: Optional[TokenEnvelopeProducer]
            envelope_validator: Optional[TokenEnvelopeRouter] 
        """
        super().__init__(loader=loader or TokenValidationLoader())
        self._envelope_producer = envelope_producer or TokenEnvelopeProducer()
        self._envelope_validator = envelope_validator or TokenEnvelopeRouter()
    
    @property
    def loader(self) -> TokenValidationLoader:
        return cast(TokenValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return self.loader.toolkit
    
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
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeToken are flagged.
                    -   The envelope_producer does not return a product
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self._envelope_producer.execute(candidate=candidate)
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
        
        validation = self._envelope_validator.execute(envelope=envelope)
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
    