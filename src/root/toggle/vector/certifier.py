# src/root/toggle/vector/certifier.py

"""
Module: root.toggle.vector.certifier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast


from err import ExcessTogglesException, NoActiveTogglesException
from err.route.validation.node.exception import NoValidationRouteException
from root import RootCertifier
from result import ValidationResult
from toggle import VectorToggle
from toolkit import VectorToggleToolkit
from util import LoggingLevelRouter


class VectorToggleRootCertifier(RootCertifier[VectorToggle]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorToggle instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : VectorToggleToolkit,
            ) -> ValidationResult[VectorToggle]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: VectorToggleToolkit = VectorToggleToolkit(),
    ):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> VectorToggleToolkit:
        return cast(VectorToggleToolkit, self.toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorToggle]:
        """
        Verify the candidate is a safe VectorToggle.

        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorToggle.
                    -   The vectorToggle's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit : VectorToggleToolkit
        Returns:
            ValidationResult[VectorToggle]
        Raises:
            TypeError
            VectorToggleNullException
            ZeroVectorToggleFlagsException
            VectorToggleRootCertifierException
            ExcessVectorToggleFlagsException
        """
        method = f"{self.__class__.__name__}.validate"
        
        bootstrap = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.model,
            model_null_exception=self.toolkit.null_exception,
        )
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRootCertifierException.MSG,
                    err_code=VectorToggleRootCertifierException.ERR_CODE,
                    ex=bootstrap.exception
                )
            )
        # --- Cast candidate to a VectorToggle for additional tests. ---#
        toggle = cast(self.toolkit, candidate)
        
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
        if toggle.excess_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRootCertifierException.MSG,
                    err_code=VectorToggleRootCertifierException.ERR_CODE,
                    ex=ExcessTogglesException(
                        msg=ExcessTogglesException.MSG,
                        err_code=ExcessTogglesException.ERR_CODE,
                    )
                )
            )
        # Pick a route for integrity testing the toggle's entity.
        validation_result = ValidationResult.failure(NoValidationRouteException())
        if toggle.is_coord_selector:
            validation_result = self.toolkit.coord.root.execute(toggle.entity)
        if toggle.is_vector_selector:
            validation_result = self.toolkit.vector.root.execute(toggle.entity)
   
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