# src/assurance/validator/context/account/validator.py

"""
Module: assurance.validator.context.account.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit
from bootstrap import AccountContextValidationLoader
from domain import AccountContext
from transit import ContextValidator
from util import LoggingLevelRouter


class AccountContextValidator(
    ContextValidator[AccountContext]
):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountContextCarrier and its payload are
            safe to use.

    Attributes:
        loader: AccountContextValidationLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[AccountContextCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            loader: [AccountContextValidationLoader] | None = None,
    ):
        """
        Args:
           loader: [AccountContextValidationLoader]
        """
        super().__init__(loader=loader or AccountContextValidationLoader())
    
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[AccountContextCarrier]:
        """
        Assure a candidate is a safe AccountContextCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The loader cannot bootstrap the process.
                    -   The chosen context is flagged.
                    -   There is no route to validate the choice.
            2.  Otherwise, send an AccountContextCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self.producer.execute(candidate=candidate)
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
        
        validation = self.router.execute(envelope=envelope)
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
    