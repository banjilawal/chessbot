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
from assurance import ContextValidator
from domain import AccountContext
from err import AccountContextValidatorException
from production import AccountContextValidationManager
from transit import AccountContextCarrier
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
        manager: AccountContextValidationManager

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[AccountContextCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            manager: Optional[AccountContextValidationManager] | None = None,
    ):
        """
        Args:
           manager: Optional[AccountContextValidationManager]
        """
        super().__init__(manager=manager or AccountContextValidationManager())
    
    @property
    def manager(self) -> AccountContextValidationManager:
        return cast(AccountContextValidationManager, super().manager)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[AccountContextCarrier]:
        """
        Assure a candidate is a safe AccountContextCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if the manager does
                not return a validation product.
            2.  Otherwise, send success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Hand the request off to the manager.
        result = self.manager.execute(candidate)
        # Handle the case that the manager does not fulfil the request
        if result.is_failure:
            return ValidationResult.failure(
                AccountContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidatorException.MSG,
                    err_code=AccountContextValidatorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AccountContextCarrier, result.payload)
        return ValidationResult.success(carrier)



    