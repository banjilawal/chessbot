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
from transit import AccountContextCarrier, ContextValidationDispatcher
from util import LoggingLevelRouter


class AccountContextValidationDispatcher(
    ContextValidationDispatcher[AccountContext]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AccountValidation workflow.

    Attributes:
        validator: AccountContextValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ContextValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[AccountContextValidator] | None = None,
    ):
        super().__init__(validator=validator or AccountContextValidator())
        
    @property
    def validator(self) -> AccountContextValidator:
        return cast(AccountContextValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[AccountContextCarrier]:
        """
        Forward a job to an AccountContextValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into an AccountContextCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
             AccountContextValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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
        carrier = cast(AccountContextCarrier, validation.authorization_applicant)
        return ValidationResult.success(carrier)