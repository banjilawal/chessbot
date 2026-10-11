# src/assurance/validator/model/board/validator.py

"""
Module: assurance.validator.model.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from artifcat import ValidationResult
from assurance import BoardLoader, BoardValidatorToolkit, ModelValidator
from domain import Arena, Board, BoardBlueprint, BoardPrimeExtract
from err import BoardCarrierEmptyException, BoardValidatorException
from exchange import ArenaValidationRequest
from transit import ArenaCarrier, BoardCarrier
from util import IdFactory, LoggingLevelRouter


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
            loader: Optional[BoardLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[BoardLoader]
        """
        super().__init__(loader=loader or BoardLoader())
        
    @property
    def loader(self) -> BoardLoader:
        return cast(BoardLoader, super().loader)
    
    @property
    def toolkit(self) -> BoardValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[BoardCarrier]:
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
            candidate: Any
        Returns:
            ValidationResult[BoardCarrier]
        Raises:
            BoardValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
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
        prime_extract = cast(BoardPrimeExtract, loading.payload)
        reference = prime_extract.reference
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
        # --- PROCESS_THE_ARENA_ATTRIBUTE. ---#
        arena_validation = self.toolkit.wrapper.arena.extract_model(
            request=ArenaValidationRequest(
                item=ArenaCarrier(model=fingerprint.arena),
                id=IdFactory.next_id(class_name="ArenaValidationRequest"),

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
        # --- PROCESS_THE_ROW_AND_COLUMN_ATTRIBUTES. ---#
        components: List[int] = []
        for number in [fingerprint.row, fingerprint.column]:
            # Handle the case that any board component in the blueprint is flagged.
            validation = self.toolkit.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    BoardValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardValidatorException.MSG,
                        err_code=BoardValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            components.append(cast(int, validation.payload))
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        arena = cast(Arena, arena_validation.payload)
        row = components[0]
        column = components[1]
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants a safe Board.
        if prime_extract.recipient_wants_model:
            model = Board(arena=arena, row=row, column=column)
            carrier = BoardCarrier(model=model)
            return ValidationResult.success(carrier)
        # Otherwise, the client is a BoardBuilder that needs a Blueprint.
        blueprint = BoardBlueprint(board=board, row=row, column=column)
        carrier = BoardCarrier(blueprint=blueprint)
        return ValidationResult.success(carrier)



