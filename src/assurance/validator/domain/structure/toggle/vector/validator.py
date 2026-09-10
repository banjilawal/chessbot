# src/root/toggle/vector/assurance/validator.py

"""
Module: root.toggle.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from assurance import ToggleValidator
from domain.metadata.blueprint import CartesianToggleBlueprint
from carrier import CartesianToggleCarrier
from err import (
    ExcessToggleActivationException, NoActiveTogglesException, NoValidationRouteException,
    CartesianToggleRootValidatorException
)
from domain.model import Coord, Vector
from assurance.validator import ToggleValidator
from artifcat import ValidationResult
from domain.structure.toggle import CartesianToggle
from operation.toolkit import CartesianToggleToolkit
from util import LoggingLevelRouter


class CartesianToggleValidator(ToggleValidator[CartesianToggle]):
    """
    Role
        - Integrity Maintenance
        - Consistency Assurance


    Responsibilities:
        1.  Ensure a CartesianToggleBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: CartesianToggleToolkit

    Provides:
        - execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Validator
    """
    
    def __init__(self, toolkit: CartesianToggleToolkit | None = CartesianToggleToolkit()):
        """
        Args:
            toolkit: CartesianToggleToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> CartesianToggleToolkit:
        return cast(CartesianToggleToolkit, super().ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult:
        """
        Certify a candidate is a CartesianToggleBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a CartesianToggleCarrier.
                    - The candidate is an empty CartesianToggleCarrier.
                    - Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a CartesianToggle in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            CartesianToggleValidatorException
            CartesianToggleCarrierNullException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRootValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRootValidatorException.MSG,
                    err_code=CartesianToggleRootValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(self.toolkit.carrier_model, carrier_validation.payload)
        
        # --- Cast the candidate into a CartesianToggleBlueprint for additional tests. ---#
        blueprint = cast(self.toolkit.blueprint_model, carrier)
        
        # Handle the case that neither option is enabled.
        if blueprint.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRootValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRootValidatorException.MSG,
                    err_code=CartesianToggleRootValidatorException.ERR_CODE,
                    ex=NoActiveTogglesException(
                        msg=NoActiveTogglesException.MSG,
                        err_code=NoActiveTogglesException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if blueprint.is_above_max_size:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRootValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRootValidatorException.MSG,
                    err_code=CartesianToggleRootValidatorException.ERR_CODE,
                    ex=ExcessToggleActivationException(
                        msg=ExcessToggleActivationException.MSG,
                        err_code=ExcessToggleActivationException.ERR_CODE,
                    )
                )
            )
        # Pick a route for integrity testing the toggle's entity.
        validation = ValidationResult.failure(NoValidationRouteException())

        if blueprint.for_coord_toggle:
            validation = self.toolkit.coord.validator.execute(
                blueprint.coord
            )
        if blueprint.for_vector_toggle:
            validation = self.toolkit.vector.validator.execute(
                blueprint.vector
            )
        # Handle the case that, the entity is not safe to use.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRootValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRootValidatorException.MSG,
                    err_code=CartesianToggleRootValidatorException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        if carrier.is_carrying_model:
            return ValidationResult.success(
                self._process_model_carrier(validation.payload)
            )
        return ValidationResult.success(
            self._process_blueprint_carrier(validation.payload)
        )
        
        
    def _process_model_carrier(self, item) -> CartesianToggleCarrier:
        if isinstance(item, Coord):
            coord = cast(Coord, item)
            return CartesianToggleCarrier(
                model=CartesianToggle(coord=coord)
            )
        vector = cast(Vector, item)
        return CartesianToggleCarrier(
            model=CartesianToggle(vector=vector)
        )
    
    def _process_blueprint_carrier(self, item) -> CartesianToggleCarrier:
        if isinstance(item, Coord):
            coord = cast(Coord, item)
            return CartesianToggleCarrier(
                blueprint=CartesianToggleBlueprint(coord=coord)
            )
        vector = cast(Vector, item)
        return CartesianToggleCarrier(
            blueprint=CartesianToggleBlueprint(vector=vector)
        )