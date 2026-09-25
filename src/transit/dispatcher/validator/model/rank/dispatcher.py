# src/transit/dispatcher/validator/model/rank/validator.py

"""
Module: transit.dispatcher.validator.model.rank.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import RankValidator
from artifcat import ValidationResult
from domain import Rank
from err import RankValidationDispatcherException
from transit import ModelValidationDispatcher, RankCarrier
from util import LoggingLevelRouter


class RankValidationDispatcher(ModelValidationDispatcher[Rank]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the RankValidation workflow.

    Attributes:
        validator: RankValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: RankValidator | None = None,
    ):
        super().__init__(validator=validator or RankValidator())
        
    @property
    def validator(self) -> RankValidator:
        return cast(RankValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[RankCarrier]:
        """
        Forward a job to a RankValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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