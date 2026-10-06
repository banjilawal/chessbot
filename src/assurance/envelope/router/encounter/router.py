# src/assurance/envelope/router/encounterr.py

"""
Module: assurance.envelope.router.encounterr
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    EncounterWarningEnvelopeConsumer, EnvelopeRouter, KillEncounterEnvelopeConsumer, CheckmateEncounterEnvelopeConsumer,
    EncounterValidatorToolkit
)
from domain import Encounter
from err import RootEncounterEnvelopeNullException, EncounterEnvelopeRouterException
from transit import RootEncounterEnvelope, EncounterCarrier
from util import LoggingLevelRouter


class EncounterEnvelopeRouter(EnvelopeRouter[Encounter]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RootEncounterEnvelope to its appropriate Consumer
            by Carrier type.

    Attributes:
        toolkit: EncounterValidatorToolkit
        kill_consumer: KillEncounterEnvelopeConsumer
        checkmate_consumer: CheckmateEncounterEnvelopeConsumer
        encounter_warning_consumer: EncounterWarningEnvelopeConsumer

    Provides:
        -   def execute(envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]

    Super Class:
        EnvelopeRouter
    """
    _kill_consumer: KillEncounterEnvelopeConsumer
    _checkmate_consumer: CheckmateEncounterEnvelopeConsumer
    _encounter_warning_consumer: EncounterWarningEnvelopeConsumer
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit]
                     | None = None,
            kill_consumer: Optional[KillEncounterEnvelopeConsumer]
                           | None = None,
            checkmate_consumer: Optional[CheckmateEncounterEnvelopeConsumer]
                                | None = None,
            encounter_warning_consumer: Optional[EncounterWarningEnvelopeConsumer]
                                        | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
            kill_consumer: Optional[KillEncounterEnvelopeConsumer]
            checkmate_consumer: Optional[CheckmateEncounterEnvelopeConsumer]
            encounter_warning_consumer: Optional[EncounterWarningEnvelopeConsumer]
        """
        super().__init__(toolkit=toolkit or EncounterValidatorToolkit())
        self._kill_consumer = (
                kill_consumer or KillEncounterEnvelopeConsumer()
        )
        self._checkmate_consumer = (
                checkmate_consumer or CheckmateEncounterEnvelopeConsumer()
        )
        self._encounter_warning_consumer = (
                encounter_warning_consumer or EncounterWarningEnvelopeConsumer()
        )
    
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return cast(EncounterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of
                the following occur:
                    -   The router cannot be primed.
                    -   The endpoint cannot consume the envelope.
                    -   No consumption route exists
            2.  Otherwise, cast the payload and send in the success result.
        Args:
            envelope: RootEncounterEnvelope
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
           EncounterEnvelopeRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the router cannot be primed.
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootEncounterEnvelope,
            null_exception=RootEncounterEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterEnvelopeRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterEnvelopeRouterException.MSG,
                    err_code=EncounterEnvelopeRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        safe = cast(RootEncounterEnvelope, priming.payload)
        
        # --- Route to the appropriate consumer. ---#
        result = ValidationResult.failure(EncounterEnvelopeRouterException())
        
        # Route to kill_encounter_validation consumers.
        if safe.for_kill_encounter_consumer:
            result = self._kill_consumer.execute(envelope=safe)
        # Route to checkmate_encounter_validation consumers.
        if safe.for_checkmate_encounter_consumer:
            result = self._checkmate_consumer.execute(envelope=safe)
        # Route to encounter_warning_validation consumers
        if safe.for_encounter_warning_consumer:
            result = self._encounter_warning_consumer.execute(envelope=safe)
            
        # Handle the case that the envelope is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterEnvelopeRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterEnvelopeRouterException.MSG,
                    err_code=EncounterEnvelopeRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        carrier = cast(EncounterCarrier, result.payload)
        return ValidationResult.success(carrier)
        




    