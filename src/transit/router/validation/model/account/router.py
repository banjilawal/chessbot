# src/transit/route/validation/model/account/router.py

"""
Module: transit.route.validation.model.account.router
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    MachineAccountEnvelopeConsumer, HumanAccountEnvelopeConsumer, AccountLayerToolkit
)
from domain import Account
from err import (
    AccountValidationRouteMissingException, RootAccountEnvelopeNullException,
    AccountValidationRouterException
)
from transit import RootAccountEnvelope, AccountCarrier, ValidationRouter
from util import LoggingLevelRouter


class AccountValidationRouter(ValidationRouter[Account]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RootAccountEnvelope to its appropriate Consumer
            by Carrier type.

    Attributes:
        toolkit: AccountLayerToolkit
        human_consumer: HumanAccountEnvelopeConsumer
        machine_consumer: MachineAccountEnvelopeConsumer
        combatant_consumer: CombatantAccountEnvelopeConsumer

    Provides:
        -   def execute(envelope: RootAccountEnvelope) -> ValidationResult[AccountCarrier]

    Super Class:
        ValidationRouter
    """
    _human_consumer: HumanAccountEnvelopeConsumer
    _machine_consumer: MachineAccountEnvelopeConsumer
    
    def __init__(
            self,
            human_consumer: Optional[HumanAccountEnvelopeConsumer] | None = None,
            machine_consumer: Optional[MachineAccountEnvelopeConsumer] | None = None,
            toolkit: Optional[AccountLayerToolkit] | None = None,
    ):
        """
        Args:
            human_consumer: Optional[HumanAccountEnvelopeConsumer]
            machine_consumer: Optional[MachineAccountEnvelopeConsumer]
            toolkit: Optional[AccountLayerToolkit]
        """
        super().__init__(toolkit=toolkit or AccountLayerToolkit())
        self._human_consumer = human_consumer or HumanAccountEnvelopeConsumer()
        self._machine_consumer = machine_consumer or MachineAccountEnvelopeConsumer()

    
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootAccountEnvelope) -> ValidationResult[AccountCarrier]:
        """
        Assure a candidate is a safe AccountCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of
                the following occur:
                    -   The router cannot be primed.
                    -   The endpoint cannot consume the envelope.
                    -   No consumption route exists
            2.  Otherwise, cast the payload and send in the success result.
        Args:
            envelope: RootAccountEnvelope
        Returns:
            ValidationResult[AccountCarrier]
        Raises:
           AccountValidationRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the router cannot be primed.
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootAccountEnvelope,
            null_exception=RootAccountEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationRouterException.MSG,
                    err_code=AccountValidationRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        safe = cast(RootAccountEnvelope, priming.payload)
        
        # --- Route to the appropriate consumer. ---#
        result = ValidationResult.failure(
            AccountValidationRouterException(
                ex=AccountValidationRouteMissingException()
            )
        )
        
        # Route to combatant_account_validation consumers.
        # Route to human_account_validation consumers.
        if safe.for_human_account_consumer:
            result = self._human_consumer.execute(envelope=safe)
        # Route to the machine_account_validation consumers
        if safe.for_machine_account_consumer:
            result = self._machine_consumer.execute(envelope=safe)
            
        # Handle the case that the envelope is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationRouterException.MSG,
                    err_code=AccountValidationRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        carrier = cast(AccountCarrier, result.payload)
        return ValidationResult.success(carrier)
        




    