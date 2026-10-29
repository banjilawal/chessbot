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
from assurance import ModelValidator
from bootstrap import GameValidationLoader
from domain import Arena, Game, GameBlueprint, GamePrimeExtract, Persona, PlayerBinder
from err import (
    ArenaNullException, EmptyItemException, GameCarrierEmptyException, GameValidatorException,
    PlayerBinderConsistencyException, PlayerBinderNullException
)
from transit import GameCarrier
from util import LoggingLevelRouter


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
    
    def __init__(self, loader: Optional[GameValidationLoader] | None = None):
        """
        Args:
            loader: Optional[GameLoader]
        """
        super().__init__(loader=loader or GameValidationLoader())
    
    @property
    def loader(self) -> GameValidationLoader:
        return cast(GameValidationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[GameCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, binder, or arena are flagged unsafe.
            2.  Otherwise, send a GameCarrier in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[GameCarrier]
        Raises:
            GameValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader fails.
        bootstrap = self.loader.execute(item)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(GamePrimeExtract, bootstrap.payload)
        carrier = extract.reference
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
        id_validation = self.loader.toolkit.blueprint_id_extractor.execute(
            candidate=fingerprint,
            blueprint_owner_name=fingerprint.domain_class_name,
            blueprint_type=self.loader.toolkit.types.blueprint,
            blueprint_null_exception=self.loader.toolkit.nulls.blueprint,
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
        # --- Handle the case that the binder is null or the wrong type. ---#
        binder_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.binder,
            target_model=PlayerBinder,
            null_exception=PlayerBinderNullException(),
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
        # --- Handle the case that the arena is null or the wrong type. ---#
        arena_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.arena,
            target_model=Arena,
            null_exception=ArenaNullException(),
        )
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
        
        # Handle the case that there are no players.
        if binder.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=EmptyItemException(),
                )
            )
        # Handle the case that the are player inconsistencies.
        if binder.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=PlayerBinderConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerBinderConsistencyException.MSG,
                        err_code=PlayerBinderConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#

        # The client wants a safe Maneuver.
        if extract.recipient_wants_model:
            model = Game(id=id, arena=arena, binder=binder)
            payload = GameCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a GameBuilder that needs a blueprint.
        blueprint = GameBlueprint(id=id, arena=arena, binder=binder)
        payload = GameCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)


