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
from assurance import (
    EncounterEnvelopeProducer, EncounterValidationRouter, EncounterValidationLoader,
    EncounterValidatorToolkit, ModelValidator
)
from domain import Encounter
from err import EncounterValidatorException
from transit import EncounterCarrier, RootEncounterEnvelope
from util import LoggingLevelRouter


class EncounterValidator(ModelValidator[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a EncounterCarrier is safe to use.

    Attributes:
        loader: EncounterValidatorToolkit
        envelope_producer: EncounterValidationRouter
        property_table_generator: RootEncounterEnvelopeGenerator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[EncounterCarrier]:

    Super Class:
        ModelValidator
    """
    _envelope_validator: EncounterValidationRouter
    _envelope_producer: EncounterEnvelopeProducer
    
    def __init__(
            self,
            loader: Optional[EncounterValidationLoader] | None = None,
            envelope_producer: Optional[EncounterEnvelopeProducer] | None = None,
            envelope_validator: Optional[EncounterValidationRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[EncounterLoader]
            envelope_producer: Optional[EncounterEnvelopeProducer]
            envelope_validator: Optional[EncounterValidationRouter]
        """
        super().__init__(loader=loader or EncounterValidationLoader())
        self._envelope_producer = envelope_producer or EncounterEnvelopeProducer()
        self._envelope_validator = envelope_validator or EncounterValidationRouter()
    
    @property
    def loader(self) -> EncounterValidationLoader:
        return cast(EncounterValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return self.loader.toolkit
    
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
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeEncounter are flagged.
                    -   The envelope_producer does not return a product
            2.  Otherwise, send a EncounterCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
            EncounterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self._envelope_producer.execute(candidate=candidate)
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
        
        validation = self._envelope_validator.execute(envelope=envelope)
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
    