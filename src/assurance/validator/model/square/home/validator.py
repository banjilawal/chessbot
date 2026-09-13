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
from assurance import SquareValidator, SquareValidatorToolkit
from domain import (
    Board, Coord, Formation, HomeSquare, HomeSquareBlueprint, Square, SquareBlueprint,
    SquareValidationRequest
)
from err import (
    FormationNullException, SquareCarrierEmptyException, SquareValidationRequestNullException, SquareValidatorException
)
from transit import HomeSquareCarrier, SquareCarrier
from util import LoggingLevelRouter


class HomeSquareValidator(SquareValidator):
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
        SquareValidator
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
    def execute(self, carrier: HomeSquareCarrier) -> ValidationResult[HomeSquareCarrier]:
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
            carrier: HomeSquareCarrier
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
            HomeSquareCarrier,
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
            blueprint_coord_name=blueprint.domain_class_name,
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
        # Handle the case that the board does not pass a validation check.
        board_validation = self.toolkit.helper.board_validator.execute(
            candidate=blueprint.board
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
        # Handle the case that the coord does not pass a validation check.
        coord_validation = self.toolkit.helper.coord_validator.execute(
            candidate=blueprint.coord
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
        # Handle the case that the request payload is null or the wrong type.
        formation_validation = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException,
        )
        
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_validation.payload)
        name = cast(str, name_validation.payload)
        board = cast(Board, board_validation.payload)
        coord = cast(Coord, coord_validation.payload)
        formation = cast(Formation, formation_validation.payloado)
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case
        if carrier.is_carrying_model:
            model = HomeSquare(
                id=id,
                name=name,
                board=board, coord=coord,
                formation=formation,
            )
            model.occupant = blueprint.occupant
            model.state = blueprint.state
            return ValidationResult.success(
                HomeSquareCarrier(model=model)
            )
        # The blueprint case
        return ValidationResult.success(
            HomeSquareCarrier(blueprint=blueprint)
        )
 