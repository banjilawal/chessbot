# src/root/toggle/vector/certifier.py

"""
Module: root.toggle.vector.certifier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast


from err import ExcessToggleActivationException, NoActiveTogglesException
from root import ToggleRootCertifier
from result import ValidationResult
from toggle import VectorToggle
from toolkit import VectorToggleToolkit
from util import LoggingLevelRouter


class VectorToggleRootCertifier(ToggleRootCertifier[VectorToggle]):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance


    Responsibilities:
        1.  Ensure a VectorToggleBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: VectorToggleToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Certifier
    """
    
    def __init__(self, toolkit: VectorToggleToolkit | None = VectorToggleToolkit()):
        """
        Args:
            toolkit: VectorToggleToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> VectorToggleToolkit:
        return cast(VectorToggleToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult:
        """
        Certify a candidate is a VectorToggleBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a VectorToggleDtoCarrier.
                    -   The candidate is an empty VectorToggleDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a VectorToggle in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            VectorToggleCertifierException
            VectorToggleDtoCarrierNullException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.model_carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRooteCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRootCertifierException.MSG,
                    err_code=VectorToggleRootCertifierException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(self.toolkit.carrier_model, carrier_validation.payload)
        
        # --- Cast the candidate into a VectorToggleBlueprint for additional tests. ---#
        toggle = cast(self.toolkit.model, candidate)
        
        # Handle the case that neither option is enabled.
        if toggle.no_active_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRootCertifierException.MSG,
                    err_code=VectorToggleRootCertifierException.ERR_CODE,
                    ex=NoActiveTogglesException(
                        msg=NoActiveTogglesException.MSG,
                        err_code=NoActiveTogglesException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if toggle.excess_active_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRootCertifierException.MSG,
                    err_code=VectorToggleRootCertifierException.ERR_CODE,
                    ex=ExcessToggleActivationException(
                        msg=ExcessToggleActivationException.MSG,
                        err_code=ExcessToggleActivationException.ERR_CODE,
                    )
                )
            )
        # Pick a route for integrity testing the toggle's entity.
        validation_result = ValidationResult.failure(NodeNoValidationRouteException())
        if toggle.is_coord_selector:
            validation_result = self.toolkit.coord.validator.execute(toggle.entity)
        if toggle.is_vector_selector:
            validation_result = self.toolkit.vector.validator.execute(toggle.entity)
   
        # Handle the case that, the entity is not safe to use.
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRootCertifierException.MSG,
                    err_code=VectorToggleRootCertifierException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(toggle)