# src/toolkit/validator/register/number/toolkit.py

"""
Module: toolkit.validator.register.number.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from toolkit import NumberRegisterToolkit
from register import NumberRegister
from root import NumberRegisterRootCertifier
from toolkit import RegisterValidatorToolkit


class NumberRegisterValidatorToolkit(RegisterValidatorToolkit[NumberRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles NumberRegisterRegisterRootCertifier dependencies.

    Attributes:
        toolkit: Optional[NumberRegisterToolkit]
        carrier_validator: Optional[NumberRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: Optional[NumberRegisterToolkit] |
                       None = NumberRegisterToolkit(),
            carrier_validator: Optional[NumberRegisterRootCertifier] |
                            None = NumberRegisterRootCertifier(),
    ):
        """
        Args:
            toolkit: Optional[NumberRegisterToolkit]
            carrier_validator: Optional[NumberRegisterRootCertifier]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)
        
    @property
    def toolkit(self) -> NumberRegisterToolkit:
        return cast(NumberRegisterToolkit, super().toolkit)
    
    @property
    def carrier_validator(self) -> NumberRegisterRootCertifier:
        return cast(NumberRegisterRootCertifier, super().carrier_validator)
    
