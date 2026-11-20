# src/transit/dispatcher/validator/model/account/dispatcher.py

"""
Module: transit.dispatcher.validator.model.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import AccountValidator
from artifcat import ValidationResult
from domain import Account
from err import AccountValidationDispatcherException
from transit import ValidationDispatcher, AccountCarrier
from util import LoggingLevelRouter


class AccountValidationDispatcher(ValidationDispatcher[Account]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Account validation jobs among workers, then forward their results.

    Attributes:
        validator: AccountValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[AccountValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[AccountValidator]
        """
        super().__init__(validator=validator or AccountValidator())
        
    @property
    def validator(self) -> AccountValidator:
        return cast(AccountValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[AccountCarrier]:
        """
        Send jobs to a AccountValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a AccountCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[AccountCarrier]
        Raises:
             AccountValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationDispatcherException.MSG,
                    err_code=AccountValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AccountCarrier, validation.payload)
        return ValidationResult.success(carrier)