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
from assurance import ModelValidator
from bootstrap import VectorValidationLoader
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
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(VectorPrimeExtract, bootstrap.payload)
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
            validation = self.loader.number_validator.execute(value)
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
            components.append(cast(int, validation.authorization_applicant))
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        x = components[0]
        y = components[1]
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Vector.
        if extract.recipient_wants_model:
            model = Vector(x=x, y=y)
            payload = VectorCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        blueprint = VectorBlueprint(x=x, y=y)
        blueprint.mark_as_validated()
        payload = VectorCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)

        


