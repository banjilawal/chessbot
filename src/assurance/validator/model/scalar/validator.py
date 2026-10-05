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
from assurance import ModelValidator, ScalarValidatorToolkit
from config import BoardSetting
from domain import Scalar, ScalarBlueprint, ScalarPrimeExtract
from err import ScalarValidatorException
from transit import ScalarCarrier
from util import LoggingLevelRouter


class ScalarValidator(ModelValidator[Scalar]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ScalarCarrier is safe to use.

    Attributes:
        loader: ScalarValidatorToolkit

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ScalarCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            loader: Optional[ScalarValidatorToolkit] | None = None,
    ):
        """
        Args:
            loader: Optional[ScalarValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ScalarValidatorToolkit())
    
    @property
    def toolkit(self) -> ScalarValidatorToolkit:
        return cast(ScalarValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[ScalarCarrier]:
        """
        Certify a ScalarCarrier's payload is either a Scalar or a Blueprint 
        that is safe to use.

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
        loading = self.toolkit.loader.execute(candidate)
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
        blueprint = cast(ScalarBlueprint, prime_extract.blueprint)
        
        # Handle the case that any scalar component in the blueprint is flagged.
        ceiling = BoardSetting.diagonal_length()
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
        # --- Extract validation payloads. ---#
        magnitude = cast(int, magnitude_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe Scalar.
        if prime_extract.carrier.has_model:
            payload = Scalar(magnitude=magnitude)
            return ValidationResult.success(ScalarCarrier(model=payload))
        
        # Otherwise, the client is a ScalarBuilder that needs a Blueprint.
        payload = ScalarBlueprint(magnitude=magnitude)
        return ValidationResult.success(ScalarCarrier(blueprint=payload))