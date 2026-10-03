# src/assurance/root/validator/token/coord/validator.py

"""
Module: assurance.root.validator.token.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import TokenPositionChart, TokenValidatorToolkit, Validator
from domain import Coord, TokenBlueprint
from err import CoordValidatorException, TokenPositionValidatorException
from exchange import CoordValidationRequest
from transit import CoordCarrier
from util import IdFactory, LoggingLevelRouter


class TokenPositionValidator(Validator[TokenPositionChart]):
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
            ) -> ValidationResult[TokenPositionChart]:

    Super Class:
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: TokenBlueprint,
    ) -> ValidationResult[TokenPositionChart]:
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
            ValidationResult[TokenPositionChart]
        Raises:
            TokenPositionValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        position_chart: TokenPositionChart = TokenPositionChart()
        # If the token has not been deployed send an empty dictionary
        if (
                blueprint.position is None and 
                blueprint.previous_position is None
        ):
            return ValidationResult.success(position_chart)
        
        position_validation = ValidationResult.failure(
            CoordValidatorException()
        )
        if blueprint.position is not None:
            # Handle the case that the position is flagged.
            position_validation = self._coord_check_runner(blueprint.position)
            if position_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenPositionValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPositionValidatorException.MSG,
                        err_code=TokenPositionValidatorException.ERR_CODE,
                        ex=position_validation.exception,
                    )
                )
        previous_position_validation = ValidationResult.failure(
            CoordValidatorException()
        )
        # Handle the case that the not-null previous_position is unsafe.
        if blueprint.previous_position is not None:
            # Handle the case that the previous position is flagged.
            previous_position_validation = self._coord_check_runner(blueprint.previous_position)
            if position_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenPositionValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPositionValidatorException.MSG,
                        err_code=TokenPositionValidatorException.ERR_CODE,
                        ex=previous_position_validation.exception,
                    )
                )
        # --- Send the work product. ---#
        position = cast(Coord, position_validation.payload)
        previous_position = cast(Coord, previous_position_validation.payload)
        position_table = TokenPositionChart(
            position=position or None,
            previous_position=previous_position or None,
        )
        return ValidationResult.success(position_table)
    
    @LoggingLevelRouter.monitor
    def _coord_check_runner(self, candidate: Any) -> ValidationResult[Coord]:
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
            ValidationResult[TokenPositionChart]
        Raises:
            TokenPositionValidatorException
        """
        method = f"{self.__class__.__name__}._coord_check_runner"
        
        # Handle the case that the candidate is flagged.
        validation = self.toolkit.wrapper.coord.extract_model(
            request=CoordValidationRequest(
                item=CoordCarrier(model=candidate),
                id=IdFactory.next_id(class_name="CoordValidationRequest"),
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenPositionValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPositionValidatorException.MSG,
                    err_code=TokenPositionValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Send the work product. ---#
        coord = cast(Coord, validation.payload)
        return ValidationResult.success(coord)
        
    