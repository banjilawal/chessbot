# src/toolkit/validator/register/toolkit.py

"""
Module: toolkit.validator.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from toolkit import RegisterToolkit
from root import RegisterRootCertifier
from toolkit import ValidatorToolkit

T = TypeVar("T", bound="Register")

class RegisterValidatorToolkit(ValidatorToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles RegisterRootCertifier dependencies.

    Attributes:
        toolkit: [RegisterToolkit[T]],
        carrier_validator: [RegisterRootCertifier[T]]
        
    Provides:
    
    Super Class:
        ValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: [RegisterToolkit[T]],
            carrier_validator: [RegisterRootCertifier[T]],
    ):
        """
        Args:
            toolkit: [RegisterToolkit[T]],
            carrier_validator: [RegisterRootCertifier[T]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)

        
    @property
    def toolkit(self) -> [RegisterToolkit[T]]:
        return cast([RegisterToolkit[T]], super()._toolkit)
        
    @property
    def carrier_validator(self) -> [RegisterRootCertifier[T]]:
        return cast([RegisterRootCertifier[T]], super()._carrier_validator)