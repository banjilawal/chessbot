# src/assurance/load/model/board/loader.py

"""
Module: assurance.load.model.board.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, BoardValidatorToolkit
from domain import Board, BoardPrimeExtract
from err import (
    BoardCarrierEmptyException, BoardLoaderException, BoardValidationRequestNullException
)
from exchange import BoardValidationRequest
from transit import BoardCarrier

from util import LoggingLevelRouter


class BoardLoader(ModelLoader[Board]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   BoardValidationRequest
            -   BoardCarrier
            -   BoardBlueprint

    Attributes:
        toolkit: BoardValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[BoardPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[BoardValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[BoardValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or BoardValidatorToolkit())
    
    @property
    def toolkit(self) -> BoardValidatorToolkit:
        return cast(BoardValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[BoardPrimeExtract]:
        """
        Extract the BoardBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a BoardValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a BoardCarrier
                        -   An empty BoardCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a BoardPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[BoardPrimeExtract]
        Raises:
            BoardLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=BoardValidationRequest,
            null_exception=BoardValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardLoaderException.MSG,
                    err_code=BoardLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[BoardValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardLoaderException.MSG,
                    err_code=BoardLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(BoardCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardLoaderException.MSG,
                    err_code=BoardLoaderException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = BoardPrimeExtract(reference=carrier, safe_blueprint=blueprint)
        return ValidationResult.success(extract)