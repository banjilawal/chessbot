# src/assurance/validator/structure/register/square/validator.py

"""
Module: assurance.validator.structure.register.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import RegisterValidator, SquareRegisterValidatorToolkit
from domain import SquareRegister
from transit import SquareRegisterCarrier
from util import LoggingLevelRouter


class SquareRegisterValidator(RegisterValidator[SquareRegister]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structures and blueprints inside an EntityCarrier's payload.

    Attributes:
        toolkit: SquareRegisterValidatorToolkit

    Provides:
        - def execute(candidate: Any) -> ValidationResult[SquareRegisterCarrier]:

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[SquareRegisterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareRegisterValidatorToolkit]
        """
        super().__init__(
            toolkit=toolkit or SquareRegisterValidatorToolkit()
        )
    
    @property
    def toolkit(self) -> SquareRegisterValidatorToolkit:
        return cast(SquareRegisterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareRegisterCarrier]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[SquareRegisterCarrier]
        Raises:
            SquareRegisterValidatorException
        """
        pass
    
    
