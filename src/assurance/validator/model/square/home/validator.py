# src/assurance/validator/model/square/assurance/validator/model.py

"""
Module: assurance.validator.model.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import SquareValidatorToolkit
from domain import Formation, HomeSquare, HomeSquareBlueprint
from err import FormationNullException, HomeSquareCarrierEmptyException, HomeSquareValidatorException
from transit import HomeSquareCarrier
from util import LoggingLevelRouter


class HomeSquareValidator:
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
        self._toolkit =toolkit or SquareValidatorToolkit()

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            home_square_id: int,
            validated_carrier: HomeSquareCarrier,
    ) -> ValidationResult[HomeSquareCarrier]:
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
            home_square_id: int
            validated_carrier: HomeSquareCarrier
        Returns:
            ValidationResult[HomeSquareCarrier]
        Raises:
            HomeSquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HomeSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareValidatorException.MSG,
                    err_code=HomeSquareValidatorException.ERR_CODE,
                    ex=HomeSquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeSquareCarrierEmptyException.MSG,
                        err_code=HomeSquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the formation does not pass a validation check.
        formation_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HomeSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeSquareValidatorException.MSG,
                    err_code=HomeSquareValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        name = blueprint.name
        state = blueprint.state
        board = blueprint.board
        coord = blueprint.coord
        occupant = blueprint.occupant
        formation = cast(Formation, formation_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if validated_carrier.is_carrying_model:
            model = HomeSquare(
                name=name,
                board=board,
                coord=coord,
                id=home_square_id,
                formation=formation,
            )
            model.occupant = occupant
            model.state = state
            return ValidationResult.success(
                HomeSquareCarrier(model=model)
            )
        # The blueprint case
        return ValidationResult.success(
            HomeSquareCarrier(
                blueprint=HomeSquareBlueprint(
                    name=name,
                    board=board,
                    coord=coord,
                    state=state,
                    occupant=occupant,
                    id=home_square_id,
                    formation=formation,
                )
            )
        )