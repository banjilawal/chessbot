# src/assurance/validator/model/footstep/validator.py

"""
Module: assurance.validator.model.footstep.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator
from bootstrap import FootstepValidationLoader
from domain import Coord, Footstep, FootstepBlueprint, FootstepPrimeExtract
from err import FootstepConsistencyException, FootstepValidatorException
from exchange import CoordValidationRequest
from transit import CoordCarrier, FootstepCarrier
from util import IdFactory, LoggingLevelRouter


class FootstepValidator(ModelValidator[Footstep]):
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
        ModelValidator
    """
    
    def __init__(self, loader: Optional[FootstepValidationLoader] | None = None):
        """
        Args:
            loader: Optional[FootstepLoader]
        """
        super().__init__(loader=loader or FootstepValidationLoader())
        
    @property
    def loader(self) -> FootstepValidationLoader:
        return cast(FootstepValidationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[FootstepCarrier]:
        """
        Assure a candidate is a safe FootstepCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   Loader fails.
                    -   The FootstepBlueprint has an inconsistency.
                    -   The CoordValidator flags either existing position.
            2.  Otherwise, send the type of carrier extract indicates.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Footstep]
        Raises:
            FootstepValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidatorException.MSG,
                    err_code=FootstepValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(FootstepPrimeExtract, bootstrap.payload)
        fingerprint = cast(FootstepBlueprint, extract.blueprint)
        
        # Handle the case that the footstep has an inconsistency.
        if fingerprint.is_not_consistent:
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
        candidate_points = fingerprint.to_dict
        for key in candidate_points.keys():
            # Handle the case that a position is not a safe Coord.
            coord_validation = self.loader.toolkit.dependency.coord.extract_model(
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
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        position = safe_coords["position"]
        previous_position = safe_coords["previous_position"]
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Team.
        if extract.recipient_wants_model:
            model = Footstep(
                position=position,
                previous_position=previous_position,
            )
            payload = FootstepCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a FootstepBuilder that needs a Blueprint.
        blueprint = FootstepBlueprint(
            position=position,
            previous_position=previous_position,
        )
        blueprint.mark_as_validated()
        payload = FootstepCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)
    