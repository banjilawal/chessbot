# src/assurance/validator/model/token/position/validator.py

"""
Module: assurance.validator.model.token.position.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from artifcat import ValidationResult
from assurance import TokenPositionTable, TokenValidatorToolkit
from domain import Coord, TokenBlueprint
from err import TokenPositionTableGeneratorException
from exchange import CoordValidationRequest
from transit import CoordCarrier
from util import IdFactory, LoggingLevelRouter


class TokenPositionTableGenerator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenBlueprint position and previous_positions fields
            are safe to use.

    Attributes:
        toolkit: TokenValidatorToolkit

    Provides:
        -   def execute(
                    blueprint: TokenBlueprint
            ) -> ValidationResult[TokenPositionTable]:

    Super Class:
    """
    _toolkit: TokenValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
        """
        self._toolkit = toolkit or TokenValidatorToolkit()

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: TokenBlueprint,
    ) -> ValidationResult[TokenPositionTable]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   blueprint.position or
                    -   blueprint.previous_postion
                is not null and gets flagged.
            2.  Otherwise, for the success result, send a dictionary that is:
                    -   Empty if the Token has not been deployed.
                    -   Any validated position.
        Args:
            blueprint: TokenBlueprint
        Returns:
            ValidationResult[TokenPositionTable]
        Raises:
            TokenPositionValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        valid_locations: Dict[str, Coord] = {}
        # If the token has not been deployed send an empty dictionary
        if (
                blueprint.position is None and 
                blueprint.previous_position is None
        ):
            return ValidationResult.success(valid_locations)
        
        if blueprint.position is not None:
            # Handle the case that the position is flagged.
            validation = self._toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=blueprint.position),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenPositionTableGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPositionTableGeneratorException.MSG,
                        err_code=TokenPositionTableGeneratorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Otherwise add to the dictionary.
            valid_locations["position"] = cast(Coord, validation.payload)
        
        if blueprint.previous_position is not None:
            # Handle the case that the previous position is flagged.
            validation = self._toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=blueprint.previous_position),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenPositionTableGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPositionTableGeneratorException.MSG,
                        err_code=TokenPositionTableGeneratorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Otherwise add to the dictionary.
            valid_locations["previous_position"] = cast(Coord, validation.payload)
        # --- Send the work product. ---#
        position_table = TokenPositionTable(
            position=valid_locations["position"] or None,
            previous_position=valid_locations["previous_position"] or None,
        )
        return ValidationResult.success(position_table)
    