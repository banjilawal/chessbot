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
from assurance import CoordLoader, CoordValidatorToolkit, ModelValidator
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
            loader: Optional[CoordLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[CoordLoader]
        """
        super().__init__(loader=loader or CoordLoader())
        
    @property
    def loader(self) -> CoordLoader:
        return cast(CoordLoader, super().loader)
    
    @property
    def toolkit(self) -> CoordValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordCarrier]:
        """
        Assure a candidate is a safe CoordCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a CoordValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a CoordCarrier
                            an empty CoordCarrier.
                    -   Either the board, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordCarrier]
        Raises:
            CoordValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
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
        prime_extract = cast(CoordPrimeExtract, loading.payload)
        carrier = prime_extract.reference
        blueprint = carrier.extract_blueprint()
        
        if blueprint is None:
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
        board_validation = self.toolkit.wrapper.board.extract_model(
            request=BoardValidationRequest(
                item=BoardCarrier(model=blueprint.board),
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
        for number in [blueprint.row, blueprint.column]:
            # Handle the case that any coord component in the blueprint is flagged.
            validation = self.toolkit.wrapper.number_validator.execute(number)
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
        if carrier.has_model:
            payload = CoordCarrier(
                model=Coord(
                    board=board,
                    row=row,
                    column=column
                )
            )
            return ValidationResult.success(payload)
        # Otherwise, the client is a CoordBuilder that needs a Blueprint.
        payload = CoordCarrier(
            blueprint=CoordBlueprint(
                board=board,
                row=row,
                column=column
            )
        )
        return ValidationResult.success(payload)



