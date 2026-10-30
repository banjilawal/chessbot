# src/assurance/validator/model/ran/validator.py

"""
Module: assurance.validator.model.rank.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, RankValidationLoader, RankLayerToolkit
from domain import Arena, Persona, Rank, RankBlueprint, RankPrimeExtract, PlayerPersona
from err import RankCarrierEmptyException, RankValidatorException
from exchange import (
    ArenaValidationRequest, PlayerPersonaValidationRequest
)
from transit import ArenaCarrier, PlayerPersonaCarrier, RankCarrier
from util import IdFactory, LoggingLevelRouter


class RankValidator(ModelValidator[Rank]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a RankCarrier and its contents are safe to use.

    Attributes:
        loader: RankLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RankCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(self, loader: Optional[RankValidationLoader] | None = None):
        """
        Args:
            loader: Optional[RankLoader]
        """
        super().__init__(loader=loader or RankValidationLoader())
    
    @property
    def loader(self) -> RankValidationLoader:
        return cast(RankValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> RankLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RankCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, persona, or arena are flagged unsafe.
            2.  Otherwise, send a RankCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RankCarrier]
        Raises:
            RankValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader fails.
        bootstrap = self.loader.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(RankPrimeExtract, bootstrap.authorization_applicant)
        carrier = extract.reference
        fingerprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Handle the case that the persona is missing. ---#
        persona_validation = self.loader.priming_validator.execute(
            candidate=fingerprint.persona,
            target_model=self.loader.toolkit.types.model,
            null_exception=self.loader.toolkit.nulls.model,
        )
        if persona_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=persona_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        persona = cast(Persona, persona_validation.authorization_applicant)

        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Rank.
        if extract.recipient_wants_model:
            model = Rank(persona)
            payload=RankCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a RankBuilder that needs a Blueprint.
        blueprint = RankBlueprint(persona)
        blueprint.mark_as_validated()
        payload = RankCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)


