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
from assurance import ModelValidator, SquareValidatorToolkit
from domain import Board, Coord, Formation, Square, SquareBlueprint, SquareValidationRequest
from err import (
    SquareCarrierEmptyException, SquareValidationRequestNullException, SquareValidatorException
)
from transit import SquareCarrier
from util import LoggingLevelRouter


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
            SquareCarrierEmptyException
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
        id_test = self.toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_coord_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        # Handle the case that the name does not pass a validation check.
        name_test = self.toolkit.helper.identity_service.validate_name(
            candidate=blueprint.name
        )
        if name_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=name_test.exception,
                )
            )
        # Handle the case that the board does not pass a validation check.
        board_test = self.toolkit.helper.board_validator.execute(
            candidate=blueprint.board
        )
        if board_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=board_test.exception,
                )
            )
        # Handle the case that the coord does not pass a validation check.
        coord_test = self.toolkit.helper.coord_validator.execute(
            candidate=blueprint.coord
        )
        if coord_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=coord_test.exception,
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        name = cast(str, name_test.payload)
        board = cast(Board, board_test.payload)
        coord = cast(Coord, coord_test.payload)
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case
        if carrier.is_carrying_model:
            model = Square(id=id, name=name, board=board, coord=coord)
            model.occupant = blueprint.occupant
            model.state = blueprint.state
            return ValidationResult.success(
                SquareCarrier(
                    model=Square(
                        id=id,
                        board=board,
                        coord=coord,
                    )
                )
            )
        # The blueprint case
        return ValidationResult.success(
            SquareCarrier(
                blueprint=SquareBlueprint(
                    id=id,
                    board=board,
                    coord=coord,
                )
            )
        )
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: SquareToolkit

    Provides:
        - execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Validator
    """
    
    def __init__(
            self,
            toolkit: SquareToolkit | None = SquareToolkit()
    ):
        """
        Args:
            toolkit: SquareToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> SquareToolkit:
        return cast(SquareToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a SquareBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The validation_priming fails.
                    - Either the board, coord or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            SquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            target_model=SquareCarrier,
            null_exception=SquareCarrierNullException()
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
        carrier = cast(SquareCarrier, carrier_validation.payload)
        if carrier.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=SquareCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierNullException.MSG,
                        err_code=SquareCarrierNullException.ERR_CODE,
                    ),
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that any id in the blueprint is flagged.
        id_test = self.toolkit.helper.identity_service.validate_blueprint_id(
            coord_blueprint=blueprint,
            coord_name=blueprint.domain_class_name,
        )
        if id_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        name_test = self.toolkit.helper.identity_service.validate_name.execute(
            candidate=blueprint.name,
        )
        if name_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=name_test.exception,
                )
            )
        # Handle the case that square.coord is not safe.
        coord_test = self.toolkit.coord_validator.execute(blueprint.coord)
        if coord_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=coord_test.exception,
                )
            )
        # Handle the case that square.board does not pass a validation check.
        board_test = self.toolkit.board_validator.execute(blueprint.board)
        if board_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=board_test.exception,
                )
            )

        formation = None
        if carrier.is_home_square_carrier:
            formation_test = self.toolkit.helper.priming_validator.execute(
                candidate=blueprint.formation,
                target_model=Formation,
                null_exception=FormationNullException()
            )
            if formation_test.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareValidatorException.MSG,
                        err_code=SquareValidatorException.ERR_CODE,
                        ex=formation_test.exception,
                    )
                )
            formation = cast(Formation, formation_test.payload)
            
            
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        name = cast(str, name_test.payload)
        board = cast(Board, board_test.payload)
        coord = cast(Coord, coord_test.payload)
        
        
        if carrier.is_home_square_carrier:
            return ValidationResult.success(
                HomeSquare(
                    id=id,
                    name=name,
                    board=board,
                    coord=coord,
                    formation=formation,
                )
            )
        if carrier.is_carrying_model:
            return ValidationResult.success(
                Square(
                    id=id,
                    name=name,
                    board=board,
                    coord=coord,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            SquareBlueprint(
                id=id,
                name=name,
                board=board,
                coord=coord,
                formation=formation,
            )
        )