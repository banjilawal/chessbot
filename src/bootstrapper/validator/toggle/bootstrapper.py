# src/bootstrapper/validator/toggle/bootstrapper.py

"""
Module: bootstrapper.validator.toggle.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Type, cast
from typing_extensions import TypeVar

from err import ExcessTogglesException, NullException, ToggleValidatorException, NoActiveTogglesException
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Toggle")


class ToggleValidator:
    """
    Role
        -   Transaction Worker
        -   Toggle Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Verify the candidate meets basic requirements of a Toggle class.

    Attributes:

    Provides:
        -   execute(
                    candidate: Any,
                    toggle_model: Type[T],
                    null_exception: NullException,
            ) -> ValidationResult:

    Super Class:
    """
        
        
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            toggle_model: Type[T],
            null_exception: NullException,
    ) -> ValidationResult:
        """
        Perform integrity tests common to all Toggle objects.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is null.
                    -   The candidate is not an instance of the toggle_model.
                    _   It has no active toggles.
                    _   It has excess toggles.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toggle_model: Type[T]
            null_exception: NullException
        Returns:
            ValidationResult
        Raises:
            ToggleValidatorException
            NoActiveTogglesException
            ExcessTogglesException
            TypeError
        """
        method = f"{self.__class__.__name__}.execute"
        
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ToggleValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ToggleValidatorException.MSG,
                    err_code=ToggleValidatorException.ERR_CODE,
                    ex=null_exception,
                )
            )
        if not isinstance(candidate, toggle_model):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ToggleValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ToggleValidatorException.MSG,
                    err_code=ToggleValidatorException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {type(toggle_model).__name__}. Got "
                        f"{type(candidate).__name__} instead."
                    ),
                )
            )
        # --- Cast the candidate into the expected Context subclass for additional tests. ---#
        toggle = cast(toggle_model, candidate)

        # Handle the case of searching with no attribute-value provided.
        if toggle.no_active_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ToggleValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ToggleValidatorException.MSG,
                    err_code=ToggleValidatorException.ERR_CODE,
                    ex=NoActiveTogglesException(
                        msg=NoActiveTogglesException.MSG,
                        err_code=NoActiveTogglesException.ERR_CODE,
                    ),
                )
            )
        # Handle the case of too many attributes being used in a search.
        if toggle.excess_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ToggleValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ToggleValidatorException.MSG,
                    err_code=ToggleValidatorException.ERR_CODE,
                    ex=ExcessTogglesException(
                        msg=ExcessTogglesException.MSG,
                        err_code=ExcessTogglesException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(toggle)
    
