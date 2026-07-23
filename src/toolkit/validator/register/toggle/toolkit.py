# src/toolkit/validator/register/toggle/toolkit.py

"""
Module: toolkit.validator.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from toolkit import ToggleRegisterToolkit
from register import ToggleRegister
from root import ToggleRegisterRootCertifier
from toolkit import RegisterValidatorToolkit


class ToggleRegisterValidatorToolkit(RegisterValidatorToolkit[ToggleRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles ToggleRegisterRegisterRootCertifier dependencies.

    Attributes:
        toolkit: Optional[ToggleRegisterToolkit]
        carrier_validator: Optional[ToggleRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: Optional[ToggleRegisterToolkit] |
                       None = ToggleRegisterToolkit(),
            carrier_validator: Optional[ToggleRegisterRootCertifier] |
                            None = ToggleRegisterRootCertifier(),
    ):
        """
        Args:
            toolkit: Optional[ToggleRegisterToolkit]
            carrier_validator: Optional[ToggleRegisterRootCertifier]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)
        
    @property
    def toolkit(self) -> ToggleRegisterToolkit:
        return cast(ToggleRegisterToolkit, super().toolkit)
    
    @property
    def carrier_validator(self) -> ToggleRegisterRootCertifier:
        return cast(ToggleRegisterRootCertifier, super().carrier_validator)
    
