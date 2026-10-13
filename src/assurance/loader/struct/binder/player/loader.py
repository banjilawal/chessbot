# src/assurance/load/struct/binder/player/loader.py

"""
Module: assurance.load.struct.binder.player.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import BinderLoader, PlayerBinderValidatorToolkit
from domain import PlayerBinder
from err import (
    PlayerBinderConsistencyException, PlayerBinderEmptyException, PlayerBinderLoaderException,
    PlayerBinderValidationRequestNullException
)
from exchange import PlayerBinderValidationRequest

from util import LoggingLevelRouter


class PlayerBinderLoader(BinderLoader[PlayerBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   PlayerBinderValidationRequest
            -   PlayerBinder
            -   PlayerBinderBlueprint

    Attributes:
        toolkit: PlayerBinderValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[PlayerBinder[T]

    Super Class:
        BinderLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[PlayerBinderValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerBinderValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or PlayerBinderValidatorToolkit())
    
    @property
    def toolkit(self) -> PlayerBinderValidatorToolkit:
        return cast(PlayerBinderValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PlayerBinder]:
        """
        Model the PlayerBinderBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a PlayerBinderValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a PlayerBinder
                        -   An empty PlayerBinder.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a PlayerBinder
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PlayerBinder]
        Raises:
            PlayerBinderLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=PlayerBinderValidationRequest,
            null_exception=PlayerBinderValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderLoaderException.MSG,
                    err_code=PlayerBinderLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[PlayerBinderValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderLoaderException.MSG,
                    err_code=PlayerBinderLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        model = cast(PlayerBinder, model_validation.payload)
        # --- Send the work product. ---#
        return ValidationResult.success(model)