# src/assurance/validator/model/board/validator.py

"""
Module: assurance.validator.model.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator
from bootstrap import BoardValidationLoader
from domain import Arena, Board, BoardBlueprint, BoardPrimeExtract, BoardState, TeamBinder
from err import (
    ArenaConsistencyException, ArenaNullException, BoardCarrierEmptyException, BoardStateNullException,
    BoardValidatorException,
    ConsistencyException, TeamBinderConsistencyException, TeamBinderNullException
)
from transit import BoardCarrier
from util import LoggingLevelRouter


class BoardValidator(ModelValidator[Board]):
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
        ModelValidator
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
            2.  Otherwise, send the recipient a carrier which has either a safe model or
                blueprint in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[BoardCarrier]
        Raises:
            BoardValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(item)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(BoardPrimeExtract, loading.payload)
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
        id_validation = self.loader.toolkit.blueprint_id_extractor.execute(
            item=fingerprint,
            blueprint_owner_name=fingerprint.domain_class_name,
            blueprint_type=self.loader.toolkit.manifest.types.blueprint,
            blueprint_null_exception=self.loader.toolkit.manifest.nulls.blueprint,
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
        state_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.validation_state,
            target_model=BoardState,
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
        arena_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.arena,
            target_model=Arena,
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
        binder_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.binder,
            target_model=TeamBinder,
            null_exception=TeamBinderNullException(),
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
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        arena = cast(Arena, arena_validation.payload)
        binder = cast(TeamBinder, binder_validation.payload)
        
        # Handle the case that there are no teams.
        if binder.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=EmptyItemException(),
                )
            )
        # Handle the case that the are team inconsistencies.
        if binder.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=TeamBinderConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamBinderConsistencyException.MSG,
                        err_code=TeamBinderConsistencyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that there is a board-arena inconsistency.
        model = Board(id=id, arena=arena, binder=binder)
        if model != arena.board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=ConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg="Inconsistency between board and arena",
                        err_code=ArenaConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants a safe Board.
        if extract.recipient_wants_model:
            payload = BoardCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a BoardBuilder that needs a Blueprint.
        blueprint = BoardBlueprint(id=id, arena=arena, binder=binder)
        blueprint.mark_as_validated()
        payload = BoardCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)



