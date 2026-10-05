# src/assurance/validator/model/vector/validator.py

"""
Module: assurance.validator.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, VectorLoader, VectorValidatorToolkit
from domain import Vector, VectorBlueprint, VectorPrimeExtract
from err import VectorCarrierEmptyException, VectorValidatorException
from transit import VectorCarrier
from util import LoggingLevelRouter


class VectorValidator(ModelValidator[Vector]):
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
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[VectorLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[VectorLoader]
        """
        super().__init__(loader=loader or VectorLoader())
    
    @property
    def loader(self) -> VectorLoader:
        return cast(VectorLoader, super().loader)
    
    @property
    def toolkit(self) -> VectorValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorCarrier]:
        """
        Assure a candidate is a safe VectorCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the x or y component is unsafe.
            2.  Otherwise, send a VectorCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorCarrier]
        Raises:
            VectorValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
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
        prime_extract = cast(VectorPrimeExtract, loading.payload)
        carrier = prime_extract.carrier
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
        # --- Extract validation payloads. ---#
        x = components[0]
        y = components[1]
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe Vector.
        if prime_extract.recipient_wants_model:
            payload = Vector(x=x, y=y)
            return ValidationResult.success(VectorCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = VectorBlueprint(x=x, y=y)
        return ValidationResult.success(VectorCarrier(blueprint=payload))
        # --- Forward the appropriate work product to the caller. ---#

        


