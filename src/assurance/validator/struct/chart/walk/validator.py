# src/assurance/validator/struct/chart/walk/validator.py

"""
Module: assurance.validator.struct.chart.walk.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import ChartValidator, WalkValidatorToolkit
from domain import Coord, WalkBlueprint, WalkPrimeExtract, Walk
from err import WalkConsistencyException, WalkValidatorException
from exchange import CoordValidationRequest
from transit import CoordCarrier, WalkCarrier
from util import IdFactory, LoggingLevelRouter


class WalkValidator(ChartValidator[Walk]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a WalkCarrier and its contents are safe to use.

    Attributes:
        toolkit: WalkValidatorToolkit

    Provides:
        -   execute(candidate: Any) -> ValidationResult[WalkCarrier]

    Super Class:
        ChartValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[WalkValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[WalkValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or WalkValidatorToolkit())
        
    @property
    def toolkit(self) -> WalkValidatorToolkit:
        return cast(WalkValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[WalkCarrier]:
        """
        Assure a candidate is a safe WalkCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   Loader fails.
                    -   The WalkBlueprint has an inconsistency.
                    -   The CoordValidator flags either existing position.
            2.  Otherwise, send the type of carrier prime_extract indicates.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Walk]
        Raises:
            WalkValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self.toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidatorException.MSG,
                    err_code=WalkValidatorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(WalkPrimeExtract, load_result.payload)
        blueprint = cast(WalkBlueprint, prime_extract.blueprint)
        
        # Handle the case that the walk has an inconsistency.
        if blueprint.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidatorException.MSG,
                    err_code=WalkValidatorException.ERR_CODE,
                    ex=WalkConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=WalkConsistencyException.MSG,
                        err_code=WalkConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- VALIDATE_THE_WALK_ENDPOINTS. ---#
        safe_coords: Dict[str, Coord] = {}
        candidate_points = blueprint.to_dict
        for key in candidate_points.keys():
            # Handle the case that a position is not a safe Coord.
            coord_validation = self.toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=candidate_points[key]),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if coord_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    WalkValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=WalkValidatorException.MSG,
                        err_code=WalkValidatorException.ERR_CODE,
                        ex=coord_validation.exception,
                    )
                )
            # Otherwise, the add value to the safe_coords.
            safe_coords[key] = cast(Coord, coord_validation.payload)
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants a safe Team.
        if prime_extract.recipient_wants_model:
            payload = WalkCarrier(
                model=Walk(
                    position=safe_coords["position"],
                    previous_position=safe_coords["previous_position"],
                )
            )
            return ValidationResult.success(payload)
        # Otherwise, the client is a WalkBuilder that needs a Blueprint.
        payload = WalkCarrier(
            blueprint=WalkBlueprint(
                position=safe_coords["position"],
                previous_position=safe_coords["previous_position"],
            )
        )
        return ValidationResult.success(payload)
    