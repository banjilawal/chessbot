# src/assurance/validator/model/rank/validator.py

"""
Module: assurance.validator.model.rank.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    BishopValidator, KingValidator, KnightValidator, ModelValidator, PawnValidator, QueenValidator,
    RankValidatorToolkit,
    RookValidator
)
from domain import Rank, RankValidationRequest
from err import RankValidationRequestNullException, RankValidatorException
from transit import BishopCarrier, KingCarrier, KnightCarrier, PawnCarrier, QueenCarrier, RankCarrier, RookCarrier
from util import LoggingLevelRouter


class RankValidator(ModelValidator[Rank]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a RankCarrier is safe to use.

    Attributes:
        loader: RankValidatorToolkit

    Provides:
        -   def execute(candidate: RankValidationRequest) ->ValidationResult[RankCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[RankValidatorToolkit] | None = None,
    ):
        """
        Args:
            loader: Optional[RankValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or RankValidatorToolkit())
    
    @property
    def toolkit(self) -> RankValidatorToolkit:
        return cast(
            RankValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RankCarrier]:
        """
        Certify a candidate is a RankCarrier whose payload is either a Rank
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a RankCarrier or its null.
                    - The candidate is an empty RankCarrier.
                    - Any Rank attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RankCarrier]
        Raises:
            RankValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.wrapper.priming_validator.execute(
            candidate=candidate,
            target_model=RankValidationRequest,
            null_exception=RankValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        request = cast(RankValidationRequest, priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.wrapper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload to route for additional processing. ---#
        carrier = cast(RankCarrier, carrier_validation.payload)
        
        if isinstance(carrier, BishopCarrier):
            helper = BishopValidator()
            return helper.execute(carrier)
        if isinstance(carrier, KingCarrier):
            helper = KingValidator()
            return helper.execute(carrier)
        if isinstance(carrier, KnightCarrier):
            helper = KnightValidator()
            return helper.execute(carrier)
        if isinstance(carrier, PawnCarrier):
            helper = PawnValidator()
            return helper.execute(carrier)
        if isinstance(carrier, QueenCarrier):
            helper = QueenValidator()
            return helper.execute(carrier)
        helper = RookValidator()
        return helper.execute(cast(RookCarrier, carrier))

    
    