# src/assurance/validator/model/square/assurance/validator/model.py

"""
Module: assurance.validator.model.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import EnvelopeConsumer, SquareValidatorToolkit
from domain import Square, SquareBlueprint
from err import RootSquareEnvelopeNullException
from transit import RootSquareEnvelope, SquareCarrier

from util import LoggingLevelRouter


class PublicSquareEnvelopeConsumer(EnvelopeConsumer[Square]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a Square covered by a SquareEnvelope is safe.

    Attributes:
        toolkit: SquareValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootSquareEnvelope
            ) -> ValidationResult[SquareCarrier]

    Super Class:
        EnvelopeConsumer
    """
    
    def __init__(self, toolkit: Optional[SquareValidatorToolkit] | None = None):
        super().__init__(toolkit=toolkit or SquareValidatorToolkit())
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return cast(SquareValidatorToolkit, super().toolkit)

    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootSquareEnvelope) -> ValidationResult[SquareCarrier]:
        """
        Certify a SquareCarrier's payload is either a Square or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a SquareValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a SquareCarrier
                            an empty SquareCarrier.
                    -   Either the id, board, or coord attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            envelope: RootSquareEnvelope
        Returns:
            ValidationResult[SquareCarrier]
        Raises:
            PublicSquareEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootSquareEnvelope,
            null_exception=RootSquareEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PublicSquareEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PublicSquareEnvelopeConsumerException.MSG,
                    err_code=PublicSquareEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        safe = cast(RootSquareEnvelope, priming.payload)
        if not safe.for_public_square_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PublicSquareEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PublicSquareEnvelopeConsumerException.MSG,
                    err_code=PublicSquareEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        prime_extract = safe.prime_extract
        # --- Extract and cast payloads of the validation results. ---#
        id = safe.id
        name = safe.name
        state = safe.state
        board = safe.board
        coord = safe.coord
        occupant = safe.occupant
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if prime_extract.recipient_wants_model:
            model = Square(
                id=id,
                name=name,
                board=board,
                coord=coord,
            )
            model.occupant = occupant
            model.state = state
            payload = SquareCarrier(model=model)
            return ValidationResult.success(payload)
        # The blueprint case
        payload = SquareCarrier(
            blueprint=SquareBlueprint(
                id=id,
                name=name,
                board=board,
                coord=coord,
                state=state,
                occupant=occupant,
            )
        )
        return ValidationResult.success(payload)