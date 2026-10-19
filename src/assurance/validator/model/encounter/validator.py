# src/assurance/validator/model/encounter/validator.py

"""
Module: assurance.validator.model.encounter.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import EncounterEnvelopeProducer, ValidationFactory
from domain import Encounter
from err import EncounterValidatorException
from transit import EncounterCarrier, EncounterValidationRouter, RootEncounterEnvelope
from util import LoggingLevelRouter


class EncounterValidator(ValidationFactory[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an EncounterCarrier is safe to use.

    Attributes:
        router: Optional[EncounterValidationRouter]
        producer: Optional[EncounterEnvelopeProducer]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[EncounterCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            router: Optional[EncounterValidationRouter] | None = None,
            producer: Optional[EncounterEnvelopeProducer] | None = None,
    ):
        """
        Args:
            router: Optional[EncounterValidationRouter]
            producer: Optional[EncounterEnvelopeProducer]
        """
        super().__init__(
            router=router or EncounterValidationRouter(),
            producer=producer or EncounterEnvelopeProducer(),
        )
    
    @property
    def router(self) -> EncounterValidationRouter:
        return cast(EncounterValidationRouter, super().router)
    
    @property
    def producer(self) -> EncounterEnvelopeProducer:
        return cast(EncounterEnvelopeProducer, super().producer)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[EncounterCarrier]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Router fails.
                    -   Team, Formation, Deployment, id, or HomeEncounter are flagged.
                    -   The producer does not return a product
            2.  Otherwise, send an EncounterCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
            EncounterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self.producer.execute(candidate=candidate)
        if product.is_failure:
            return ValidationResult.failure(
                EncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidatorException.MSG,
                    err_code=EncounterValidatorException.ERR_CODE,
                    ex=product.exception,
                )
            )
        envelope = cast(RootEncounterEnvelope, product.payload)
        
        validation = self.router.execute(envelope=envelope)
        if validation.is_failure:
            return ValidationResult.failure(
                EncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidatorException.MSG,
                    err_code=EncounterValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        carrier = cast(EncounterCarrier, validation.payload)
        return ValidationResult.success(carrier)
    