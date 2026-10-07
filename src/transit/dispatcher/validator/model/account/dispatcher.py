# src/transit/dispatcher/validator/model/account/validator.py

"""
Module: transit.dispatcher.validator.model.account.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import AccountValidator
from artifcat import ValidationResult
from domain import Account
from err import AccountValidationDispatcherException
from transit import ModelValidationDispatcher, AccountCarrier
from util import LoggingLevelRouter


class AccountValidationDispatcher(ModelValidationDispatcher[Account]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AccountValidation workflow.

    Attributes:
        validator: AccountValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: AccountValidator | None = None,
    ):
        super().__init__(validator=validator or AccountValidator())
        
    @property
    def validator(self) -> AccountValidator:
        return cast(AccountValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[AccountCarrier]:
        """
        Forward a job to a AccountValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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