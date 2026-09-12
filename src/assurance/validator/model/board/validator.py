# src/assurance/validator/model/board/validator.py

"""
Module: assurance.validator.model.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelValidator, BoardValidatorToolkit
from domain import Board, BoardBlueprint, BoardValidationRequest
from err import (
    BoardCarrierEmptyException, BoardValidationRequestNullException, BoardValidatorException
)
from transit import BoardCarrier
from util import LoggingLevelRouter


class BoardValidator(ModelValidator[Board]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a BoardCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: BoardValidationToolkit

    Provides:
        - def execute(request: BoardValidationRequest) ->ValidationResult[BoardCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[BoardValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[BoardValidationToolkit]
        """
        super().__init__(toolkit=toolkit or BoardValidatorToolkit())
    
    @property
    def toolkit(self) -> BoardValidatorToolkit:
        return cast(
            BoardValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: BoardValidationRequest) -> ValidationResult[BoardCarrier]:
        """
        Certify a candidate is a BoardCarrier whose payload is either a Board
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a BoardCarrier or its null.
                    - The candidate is an empty BoardCarrier.
                    - Any Board attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[BoardCarrier]
        Raises:
            BoardValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=BoardValidationRequest,
            null_exception=BoardValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(BoardValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            Type[self.toolkit.metadata.types.carrier],
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that there is no blueprint.
        if blueprint is None:
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
        
        # Handle the case that any board component in the blueprint is flagged.
        numbers = []
        for number in [blueprint.x, blueprint.y]:
            validation = self.toolkit.helper.number_validator.execute(number)
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
            numbers.append(cast(int, validation.payload))
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case
        if carrier.is_carrying_model:
            return ValidationResult.success(
                BoardCarrier(
                    model=Board(
                        x=numbers[0],
                        y=numbers[1],
                    )
                )
            )
        # The blueprint case
        return ValidationResult.success(
            BoardCarrier(
                blueprint=BoardBlueprint(
                    x=numbers[0],
                    y=numbers[1],
                )
            )
        )