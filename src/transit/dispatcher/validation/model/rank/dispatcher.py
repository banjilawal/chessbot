# src/transit/dispatcher/validator/model/rank/dispatcher.py

"""
Module: transit.dispatcher.validator.model.rank.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import RankValidator
from artifcat import ValidationResult
from domain import Rank
from err import RankValidationDispatcherException
from transit import ValidationDispatcher, RankCarrier
from util import LoggingLevelRouter


class RankValidationDispatcher(ValidationDispatcher[Rank]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Rank validation jobs among workers, then forward their results.

    Attributes:
        validator: RankValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[RankValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[RankValidator]
        """
        super().__init__(validator=validator or RankValidator())
        
    @property
    def validator(self) -> RankValidator:
        return cast(RankValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[RankCarrier]:
        """
        Send jobs to a RankValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a RankCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[RankCarrier]
        Raises:
             RankValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationDispatcherException.MSG,
                    err_code=RankValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(RankCarrier, validation.payload)
        return ValidationResult.success(carrier)