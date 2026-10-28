# src/assurance/validator/context/ran/validator.py

"""
Module: assurance.validator.context.rank.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ContextValidator, RankValidationLoader, RankLayerToolkit
from domain import Arena, Rank, RankBlueprint, RankPrimeExtract, PlayerBinder
from err import RankCarrierEmptyException, RankValidatorException
from exchange import (
    ArenaValidationRequest, PlayerBinderValidationRequest
)
from transit import ArenaCarrier, PlayerBinderCarrier, RankCarrier
from util import IdFactory, LoggingLevelRouter


class RankValidator(ContextValidator[Rank]):
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
        ContextValidator
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
    def execute(self, item: Any) -> ValidationResult[RankCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, binder, or arena are flagged unsafe.
            2.  Otherwise, send a RankCarrier in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[RankCarrier]
        Raises:
            RankValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader fails.
        loading = self.loader.execute(item)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(RankPrimeExtract, loading.payload)
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
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            item=fingerprint,
            blueprint_owner_name=fingerprint.domain_class_name,
            blueprint_type=self.toolkit.manifest.types.blueprint,
            blueprint_null_exception=self.toolkit.manifest.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- Handle the case that the binder is not safe. ---#
        binder_validation = self.toolkit.dependency.binder.extract_context(
            request=PlayerBinderValidationRequest(
                item=PlayerBinderCarrier(context=fingerprint.binder),
                id=IdFactory.next_id(class_name="PlayerBinderValidationRequest"),
            )
        )
        if binder_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=binder_validation.exception,
                )
            )
        # --- Handle the case that the arena is not safe. ---#
        arena_validation = self.toolkit.dependency.arena.extract_context(
            request=ArenaValidationRequest(
                item=ArenaCarrier(context=fingerprint.arena),
                id=IdFactory.next_id(class_name="ArenaValidationRequest"),
            )
        )
        # Handle the case that the arena is flagged.
        if arena_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=arena_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        arena = cast(Arena, arena_validation.payload)
        binder = cast(PlayerBinder, binder_validation.payload)

        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Rank.
        if extract.recipient_wants_context:
            payload = Rank(
                id=id,
                binder=binder,
                arena=arena,
            )
            return ValidationResult.success(
                RankCarrier(context=payload)
            )
        # Otherwise, the client is a RankBuilder that needs a Blueprint.
        payload = RankBlueprint(
            id=id,
            binder=binder,
            arena=arena,
        )
        return ValidationResult.success(
            RankCarrier(blueprint=payload)
        )


