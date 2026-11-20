# src/transit/dispatcher/validator/context/account/dispatcher.py

"""
Module: transit.dispatcher.validator.context.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import AccountContextValidator
from domain import AccountContext
from transit import AccountContextCarrier, ValidationDispatcher
from util import LoggingLevelRouter


class AccountContextValidationDispatcher(ValidationDispatcher[AccountContext]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute AccountContext validation jobs among workers, then forward their results.

    Attributes:
        validator: AccountContextValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(
            self,
            validator: Optional[AccountContextValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[AccountContextValidator]
        """
        super().__init__(validator=validator or AccountContextValidator())
    
    @property
    def validator(self) -> AccountContextValidator:
        return cast(AccountContextValidator, super().validator)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[AccountContextCarrier]:
        """
        Send jobs to an AccountContextValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into an AccountContextCarrier and
                send in the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
             AccountContextValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountContextValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationDispatcherException.MSG,
                    err_code=AccountContextValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AccountContextCarrier, validation.payload)
        return ValidationResult.success(carrier)