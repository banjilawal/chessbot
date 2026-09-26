# src/assurance/validator/model/team/validator.py

"""
Module: assurance.validator.model.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import BoardValidationResponse, ValidationResult
from assurance import ModelValidator, TeamValidatorToolkit
from domain import (
    Archetype, Board, BoardValidationRequest, Player, PlayerValidationRequest, Team,
    TeamBlueprint, TeamValidationRequest
)
from err import (
    ArchetypeNullException, BoardValidatorResponseWrapperExceptionValidation, EmptyBoardCarrierException,
    EmptyPlayerCarrierException,
    EmptyTeamCarrierException, TeamValidationRequestNullException, TeamValidatorException
)
from transit import BoardCarrier, PlayerCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class TeamValidator(ModelValidator[Team]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamCarrier and its contents are safe before use.

    Attributes:
        toolkit: TeamValidatorToolkit

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TeamCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[TeamValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TeamValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TeamValidatorToolkit())
    
    @property
    def toolkit(self) -> TeamValidatorToolkit:
        return cast(TeamValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamCarrier]:
        """
        Certify a TeamCarrier's payload is either a Team or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a TeamValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a TeamCarrier
                            an empty TeamCarrier.
                    -   Either the id, board, or owner attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamCarrier]
        Raises:
            TeamValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        blueprint_load_result = self.toolkit.blueprint_loader.execute(candidate)
        if blueprint_load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=blueprint_load_result.exception,
                )
            )
        blueprint = cast(
            TeamBlueprint,
            blueprint_load_result.payload,
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
            candidate=BoardValidationRequest(
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
            candidate=PlayerValidationRequest(
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
        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        board = cast(Board, board_validation.payload)
        owner = cast(Player, owner_validation.payload)
        archetype = cast(Archetype, archetype_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.is_carrying_model:
            payload = Team(
                id=id,
                board=board,
                owner=owner,
                archetype=archetype,
            )
            return ValidationResult.success(TeamCarrier(model=payload))
        # The blueprint case
        payload = TeamBlueprint(
            id=id,
            board=board,
            owner=owner,
            archetype=archetype,
        )
        return ValidationResult.success(TeamCarrier(blueprint=payload))
