# src/assurance/root/validator/token/coord/validator.py

"""
Module: assurance.root.validator.token.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import TokenValidatorToolkit, Validator
from domain import Coord, ParticipantCoordChart
from err import StructureNullException, ParticipantCoordChartValidatorException
from exchange import CoordValidationRequest
from transit import CoordCarrier
from util import IdFactory, LoggingLevelRouter


class ParticipantCoordChartValidator(Validator[ParticipantCoordChart]):
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
    def execute(self, candidate: Any) -> ValidationResult[ParticipantCoordChart]:
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
        
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=Type[ParticipantCoordChart],
            null_exception=StructureNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipantCoordChartValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipantCoordChartValidatorException.MSG,
                    err_code=ParticipantCoordChartValidatorException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        candidate_chart = cast(ParticipantCoordChart, priming.payload)
        # Handle the case that the position_chart has an inconsistency.
        if candidate_chart.is_not_consistent:
            # Send the exception chain on failure.
            validation_result = ValidationResult.failure(
                ParticipantCoordChartValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipantCoordChartValidatorException.MSG,
                    err_code=ParticipantCoordChartValidatorException.ERR_CODE,
                    ex=ParticiantCoordChartConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticiantCoordChartConsistencyException.MSG,
                        err_code=ParticiantCoordChartConsistencyException.ERR_CODE,
                    ),
                )
            )
        position = candidate_chart.position
        if candidate_chart.position_exists:
            coord_validation = self._coord_check_runner(candidate_chart.position)
            if coord_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    ParticipantCoordChartValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipantCoordChartValidatorException.MSG,
                        err_code=ParticipantCoordChartValidatorException.ERR_CODE,
                        ex=coord_validation.exception,
                    )
                )
            position = cast(Coord, coord_validation.payload)
        previous_position = candidate_chart.previous_position
        if candidate_chart.previous_position.exists:
            coord_validation = self.toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=candidate_chart.previous_position),
                    id=IdFactory.next_id(class_name="CoordValidationRequest")
                )
            )
            if coord_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    ParticipantCoordChartValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipantCoordChartValidatorException.MSG,
                        err_code=ParticipantCoordChartValidatorException.ERR_CODE,
                        ex=coord_validation.exception,
                    )
                )
            previous_position = cast(Coord, coord_validation.payload)
        # --- Send the work product. ---#
        carrier = ParticipantCoordChartCarrier(
            model=articipantCoordChart(
                position=position,
                previous_position=previous_position,
            )
        )
        return ValidationResult.success(carrier)
    
    @LoggingLevelRouter.monitor
    def _coord_check_runner(self, coord_candidate: Any) -> ValidationResult[Coord]:
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
                ParticipantCoordChartValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipantCoordChartValidatorException.MSG,
                    err_code=ParticipantCoordChartValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Send the work product. ---#
        coord = cast(Coord, validation.payload)
        return ValidationResult.success(coord)
        
    