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
from assurance import ModelValidator, TeamValidatorToolkit
from domain import Archetype, Board, Player, Team, TeamValidationRequest
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
        - def execute(request: TeamValidationRequest) -> ValidationResult[TeamCarrier]:

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
    def execute(
            self,
            request: TeamValidationRequest
    ) -> ValidationResult[TeamCarrier]:
        """
        Certify a candidate is a TeamCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a TeamCarrier or its null.
                    -   The candidate is an empty TeamCarrier.
                    -   Either the
                            -   id
                            -   board
                            -   owner
                        attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            request: TeamValidationRequest
        Returns:
            ValidationResult[TeamCarrier]
        Raises:
            TeamValidatorException
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
        id_test = self.toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        # Handle the case that the board does not pass a validation check.
        board_test = self.toolkit.helper.board_validator.execute(
            candidate=blueprint.board
        )
        if board_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=board_test.exception,
                )
            )
        # Handle the case that the owner does not pass a validation check.
        owner_test = self.toolkit.helper.owner_validator.execute(
            candidate=blueprint.owner
        )
        if owner_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=owner_test.exception,
                )
            )
        # Handle the case that the archetype does not pass a validation check.
        archetype_test = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.archetype,
            target_model=Archetype,
            null_exception=ArchetypeNullException(),
        )
        if archetype_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=archetype_test.exception,
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        board = cast(Board, board_test.payload)
        owner = cast(Player, owner_test.payload)
        archetype = cast(Archetype, archetype_test.payload)
        
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

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a TeamBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The validation_priming fails.
                    - Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            TeamValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the validator is not primed.
        priming_result = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            blueprint_model=self.toolkit.blueprint_model,
            blueprint_null_exception=self.toolkit.blueprint_null_exception,
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into TeamBlueprint for routing attribute testing ---#
        blueprint = cast(TeamBlueprint, candidate)
        
        # Handle the case that the blueprint's id does not pass.
        id_validation_result = self.toolkit.blueprint_id_validator.execute(
            candidate=blueprint.id,
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=id_validation_result.exception
                )
            )
        # Handle the case that the owner gets flagged.
        owner_validation_result = self.toolkit.player_validator.execute(blueprint.owner)
        if owner_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=owner_validation_result.exception
                )
            )
        # Handle the case that the board is not safe.
        board_validation_result = self.toolkit.board_validator.excute(blueprint.board)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=owner_validation_result.exception
                )
            )
        # Handle the case that the schema is not safe.
        schema_validation_result = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.schema,
            target_model=type[Archetype],
            null_exception=SchemaNullException(),
        )
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidatorException.MSG,
                    err_code=TeamValidatorException.ERR_CODE,
                    ex=owner_validation_result.exception
                )
            )
        id = cast(int, id_validation_result.payload)
        board = cast(Board, board_validation_result.payload)
        owner = cast(type(blueprint.id), owner_validation_result.payload)
        schema = cast(Archetype, schema_validation_result.payload)
        
        # On validation success forward the work product to the caller.
        return ValidationResult.success(
            TeamBlueprint(
                id=id,
                board=board,
                owner=owner,
                schema=schema
            )
        )
