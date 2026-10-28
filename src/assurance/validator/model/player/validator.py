# src/assurance/validator/model/player/validator.py

"""
Module: assurance.validator.model.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator
from bootstrap import PlayerValidationLoader
from domain import Account, Archetype, Game, Player, PlayerBlueprint, PlayerPrimeExtract
from err import (
    ArchetypeNullException, GameNullException, PlayerCarrierEmptyException, PlayerNotFoundException,
    PlayerValidatorException
)
from exchange import AccountValidationRequest
from transit import AccountCarrier, PlayerCarrier
from util import IdFactory, LoggingLevelRouter


class PlayerValidator(ModelValidator[Player]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerCarrier and its contents are safe to use.

    Attributes:
        loader: PlayerLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[PlayerCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(self, loader: Optional[PlayerValidationLoader] | None = None):
        """
        Args:
            loader: Optional[PlayerLoader]
        """
        super().__init__(loader=loader or PlayerValidationLoader())
    
    @property
    def loader(self) -> PlayerValidationLoader:
        return cast(PlayerValidationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[PlayerCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, account, or game are flagged unsafe.
            2.  Otherwise, send a PlayerCarrier in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[PlayerCarrier]
        Raises:
            PlayerValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader fails.
        loading = self.loader.execute(item)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(PlayerPrimeExtract, loading.payload)
        fingerprint = extract.reference.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the archetype does not pass a validation check.
        archetype_validation = self.loader.priming_validator.execute(
            item=fingerprint.archetype,
            target_model=Archetype,
            null_exception=ArchetypeNullException(),
        )
        if archetype_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=archetype_validation.exception,
                )
            )
        # Handle the case that the game does not pass a validation check.
        game_validation = self.loader.priming_validator.execute(
            item=fingerprint.game,
            target_model=Game,
            null_exception=GameNullException(),
        )
        if game_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=game_validation.exception,
                )
            )
        # --- Handle the case that the account is not safe. ---#
        account_validation = self.loader.dependency.account.extract_model(
            request=AccountValidationRequest(
                item=AccountCarrier(model=fingerprint.account),
                id=IdFactory.next_id(class_name="AccountValidationRequest"),
            )
        )
        if account_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=account_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        game = cast(Game, game_validation.payload)
        account = cast(Account, account_validation.payload)
        archetype = cast(Archetype, archetype_validation.payload)
        
        model = Player(game=game, account=account, archetype=archetype)
        if model not in game.binder.to_list:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=PlayerNotFoundException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerNotFoundException.MSG,
                        err_code=PlayerNotFoundException.ERR_CODE,
                    )
                )
            )
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Player.
        if extract.recipient_wants_model:
            payload = PlayerCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a PlayerBuilder that needs a Blueprint.
        blueprint = PlayerBlueprint(
            game=game,
            account=account,
            archetype=archetype,
        )
        blueprint.mark_as_validated()
        payload = PlayerCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)


