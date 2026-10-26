# src/assurance/load/context/vector/loader.py

"""
Module: assurance.load.context.vector.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, VectorValidatorToolkit
from domain import Vector, Vector
from err import (
    VectorCarrierEmptyException, VectorContextValidationLoaderException, VectorValidationRequestNullException
)
from exchange import VectorValidationRequest
from transit import VectorCarrier

from util import LoggingLevelRouter


class VectorContextValidationLoader(ContextValidationLoader[Vector]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   VectorValidationRequest
            -   VectorCarrier
            -   VectorBlueprint

    Attributes:
        toolkit: VectorValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[Vector[T]

    Super Class:
        ContextLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[VectorValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or VectorValidatorToolkit())
    
    @property
    def toolkit(self) -> VectorValidatorToolkit:
        return cast(VectorValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Vector]:
        """
        Extract the VectorBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a VectorValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a VectorCarrier
                        -   An empty VectorCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a Vector
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Vector]
        Raises:
            VectorLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_context=VectorValidationRequest,
            null_exception=VectorValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationLoaderException.MSG,
                    err_code=VectorContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[VectorValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_context=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationLoaderException.MSG,
                    err_code=VectorContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(VectorCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationLoaderException.MSG,
                    err_code=VectorContextValidationLoaderException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = Vector(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)