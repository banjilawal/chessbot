# src/assurance/load/model/coord/loader.py

"""
Module: assurance.load.model.coord.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, CoordValidatorToolkit
from domain import Coord, CoordPrimeExtract
from err import (
    CoordCarrierEmptyException, CoordLoaderException, CoordValidationRequestNullException
)
from exchange import CoordValidationRequest
from transit import CoordCarrier

from util import LoggingLevelRouter


class CoordLoader(ModelLoader[Coord]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   CoordValidationRequest
            -   CoordCarrier
            -   CoordBlueprint

    Attributes:
        toolkit: CoordValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[CoordPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[CoordValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[CoordValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or CoordValidatorToolkit())
    
    @property
    def toolkit(self) -> CoordValidatorToolkit:
        return cast(CoordValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordPrimeExtract]:
        """
        Extract the CoordBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a CoordValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a CoordCarrier
                        -   An empty CoordCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a CoordPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordPrimeExtract]
        Raises:
            CoordLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=CoordValidationRequest,
            null_exception=CoordValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordLoaderException.MSG,
                    err_code=CoordLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[CoordValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordLoaderException.MSG,
                    err_code=CoordLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(CoordCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordLoaderException.MSG,
                    err_code=CoordLoaderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = CoordPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)