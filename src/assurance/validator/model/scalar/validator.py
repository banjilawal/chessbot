# src/assurance/validator/model/scalar/validator.py

"""
Module: assurance.validator.model.scalar.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, ScalarLoader, ScalarValidatorToolkit
from config import BoardSetting
from domain import Scalar, ScalarBlueprint, ScalarPrimeExtract
from err import ScalarCarrierEmptyException, ScalarValidatorException
from transit import ScalarCarrier
from util import LoggingLevelRouter


class ScalarValidator(ModelValidator[Scalar]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ScalarCarrier and its contents are safe to use.

    Attributes:
        loader: ScalarLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ScalarCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(self, loader: Optional[ScalarLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[ScalarLoader]
        """
        super().__init__(loader=loader or ScalarLoader())
        
    @property
    def loader(self) -> ScalarLoader:
        return cast(ScalarLoader, super().loader)
    
    @property
    def toolkit(self) -> ScalarValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ScalarCarrier]:
        """
        Assure a candidate is a safe ScalarCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Either the id, board, or owner are flagged unsafe.
            2.  Otherwise, send a ScalarCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ScalarCarrier]
        Raises:
            ScalarValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(ScalarPrimeExtract, loading.payload)
        carrier = prime_extract.carrier
        blueprint = carrier.extract_blueprint()
        
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the magnitude is out of bounds.
        ceiling = BoardSetting.diagonal_length() - 1
        magnitude_validation = self.toolkit.number_validator.execute(
            candidate=blueprint.magnitude,
            floor= (-1 * ceiling),
            ceiling=ceiling,
        )
        if magnitude_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidatorException.MSG,
                    err_code=ScalarValidatorException.ERR_CODE,
                    ex=magnitude_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        magnitude = cast(int, magnitude_validation.payload)
        
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe Scalar.
        if prime_extract.recipient_wants_model:
            payload = ScalarCarrier(
                model=Scalar(magnitude=magnitude)
            )
            return ValidationResult.success(payload)
        
        # Otherwise, the client is a ScalarBuilder that needs a Blueprint.
        payload = ScalarCarrier(
            blueprint=ScalarBlueprint(magnitude=magnitude)
        )
        return ValidationResult.success(payload)