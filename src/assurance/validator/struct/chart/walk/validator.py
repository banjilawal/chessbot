# src/assurance/validator/struct/chart/footstep/validator.py

"""
Module: assurance.validator.struct.chart.footstep.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import ChartValidator, FootstepLoader, FootstepValidatorToolkit
from domain import Coord, FootstepBlueprint, FootstepPrimeExtract, Footstep
from err import FootstepConsistencyException, FootstepValidatorException
from exchange import CoordValidationRequest
from transit import CoordCarrier, FootstepCarrier
from util import IdFactory, LoggingLevelRouter


class FootstepValidator(ChartValidator[Footstep]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a FootstepCarrier and its contents are safe to use.

    Attributes:
        loader: FootstepLoader

    Provides:
        -   execute(candidate: Any) -> ValidationResult[FootstepCarrier]

    Super Class:
        ChartValidator
    """
    
    def __init__(self, loader: Optional[FootstepLoader] | None = None):
        """
        Args:
            loader: Optional[FootstepLoader]
        """
        super().__init__(loader=loader or FootstepLoader())
        
    @property
    def loader(self) -> FootstepLoader:
        return cast(FootstepLoader, super().loader)
    
    @property
    def toolkit(self) -> FootstepValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[FootstepCarrier]:
        """
        Assure a candidate is a safe FootstepCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   Loader fails.
                    -   The FootstepBlueprint has an inconsistency.
                    -   The CoordValidator flags either existing position.
            2.  Otherwise, send the type of carrier prime_extract indicates.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Footstep]
        Raises:
            FootstepValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.toolkit.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidatorException.MSG,
                    err_code=FootstepValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(FootstepPrimeExtract, loading.payload)
        blueprint = cast(FootstepBlueprint, prime_extract.blueprint)
        
        # Handle the case that the footstep has an inconsistency.
        if blueprint.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidatorException.MSG,
                    err_code=FootstepValidatorException.ERR_CODE,
                    ex=FootstepConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepConsistencyException.MSG,
                        err_code=FootstepConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- VALIDATE_THE_FOOTSTEP_ENDPOINTS. ---#
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
                    FootstepValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepValidatorException.MSG,
                        err_code=FootstepValidatorException.ERR_CODE,
                        ex=coord_validation.exception,
                    )
                )
            # Otherwise, the add value to the safe_coords.
            safe_coords[key] = cast(Coord, coord_validation.payload)
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants a safe Team.
        if prime_extract.recipient_wants_model:
            payload = FootstepCarrier(
                model=Footstep(
                    position=safe_coords["position"],
                    previous_position=safe_coords["previous_position"],
                )
            )
            return ValidationResult.success(payload)
        # Otherwise, the client is a FootstepBuilder that needs a Blueprint.
        payload = FootstepCarrier(
            blueprint=FootstepBlueprint(
                position=safe_coords["position"],
                previous_position=safe_coords["previous_position"],
            )
        )
        return ValidationResult.success(payload)
    