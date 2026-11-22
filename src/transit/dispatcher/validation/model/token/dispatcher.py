# src/transit/dispatcher/validator/model/token/dispatcher.py

"""
Module: transit.dispatcher.validator.model.token.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import TokenValidator
from artifcat import ValidationResult
from domain import Token
from err import TokenValidationDispatcherException
from transit import ValidationDispatcher, TokenCarrier
from util import LoggingLevelRouter


class TokenValidationDispatcher(ValidationDispatcher[Token]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Token validation jobs among workers, then forward their results.

    Attributes:
        validator: TokenValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[TokenValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[TokenValidator]
        """
        super().__init__(validator=validator or TokenValidator())
        
    @property
    def validator(self) -> TokenValidator:
        return cast(TokenValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TokenCarrier]:
        """
        Send jobs to a TokenValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
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
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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
        carrier = cast(TokenCarrier, validation.content)
        return ValidationResult.success(carrier)