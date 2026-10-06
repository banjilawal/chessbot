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
from domain import Formation, PublicSquare, PublicSquareBlueprint
from err import FormationNullException, EmptyPublicSquareCarrierException, PublicSquareValidatorException
from transit import PublicSquareCarrier
from util import LoggingLevelRouter


class PublicSquareValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareCarrier is safe to use.

    Attributes:
        loader: SquareValidatorToolkit

    Provides:
        -   def execute(candidate: SquareValidationRequest) -> ValidationResult[SquareCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[SquareValidatorToolkit] | None = None,
    ):
        """
        Args:
            loader: Optional[SquareValidatorToolkit]
        """
        self._toolkit =toolkit or SquareValidatorToolkit()

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            public_square_id: int,
            validated_carrier: PublicSquareCarrier,
    ) -> ValidationResult[PublicSquareCarrier]:
        """
        Certify a SquareCarrier's payload is either a Square or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a SquareValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a SquareCarrier
                            an empty SquareCarrier.
                    -   Either the id, board, or coord attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            public_square_id: int
            validated_carrier: PublicSquareCarrier
        Returns:
            ValidationResult[PublicSquareCarrier]
        Raises:
            PublicSquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PublicSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PublicSquareValidatorException.MSG,
                    err_code=PublicSquareValidatorException.ERR_CODE,
                    ex=EmptyPublicSquareCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyPublicSquareCarrierException.MSG,
                        err_code=EmptyPublicSquareCarrierException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the formation does not pass a validation check.
        formation_validation = self._toolkit.wrapper.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PublicSquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PublicSquareValidatorException.MSG,
                    err_code=PublicSquareValidatorException.ERR_CODE,
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
        if validated_carrier.has_model:
            model = PublicSquare(
                name=name,
                board=board,
                coord=coord,
                id=public_square_id,
                formation=formation,
            )
            model.occupant = occupant
            model.state = state
            return ValidationResult.success(
                PublicSquareCarrier(model=model)
            )
        # The blueprint case
        return ValidationResult.success(
            PublicSquareCarrier(
                blueprint=PublicSquareBlueprint(
                    name=name,
                    board=board,
                    coord=coord,
                    state=state,
                    occupant=occupant,
                    id=public_square_id,
                    formation=formation,
                )
            )
        )