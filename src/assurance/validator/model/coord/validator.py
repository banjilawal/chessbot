# src/assurance/validator/model/coord/validator.py

"""
Module: assurance.validator.model.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator
from bootstrap import CoordValidationLoader
from domain import Board, Coord, CoordBlueprint, CoordPrimeExtract
from err import CoordCarrierEmptyException, CoordValidatorException
from exchange import BoardValidationRequest
from transit import BoardCarrier, CoordCarrier
from util import IdFactory, LoggingLevelRouter


class CoordValidator(ModelValidator[Coord]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordCarrier and its contents are safe to use.

    Attributes:
        loader: CoordLoader

    Provides:
        -   def execute(candidate: Ant) -> ValidationResult[CoordCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[CoordValidationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[CoordLoader]
        """
        super().__init__(loader=loader or CoordValidationLoader())
        
    @property
    def loader(self) -> CoordValidationLoader:
        return cast(CoordValidationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[CoordCarrier]:
        """
        Assure a candidate is a safe CoordCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate cannot be loaded as a CoordValidationRequest.
                    -   A CoordBlueprint cannot be extracted from the request.
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
            ValidationResult[CoordCarrier]
        Raises:
            CoordValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(item)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(CoordPrimeExtract, loading.payload)
        reference = extract.reference
        fingerprint = reference.extract_blueprint()
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_BOARD_ATTRIBUTE. ---#
        board_validation = self.loader.toolkit.dependency.board.extract_model(
            request=BoardValidationRequest(
                item=BoardCarrier(model=fingerprint.board),
                id=IdFactory.next_id(class_name="BoardValidationRequest"),
            )
        )
        # Handle the case that the board is flagged.
        if board_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # --- PROCESS_THE_ROW_AND_COLUMN_ATTRIBUTES. ---#
        components: List[int] = []
        for number in [fingerprint.row, fingerprint.column]:
            # Handle the case that any coord component in the blueprint is flagged.
            validation = self.loader.toolkit.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CoordValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordValidatorException.MSG,
                        err_code=CoordValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            components.append(cast(int, validation.payload))
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        board = cast(Board, board_validation.payload)
        row = components[0]
        column = components[1]
        
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants a safe Coord.
        if extract.recipient_wants_model:
            model = Coord(board=board, row=row, column=column)
            payload = CoordCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a CoordBuilder that needs a Blueprint.
        blueprint = CoordBlueprint(board=board, row=row, column=column)
        blueprint.mark_as_validated()
        payload = CoordCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)



