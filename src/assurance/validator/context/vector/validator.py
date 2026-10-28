# src/assurance/validator/context/vector/validator.py

"""
Module: assurance.validator.context.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ContextValidator, VectorValidationLoader, VectorLayerToolkit
from domain import Vector, VectorBlueprint, VectorPrimeExtract
from err import VectorCarrierEmptyException, VectorValidatorException
from transit import VectorCarrier
from util import LoggingLevelRouter


class VectorValidator(ContextValidator[Vector]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorCarrier is safe to use.

    Attributes:
        loader: VectorLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[VectorCarrier]:

    Super Class:
        ContextValidator
    """
    
    def __init__(
            self,
            loader: Optional[VectorValidationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[VectorLoader]
        """
        super().__init__(loader=loader or VectorValidationLoader())
    
    @property
    def loader(self) -> VectorValidationLoader:
        return cast(VectorValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> VectorLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[VectorCarrier]:
        """
        Assure a candidate is a safe VectorCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the x or y component is unsafe.
            2.  Otherwise, send a VectorCarrier in the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[VectorCarrier]
        Raises:
            VectorValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(item)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(VectorPrimeExtract, loading.payload)
        carrier = extract.reference
        blueprint = carrier.extract_blueprint()
        
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        
        # Handle the case that any vector component in the blueprint is flagged.
        components = []
        for value in [blueprint.x, blueprint.y]:
            validation = self.toolkit.number_validator.execute(value)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorValidatorException.MSG,
                        err_code=VectorValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            components.append(cast(int, validation.payload))
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        x = components[0]
        y = components[1]
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Vector.
        if extract.recipient_wants_context:
            payload = VectorCarrier(
                context=Vector(x=x, y=y)
            )
            return ValidationResult.success(payload)
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = VectorCarrier(
            blueprint=VectorBlueprint(x=x, y=y)
        )
        return ValidationResult.success(payload)

        


