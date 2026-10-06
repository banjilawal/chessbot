# src/assurance/envelope/consumer/square/home/consumer.py

"""
Module: assurance.envelope.consumer.square.home.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import RootEnvelopeConsumer, SquareValidatorToolkit
from domain import Formation, HomeSquare, HomeSquareBlueprint
from err import (
    EmptyHomeSquareCarrierException, FormationNullException, HomeSquareEnvelopeConsumerException,
    RootSquareEnvelopeNullException,
)
from transit import HomeSquareCarrier, RootSquareEnvelope
from util import LoggingLevelRouter


class HomeSquareEnvelopeConsumer(RootEnvelopeConsumer[HomeSquare]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a HomeSquare covered by a SquareEnvelope is safe.

    Attributes:
        toolkit: SquareValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootSquareEnvelope
            ) -> ValidationResult[HomeSquareCarrier]

    Super Class:
        EnvelopeConsumer
    """
    
    def __init__(self, toolkit: Optional[SquareValidatorToolkit] | None = None):
        super().__init__(toolkit=toolkit or SquareValidatorToolkit())
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return cast(SquareValidatorToolkit, super().toolkit)

    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootSquareEnvelope) -> ValidationResult[HomeSquareCarrier]:
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
            ValidationResult[HomeSquareCarrier]
        Raises:
            HomeSquareEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the consumer cannot be primed.
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootSquareEnvelope,
            null_exception=RootSquareEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HomeSquareEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareEnvelopeConsumerException.MSG,
                    err_code=HomeSquareEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        safe = cast(RootSquareEnvelope, priming.payload)
        if not safe.for_home_square_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HomeSquareEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareEnvelopeConsumerException.MSG,
                    err_code=HomeSquareEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        original_extract = safe.prime_extract
        reference = cast(HomeSquareCarrier, original_extract.reference)
        blueprint = reference.extract_blueprint()
        
        # Handle the case that there is no blueprint in the carrier.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HomeSquareEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareEnvelopeConsumerException.MSG,
                    err_code=HomeSquareEnvelopeConsumerException.ERR_CODE,
                    ex=EmptyHomeSquareCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyHomeSquareCarrierException.MSG,
                        err_code=EmptyHomeSquareCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_FORMATION_ATTRIBUTE. ---#
        formation_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        # Handle the case that the formation does not pass a validation check.
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HomeSquareEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareEnvelopeConsumerException.MSG,
                    err_code=HomeSquareEnvelopeConsumerException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        name = safe.name
        state = safe.state
        board = safe.board
        coord = safe.coord
        occupant = safe.occupant
        formation = cast(Formation, formation_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if original_extract.recipient_wants_model:
            model = HomeSquare(
                id=id,
                name=name,
                board=board,
                coord=coord,
                formation=formation,
            )
            model.occupant = safe.occupant
            model.state = safe.state
            return ValidationResult.success(
                HomeSquareCarrier(model=model)
            )
        # The blueprint case
        payload = HomeSquareCarrier(
            blueprint=HomeSquareBlueprint(
                id=id,
                name=name,
                board=board,
                coord=coord,
                state=state,
                occupant=occupant,
                formation=formation,
            )
        )
        return ValidationResult.success(payload)