# src/assurance/load/struct/binder/team/loader.py

"""
Module: assurance.load.struct.binder.team.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import BinderLoader, TeamBinderValidatorToolkit
from domain import TeamBinder
from err import (
    TeamBinderConsistencyException, TeamBinderEmptyException, TeamBinderLoaderException,
    TeamBinderValidationRequestNullException
)
from exchange import TeamBinderValidationRequest

from util import LoggingLevelRouter


class TeamBinderLoader(BinderLoader[TeamBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TeamBinderValidationRequest
            -   TeamBinder
            -   TeamBinderBlueprint

    Attributes:
        toolkit: TeamBinderValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[TeamBinder[T]

    Super Class:
        BinderLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TeamBinderValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TeamBinderValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TeamBinderValidatorToolkit())
    
    @property
    def toolkit(self) -> TeamBinderValidatorToolkit:
        return cast(TeamBinderValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamBinder]:
        """
        Model the TeamBinderBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a TeamBinderValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a TeamBinder
                        -   An empty TeamBinder.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a TeamBinder
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamBinder]
        Raises:
            TeamBinderLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=TeamBinderValidationRequest,
            null_exception=TeamBinderValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderLoaderException.MSG,
                    err_code=TeamBinderLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[TeamBinderValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderLoaderException.MSG,
                    err_code=TeamBinderLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        model = cast(TeamBinder, model_validation.payload)
        # --- Send the work product. ---#
        return ValidationResult.success(model)