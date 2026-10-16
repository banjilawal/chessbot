# src/assurance/validator/model/account/validator.py

"""
Module: assurance.validator.model.account.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    AccountEnvelopeProducer, AccountValidationRouter, AccountValidationLoader,
    AccountValidatorToolkit, ModelValidator
)
from domain import Account
from err import AccountValidatorException
from transit import AccountCarrier, RootAccountEnvelope
from util import LoggingLevelRouter


class AccountValidator(ModelValidator[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a AccountCarrier is safe to use.

    Attributes:
        loader: Optional[AccountLoader]
        envelope_producer: Optional[AccountEnvelopeProducer]
        envelope_validator: Optional[AccountValidationRouter]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[AccountCarrier]:

    Super Class:
        ModelValidator
    """
    _envelope_validator: AccountValidationRouter
    _envelope_producer: AccountEnvelopeProducer
    
    def __init__(
            self,
            loader: Optional[AccountValidationLoader] | None = None,
            envelope_producer: Optional[AccountEnvelopeProducer] | None = None,
            envelope_validator: Optional[AccountValidationRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[AccountLoader]
            envelope_producer: Optional[AccountEnvelopeProducer]
            envelope_validator: Optional[AccountValidationRouter]
        """
        super().__init__(loader=loader or AccountValidationLoader())
        self._envelope_producer = envelope_producer or AccountEnvelopeProducer()
        self._envelope_validator = envelope_validator or AccountValidationRouter()
    
    @property
    def loader(self) -> AccountValidationLoader:
        return cast(AccountValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> AccountValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[AccountCarrier]:
        """
        Assure a candidate is a safe AccountCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeAccount are flagged.
                    -   The envelope_producer does not return a product
            2.  Otherwise, send a AccountCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AccountCarrier]
        Raises:
            AccountValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self._envelope_producer.execute(candidate=candidate)
        if product.is_failure:
            return ValidationResult.failure(
                AccountValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidatorException.MSG,
                    err_code=AccountValidatorException.ERR_CODE,
                    ex=product.exception,
                )
            )
        envelope = cast(RootAccountEnvelope, product.payload)
        
        validation = self._envelope_validator.execute(envelope=envelope)
        if validation.is_failure:
            return ValidationResult.failure(
                AccountValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidatorException.MSG,
                    err_code=AccountValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        carrier = cast(AccountCarrier, validation.payload)
        return ValidationResult.success(carrier)
    