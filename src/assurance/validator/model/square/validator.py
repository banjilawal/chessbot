# src/assurance/validator/model/square/assurance/validator/model.py

"""
Module: assurance.validator.model.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import HomeSquareValidator, ModelValidator, SquareValidatorToolkit
from domain import (
    Board, BoardValidationRequest, Coord, CoordValidationRequest, Formation, Square, SquareBlueprint,
    SquareState, SquareValidationRequest
)
from err import (
    BoardCarrierEmptyException, CoordCarrierEmptyException, NullException, SquareCarrierEmptyException,
    SquareValidationRequestNullException,
    SquareValidatorException
)
from transit import BoardCarrier, CoordCarrier, HomeSquareCarrier, SquareCarrier
from util import IdFactory, LoggingLevelRouter


class SquareValidator(ModelValidator[Square]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: SquareValidationToolkit

    Provides:
        *   def execute(request: SquareValidationRequest) -> ValidationResult[SquareCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[SquareValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareValidationToolkit]
        """
        super().__init__(toolkit=toolkit or SquareValidatorToolkit())
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return cast(
            SquareValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: SquareValidationRequest) -> ValidationResult[SquareCarrier]:
        """
        Certify a SquareCarrier's payload is either a Square or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a SquareValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a SquareCarrier
                            an empty SquareCarrier.
                    *   Either the id, board, or coord attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            request: SquareValidationRequest
        Returns:
            ValidationResult[SquareCarrier]
        Raises:
            SquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=SquareValidationRequest,
            null_exception=SquareValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(SquareValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            SquareCarrier,
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
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
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the name does not pass a validation check.
        name_validation = self.toolkit.helper.identity_service.validate_name(
            candidate=blueprint.name
        )
        if name_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=name_validation.exception,
                )
            )
        # Handle the case that the state is null or the wrong type.
        state_validation = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.state,
            target_model=SquareState,
            null_exception=NullException(),
        )
        if state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=state_validation.exception,
                )
            )
        # Handle the case that the board does not pass a validation check.
        board_validation = self.toolkit.helper.board_validator.execute(
            request=BoardValidationRequest(
                id=IdFactory.next_id(class_name="BoardValidationRequest"),
                item=BoardCarrier(model=blueprint.board),
            )
        )
        if board_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        board_carrier = cast(BoardCarrier, board_validation.payload)
        if not board_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the coord does not pass a validation check.
        coord_validation = self.toolkit.helper.coord_validator.execute(
            request=CoordValidationRequest(
                id=IdFactory.next_id(class_name="CoordValidationRequest"),
                item=CoordCarrier(model=blueprint.coord),
            )
        )
        if coord_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=coord_validation.exception,
                )
            )
        coord_carrier = cast(CoordCarrier, coord_validation.payload)
        if not coord_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        if isinstance(carrier, HomeSquareCarrier):
            helper = HomeSquareValidator()
            return helper.execute(carrier)
        
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_validation.payload)
        name = cast(str, name_validation.payload)
        state = cast(SquareState, state_validation.payload)
        board = cast(Board, board_carrier.entity)
        coord = cast(Coord, coord_carrier.entity)
        occupant = blueprint.occupant
        
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.is_carrying_model:
            model = Square(id=id, name=name, board=board, coord=coord)
            model.occupant = occupant
            model.state = state
            return ValidationResult.success(
                SquareCarrier(model=model)
            )
        # The blueprint case
        return ValidationResult.success(
            SquareCarrier(
                blueprint=SquareBlueprint(
                    id=id,
                    name=name,
                    board=board,
                    coord=coord,
                    state=state,
                    occupant=occupant,
                )
            )
        )