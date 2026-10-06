# src/assurance/envelope/router/squarer.py

"""
Module: assurance.envelope.router.squarer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    EnvelopeRouter, HomeSquareEnvelopeConsumer, PublicSquareEnvelopeConsumer,
    SquareValidatorToolkit
)
from domain import Square
from err import RootSquareEnvelopeNullException, SquareEnvelopeRouterException
from transit import RootSquareEnvelope, SquareCarrier
from util import LoggingLevelRouter


class SquareEnvelopeRouter(EnvelopeRouter[Square]):
    """
    Role
        - Router

    Responsibilities:
        1.  Route a RootSquareEnvelope to its appropriate Consumer by the SquareCarrier type.

    Attributes:
        toolkit: SquareValidatorToolkit
        home: HomeSquareEnvelopeConsumer
        public: PublicSquareEnvelopeConsumer

    Provides:
        -   def execute(
                envelope: RootSquareEnvelope
            ) -> ValidationResult[SquareCarrier]

    Super Class:
        EnvelopeRouter
    """
    _home_consumer: HomeSquareEnvelopeConsumer
    _public_consumer: PublicSquareEnvelopeConsumer
    
    def __init__(
            self,
            toolkit: Optional[SquareValidatorToolkit] | None = None,
            home_consumer: Optional[HomeSquareEnvelopeConsumer] | None = None,
            public_consumer: Optional[PublicSquareEnvelopeConsumer] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareValidatorToolkit]
            home_consumer: Optional[HomeSquareEnvelopeConsumer]
            public_consumer: Optional[PublicSquareEnvelopeConsumer]
        """
        super().__init__(toolkit=toolkit or SquareValidatorToolkit())
        self._home_consumer = home_consumer or HomeSquareEnvelopeConsumer()
        self._public_consumer = public_consumer or PublicSquareEnvelopeConsumer()
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return cast(SquareValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootSquareEnvelope) -> ValidationResult[SquareCarrier]:
        """
        Assure a candidate is a safe SquareCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur:
                    -   The router cannot be primed.
                    -   The endpoint cannot consume the envelope.
                    -   No consumption route exists
            2.  Otherwise, cast the payload and send in the success result.
        Args:
            envelope: RootSquareEnvelope
        Returns:
            ValidationResult[SquareCarrier]
        Raises:
           SquareEnvelopeRouterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the router cannot be primed.
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootSquareEnvelope,
            null_exception=RootSquareEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareEnvelopeRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareEnvelopeRouterException.MSG,
                    err_code=SquareEnvelopeRouterException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # Otherwise get the payload.
        safe_envelope = cast(RootSquareEnvelope, priming.payload)
        
        # --- Route to the appropriate consumer. ---#
        result = ValidationResult.failure(SquareEnvelopeRouterException())
        if safe_envelope.for_home_square_consumer:
            result = self._home_consumer.execute(envelope=safe_envelope)
        else:
            result = self._public_consumer.execute(envelope=safe_envelope)
        # Handle the case that the envelope is not consumed.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareEnvelopeRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareEnvelopeRouterException.MSG,
                    err_code=SquareEnvelopeRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product to client. ---#
        carrier = cast(SquareCarrier, result.payload)
        return ValidationResult.success(carrier)
        




    