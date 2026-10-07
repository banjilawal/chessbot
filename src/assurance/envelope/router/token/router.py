# src/assurance/envelope/router/tokenr.py

"""
Module: assurance.envelope.router.tokenr
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    EnvelopeRouter, CombatantTokenEnvelopeConsumer,
    PawnTokenEnvelopeConsumer, TokenValidatorToolkit
)
from domain import Token
from err import RootTokenEnvelopeNullException, TokenEnvelopeRouterException
from transit import RootTokenEnvelope, TokenCarrier
from util import LoggingLevelRouter


class TokenEnvelopeRouter(EnvelopeRouter[Token]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RootTokenEnvelope to its appropriate Consumer
            by Carrier type.

    Attributes:
        toolkit: TokenValidatorToolkit
        combatant_consumer: CombatantTokenEnvelopeConsumer
        pawn_consumer: PawnTokenEnvelopeConsumer
        token_warning_consumer: TokenWarningEnvelopeConsumer

    Provides:
        -   def execute(envelope: RootTokenEnvelope) -> ValidationResult[TokenCarrier]

    Super Class:
        EnvelopeRouter
    """
    _combatant_consumer: CombatantTokenEnvelopeConsumer
    _pawn_consumer: PawnTokenEnvelopeConsumer
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            combatant_consumer: Optional[CombatantTokenEnvelopeConsumer] | None = None,
            pawn_consumer: Optional[PawnTokenEnvelopeConsumer] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            combatant_consumer: Optional[CombatantTokenEnvelopeConsumer]
            pawn_consumer: Optional[PawnTokenEnvelopeConsumer]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._combatant_consumer = combatant_consumer or CombatantTokenEnvelopeConsumer()
        self._pawn_consumer = pawn_consumer or PawnTokenEnvelopeConsumer()
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootTokenEnvelope) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of
                the following occur:
                    -   The router cannot be primed.
                    -   The endpoint cannot consume the envelope.
                    -   No consumption route exists
            2.  Otherwise, cast the payload and send in the success result.
        Args:
            envelope: RootTokenEnvelope
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
           TokenEnvelopeRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the router cannot be primed.
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootTokenEnvelope,
            null_exception=RootTokenEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeRouterException.MSG,
                    err_code=TokenEnvelopeRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        safe = cast(RootTokenEnvelope, priming.payload)
        
        # --- Route to the appropriate consumer. ---#
        result = ValidationResult.failure(TokenEnvelopeRouterException())
        
        # Route to combatant_token_validation consumers.
        if safe.for_combatant_token_consumer:
            result = self._combatant_consumer.execute(envelope=safe)
        # Route to pawn_token_validation consumers.
        if safe.for_pawn_token_consumer:
            result = self._pawn_consumer.execute(envelope=safe)
            
        # Handle the case that the envelope is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeRouterException.MSG,
                    err_code=TokenEnvelopeRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        carrier = cast(TokenCarrier, result.payload)
        return ValidationResult.success(carrier)
        




    