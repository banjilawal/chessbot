# src/assurance/validator/structure/node/validator.py

"""
Module: assurance.validator.node.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from assurance import NodeValidator, VectorNodeValidationToolkit
from fabrication import VectorNodeBlueprint
from domain.structure.node import VectorNode
from artifcat import ValidationResult
from transit.carrier import VectorNodeCarrier
from util import LoggingLevelRouter


class VectorNodeValidator(NodeValidator):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a Node instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: VectorNodeValidationToolkit

    Provides:
        - execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, toolkit: VectorNodeValidationToolkit):
        """
        Args:
            toolkit: VectorNodeValidator
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> VectorNodeValidationToolkit:
        return cast(VectorNodeValidationToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult[VectorNode|VectorNodeBlueprint]:
        """
        Certify a candidate is either a Vector or its Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a VectorCarrier.
                    - The candidate is an empty VectorCarrier.
                    - Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a Vector in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult[VectorNode|VectorNodeBlueprint]
        Raises:
            VectorNodeValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.types.carrier,
            model_null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidatorException.MSG,
                    err_code=VectorNodeValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the candidate into VectorNodeCarrier for additional testing ---#
        carrier = cast(self.toolkit.types.carrier, carrier_validation.payload)
        
        # --- Cast the candidate into a VectorBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, the blueprint's vector is flagged.
        validation = self.toolkit.vector_validator.execute(blueprint.vector)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeValidatorException.MSG,
                    err_code=VectorNodeValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        
        # --- Use the validated vector to build the appropriate object. ---#
        blueprint = cast(VectorNodeBlueprint, validation.payload)
        vector = blueprint.vector
        
        if carrier.is_carrying_model:
            return ValidationResult.success(
                VectorNodeCarrier(model=VectorNode(payload=vector))
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            VectorNodeCarrier(blueprint=VectorNodeBlueprint(vector=vector))
        )
        
    
    
        
        
