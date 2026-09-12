# src/assurance/validator/model/coord/validator.py

"""
Module: assurance.validator.model.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, CoordValidatorToolkit
from domain import (
    Board, BoardValidationRequest, Coord, CoordBlueprint, CoordValidationRequest
)
from err import (
    BoardCarrierEmptyException, CoordValidationRequestNullException, CoordValidatorException
)
from transit import BoardCarrier, CoordCarrier
from util import IdFactory, LoggingLevelRouter


class CoordValidator(ModelValidator[Coord]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: CoordValidationToolkit

    Provides:
        *   def execute(request: CoordValidationRequest) -> ValidationResult[CoordCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[CoordValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[CoordValidationToolkit]
        """
        super().__init__(toolkit=toolkit or CoordValidatorToolkit())
    
    @property
    def toolkit(self) -> CoordValidatorToolkit:
        return cast(
            CoordValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: CoordValidationRequest) -> ValidationResult[CoordCarrier]:
        """
        Certify a CoordCarrier's payload is either a Coord or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a CoordValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a CoordCarrier
                            an empty CoordCarrier.
                    *   Either the board, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            request: CoordValidationRequest
        Returns:
            ValidationResult[CoordCarrier]
        Raises:
            CoordValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=CoordValidationRequest,
            null_exception=CoordValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(CoordValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            CoordCarrier,
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Run the board validation checks. ---#
        board_validation = self.toolkit.helper.board_validator.execute(
            request=BoardValidationRequest(
                id=IdFactory.next_id(class_name="BoardValidationRequest"),
                item=BoardCarrier(model=blueprint.board),
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
        # --- Extract the board validation payload. ---#
        board_carrier = cast(
            BoardCarrier,
            board_validation.payload
        )
        # Handle the case that the board_carrier does not contain a model.
        if not board_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorException.MSG,
                    err_code=CoordValidatorException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any coord component in the blueprint is flagged.
        components: List[int] = []
        for number in [blueprint.row, blueprint.column]:
            validation = self.toolkit.helper.number_validator.execute(number)
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
        # --- Extract validation payloads. ---#
        board = cast(Board, board_carrier.entity)
        row = components[0]
        column = components[1]
        # --- Forward the appropriate work product to the caller. ---#  
        # The model case
        if carrier.is_carrying_model:
            model = Coord(board=board, row=row, column=column)
            return ValidationResult.success(
                CoordCarrier(model=model)
            )
        # The blueprint case
        blueprint = CoordBlueprint(board=board, row=row, column=column)
        return ValidationResult.success(
            CoordCarrier(blueprint=blueprint)
        )

        



