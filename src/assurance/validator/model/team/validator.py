# src/assurance/validator/model/team/validator.py

"""
Module: assurance.validator.model.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, TeamValidatorToolkit
from domain import Archetype, Board, Player, Team, TeamBlueprint, TeamValidationRequest
from err import (
    ArchetypeNullException, TeamCarrierEmptyException, TeamValidationRequestNullException,
    TeamValidatorException
)
from transit import TeamCarrier
from util import LoggingLevelRouter


class TeamValidator(ModelValidator[Team]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: TeamValidationToolkit

    Provides:
        *   def execute(request: TeamValidationRequest) -> ValidationResult[TeamCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[TeamValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TeamValidationToolkit]
        """
        super().__init__(toolkit=toolkit or TeamValidatorToolkit())
    
    @property
    def toolkit(self) -> TeamValidatorToolkit:
        return cast(
            TeamValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TeamValidationRequest) -> ValidationResult[TeamCarrier]:
        """
        Certify a TeamCarrier's payload is either a Team or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a TeamValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a TeamCarrier
                            an empty TeamCarrier.
                    *   Either the id, board, or owner attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            request: TeamValidationRequest
        Returns:
            ValidationResult[TeamCarrier]
        Raises:
            TeamValidatorException
            TeamCarrierEmptyException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=TeamValidationRequest,
            null_exception=TeamValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(TeamValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            TeamCarrier,
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
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
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.helper.blueprint_id_extractor.execute(
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
        # Handle the case that the board does not pass a validation check.
        board_validation = self.toolkit.helper.board_validator.execute(
            candidate=blueprint.board
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
        # Handle the case that the owner does not pass a validation check.
        owner_validation = self.toolkit.helper.owner_validator.execute(
            candidate=blueprint.owner
        )
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
        # Handle the case that the archetype does not pass a validation check.
        archetype_validation = self.toolkit.helper.priming_validator.execute(
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
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_validation.payload)
        board = cast(Board, board_validation.payload)
        owner = cast(Player, owner_validation.payload)
        archetype = cast(Archetype, archetype_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case
        if carrier.is_carrying_model:
            return ValidationResult.success(
                TeamCarrier(
                    model=Team(
                        id=id,
                        board=board,
                        owner=owner,
                        archetype=archetype,
                    )
                )
            )
        # The blueprint case
        return ValidationResult.success(
            TeamCarrier(
                blueprint=TeamBlueprint(
                    id=id,
                    board=board,
                    owner=owner,
                    archetype=archetype,
                )
            )
        )