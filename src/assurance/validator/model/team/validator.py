# src/assurance/validator/model/team/validator.py

"""
Module: assurance.validator.model.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, TeamLoader, TeamValidatorToolkit
from domain import Archetype, Board, Player, Team, TeamBlueprint, TeamPrimeExtract
from err import ArchetypeNullException, TeamCarrierEmptyException, TeamValidatorException
from exchange import BoardValidationRequest, PlayerValidationRequest
from transit import BoardCarrier, PlayerCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class TeamValidator(ModelValidator[Team]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamCarrier and its contents are safe to use.

    Attributes:
        loader: TeamLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TeamCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(self, loader: Optional[TeamLoader] | None = None):
        """
        Args:
            loader: Optional[TeamLoader]
        """
        super().__init__(loader=loader or TeamLoader())
    
    @property
    def loader(self) -> TeamLoader:
        return cast(TeamLoader, super().loader)
    
    @property
    def toolkit(self) -> TeamValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, board, or owner are flagged unsafe.
            2.  Otherwise, send a TeamCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamCarrier]
        Raises:
            TeamValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TeamPrimeExtract, loading.payload)
        carrier = prime_extract.reference
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the archetype does not pass a validation check.
        archetype_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.archetype,
            target_model=Archetype,
            null_exception=ArchetypeNullException(),
        )
        if archetype_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=archetype_validation.exception,
                )
            )
        # --- Handle the case that the board is not safe. ---#
        board_validation = self.toolkit.wrapper.board.extract_model(
            request=BoardValidationRequest(
                item=BoardCarrier(model=blueprint.board),
                id=IdFactory.next_id(class_name="BoardValidationRequest"),
            )
        )
        if board_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # --- Handle the case that the owner is not safe. ---#
        owner_validation = self.toolkit.wrapper.owner.extract_model(
            request=PlayerValidationRequest(
                item=PlayerCarrier(model=blueprint.owner),
                id=IdFactory.next_id(class_name="PlayerValidationRequest"),
            )
        )
        # Handle the case that the owner is flagged.
        if owner_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=owner_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        board = cast(Board, board_validation.payload)
        owner = cast(Player, owner_validation.payload)
        archetype = cast(Archetype, archetype_validation.payload)
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Team.
        if prime_extract.recipient_wants_model:
            payload = Team(
                id=id,
                board=board,
                owner=owner,
                archetype=archetype,
            )
            return ValidationResult.success(
                TeamCarrier(model=payload)
            )
        # Otherwise, the client is a TeamBuilder that needs a Blueprint.
        payload = TeamBlueprint(
            id=id,
            board=board,
            owner=owner,
            archetype=archetype,
        )
        return ValidationResult.success(
            TeamCarrier(blueprint=payload)
        )

