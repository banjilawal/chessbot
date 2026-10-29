# src/assurance/validator/context/board/validator.py

"""
Module: assurance.validator.context.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import BoardValidationLoader, BoardLayerToolkit, ContextValidator
from domain import Arena, Board, BoardBlueprint, BoardPrimeExtract, BoardState, TeamBinder
from err import (
    ArenaConsistencyException, ArenaNullException, BoardCarrierEmptyException,
    BoardStateNullException, BoardValidatorException
)
from exchange import TeamBinderValidationRequest
from transit import BoardCarrier, TeamBinderCarrier
from util import IdFactory, LoggingLevelRouter


class BoardValidator(ContextValidator[Board]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a BoardCarrier and its contents are safe to use.

    Attributes:
        loader: BoardLoader

    Provides:
        -   def execute(candidate: Ant) -> ValidationResult[BoardCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            loader: Optional[BoardValidationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[BoardLoader]
        """
        super().__init__(loader=loader or BoardValidationLoader())
        
    @property
    def loader(self) -> BoardValidationLoader:
        return cast(BoardValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> BoardLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[BoardCarrier]:
        """
        Assure a candidate is a safe BoardCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate cannot be loaded as a BoardValidationRequest.
                    -   A BoardBlueprint cannot be extracted from the request.
                    -   Either the:
                        -   board
                        -   row
                        -   column
                    attributes are flagged unsafe.
            2.  Otherwise, send the recipient a carrier which has either a safe context or
                blueprint in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[BoardCarrier]
        Raises:
            BoardValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(item)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(BoardPrimeExtract, bootstrap.payload)
        reference = extract.reference
        fingerprint = reference.extract_blueprint()
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
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
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- PROCESS_THE_BOARD_STATE_ATTRIBUTE. ---#
        # Handle the case that the archetype does not pass a validation check.
        state_validation = self.toolkit.priming_validator.execute(
            candidate=fingerprint.validation_state,
            target_context=BoardState,
            null_exception=BoardStateNullException(),
        )
        if state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=state_validation.exception,
                )
            )
        # --- PROCESS_THE_ARENA_ATTRIBUTE. ---#
        arena_validation = self.toolkit.priming_validator.execute(
            candidate=fingerprint.arena,
            target_context=Arena,
            null_exception=ArenaNullException(),
        )
        if arena_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=arena_validation.exception,
                )
            )
        # --- PROCESS_THE_BOARD_BINDER_ATTRIBUTE. ---#
        binder_validation = self.toolkit.dependency.binder.extract_context.execute(
            item=TeamBinderValidationRequest(
                item=TeamBinderCarrier(context=fingerprint.binder),
                id=IdFactory.next_id(class_name="TeamBinderValidationRequest")
            )
        )
        if binder_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=binder_validation.exception,
                )
            )
        # Handle the case that the board is flagged.
        if arena_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=arena_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        arena = cast(Arena, arena_validation.payload)
        binder = cast(TeamBinder, binder_validation.payload)
        
        context = Board(id=id, arena=arena, binder=binder)
        if context != arena.board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=ArenaConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ArenaConsistencyException.MSG,
                        err_code=ArenaConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants a safe Board.
        if extract.recipient_wants_model:
            carrier = BoardCarrier(model=model)
            return ValidationResult.success(carrier)
        # Otherwise, the client is a BoardBuilder that needs a Blueprint.
        blueprint = BoardBlueprint(id=id, arena=arena, binder=binder)
        carrier = BoardCarrier(blueprint=blueprint)
        return ValidationResult.success(carrier)



