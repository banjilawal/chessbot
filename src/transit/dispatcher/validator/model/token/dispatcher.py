# src/transit/dispatcher/validator/model/token/validator.py

"""
Module: transit.dispatcher.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import TokenValidator
from artifcat import ValidationResult
from domain import Token
from err import TokenValidationDispatcherException
from transit import ModelValidationDispatcher, TokenCarrier
from util import LoggingLevelRouter


class TokenValidationDispatcher(ModelValidationDispatcher[Token]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the TokenValidation workflow.

    Attributes:
        validator: TokenValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: TokenValidator | None = None,
    ):
        super().__init__(validator=validator or TokenValidator())
        
    @property
    def validator(self) -> TokenValidator:
        return cast(TokenValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TokenCarrier]:
        """
        Forward a job to a TokenValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a TokenCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
             TokenValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationDispatcherException.MSG,
                    err_code=TokenValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(TokenCarrier, validation.payload)
        return ValidationResult.success(carrier)