# src/assurance/validator/model/game/validator.py

"""
Module: assurance.validator.model.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, GameLoader, GameValidatorToolkit
from domain import Arena, Game, GameBlueprint, GamePrimeExtract, PlayerBinder
from err import GameCarrierEmptyException, GameValidatorException
from exchange import (
    ArenaValidationRequest, PlayerBinderValidationRequest
)
from transit import ArenaCarrier, PlayerBinderCarrier, GameCarrier
from util import IdFactory, LoggingLevelRouter


class GameValidator(ModelValidator[Game]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a GameCarrier and its contents are safe to use.

    Attributes:
        loader: GameLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[GameCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(self, loader: Optional[GameLoader] | None = None):
        """
        Args:
            loader: Optional[GameLoader]
        """
        super().__init__(loader=loader or GameLoader())
    
    @property
    def loader(self) -> GameLoader:
        return cast(GameLoader, super().loader)
    
    @property
    def toolkit(self) -> GameValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[GameCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, binder, or arena are flagged unsafe.
            2.  Otherwise, send a GameCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[GameCarrier]
        Raises:
            GameValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader fails.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(GamePrimeExtract, loading.payload)
        carrier = prime_extract.reference
        fingerprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=fingerprint,
            blueprint_owner_name=fingerprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- Handle the case that the binder is not safe. ---#
        binder_validation = self.toolkit.wrapper.binder.extract_model(
            request=PlayerBinderValidationRequest(
                item=PlayerBinderCarrier(model=fingerprint.binder),
                id=IdFactory.next_id(class_name="PlayerBinderValidationRequest"),
            )
        )
        if binder_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=binder_validation.exception,
                )
            )
        # --- Handle the case that the arena is not safe. ---#
        arena_validation = self.toolkit.wrapper.arena.extract_model(
            request=ArenaValidationRequest(
                item=ArenaCarrier(model=fingerprint.arena),
                id=IdFactory.next_id(class_name="ArenaValidationRequest"),
            )
        )
        # Handle the case that the arena is flagged.
        if arena_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=arena_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        arena = cast(Arena, arena_validation.payload)
        binder = cast(PlayerBinder, binder_validation.payload)

        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Game.
        if prime_extract.recipient_wants_model:
            payload = Game(
                id=id,
                binder=binder,
                arena=arena,
            )
            return ValidationResult.success(
                GameCarrier(model=payload)
            )
        # Otherwise, the client is a GameBuilder that needs a Blueprint.
        payload = GameBlueprint(
            id=id,
            binder=binder,
            arena=arena,
        )
        return ValidationResult.success(
            GameCarrier(blueprint=payload)
        )


