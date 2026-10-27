# src/transit/route/validation/model/token/router.py

"""
Module: transit.route.validation.model.token.router
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    CombatantTokenEnvelopeConsumer, KingTokenEnvelopeConsumer, PawnTokenEnvelopeConsumer,
    TokenLayerToolkit
)
from domain import Token
from err import RootTokenEnvelopeNullException, TokenValidationRouteMissingException, TokenValidationRouterException
from transit import RootTokenEnvelope, TokenCarrier, ValidationRouter
from util import LoggingLevelRouter


class TokenValidationRouter(ValidationRouter[Token]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RootTokenEnvelope to its appropriate Consumer
            by Carrier type.

    Attributes:
        toolkit: TokenLayerToolkit
        pawn_consumer: PawnTokenEnvelopeConsumer
        king_consumer: KingTokenEnvelopeConsumer
        combatant_consumer: CombatantTokenEnvelopeConsumer

    Provides:
        -   def execute(envelope: RootTokenEnvelope) -> ValidationResult[TokenCarrier]

    Super Class:
        ValidationRouter
    """
    _pawn_consumer: PawnTokenEnvelopeConsumer
    _king_consumer: KingTokenEnvelopeConsumer
    _combatant_consumer: CombatantTokenEnvelopeConsumer
    
    def __init__(
            self,
            pawn_consumer: Optional[PawnTokenEnvelopeConsumer] | None = None,
            king_consumer: Optional[KingTokenEnvelopeConsumer] | None = None,
            combatant_consumer: Optional[CombatantTokenEnvelopeConsumer] | None = None,
            toolkit: Optional[TokenLayerToolkit] | None = None,
    ):
        """
        Args:
            pawn_consumer: Optional[PawnTokenEnvelopeConsumer]
            king_consumer: Optional[KingTokenEnvelopeConsumer]
            combatant_consumer: Optional[CombatantTokenEnvelopeConsumer]
            toolkit: Optional[TokenLayerToolkit]
        """
        super().__init__(toolkit=toolkit or TokenLayerToolkit())
        self._pawn_consumer = pawn_consumer or PawnTokenEnvelopeConsumer()
        self._king_consumer = king_consumer or KingTokenEnvelopeConsumer()
        self._combatant_consumer = combatant_consumer or CombatantTokenEnvelopeConsumer()

    
    @property
    def toolkit(self) -> TokenLayerToolkit:
        return cast(TokenLayerToolkit, super().toolkit)
    
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
           TokenValidationRouterException
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
                TokenValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationRouterException.MSG,
                    err_code=TokenValidationRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        safe = cast(RootTokenEnvelope, priming.payload)
        
        # --- Route to the appropriate consumer. ---#
        result = ValidationResult.failure(
            TokenValidationRouterException(
                ex=TokenValidationRouteMissingException()
            )
        )
        
        # Route to combatant_token_validation consumers.
        if safe.for_combatant_token_consumer:
            result = self._combatant_consumer.execute(envelope=safe)
        # Route to pawn_token_validation consumers.
        if safe.for_pawn_token_consumer:
            result = self._pawn_consumer.execute(envelope=safe)
        # Route to the king_token_validation consumers
        if safe.for_king_token_consumer:
            result = self._king_consumer.execute(envelope=safe)
            
        # Handle the case that the envelope is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationRouterException.MSG,
                    err_code=TokenValidationRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        carrier = cast(TokenCarrier, result.payload)
        return ValidationResult.success(carrier)
        




    