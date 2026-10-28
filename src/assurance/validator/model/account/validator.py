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
from assurance import ModelValidationFactory
from domain import Account
from err import AccountValidatorException
from production import AccountEnvelopeManager
from transit import AccountCarrier
from util import LoggingLevelRouter


class AccountValidator(ModelValidationFactory[Account]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountCarrier is safe to use.

    Attributes:
        manager: Optional[AccountEnvelopeManager]

    Provides:
        -   def execute(candidate: item) -> ValidationResult[AccountCarrier]:

    Super Class:
        ModelValidationFactory
    """
    
    def __init__(self, manager: Optional[AccountEnvelopeManager]):
        """
        Args:
            manager: Optional[AccountEnvelopeManager]
        """
        super().__init__(manager=manager or AccountEnvelopeManager())

    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[AccountCarrier]:
        """
        Assure a candidate is a safe AccountCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Router fails.
                    -   Team, Formation, Deployment, id, or HomeAccount are flagged.
                    -   The producer does not return a product
            2.  Otherwise, send an AccountCarrier in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[AccountCarrier]
        Raises:
            AccountValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        validation = self.manager.execute(item=item)
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
    