# src/toolkit/validator/register/vector/toolkit.py

"""
Module: toolkit.validator.register.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from toolkit import VectorRegisterToolkit
from register import VectorRegister
from root import VectorRegisterRootCertifier
from toolkit import RegisterValidatorToolkit


class VectorRegisterValidatorToolkit(RegisterValidatorToolkit[VectorRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorRegisterRegisterRootCertifier dependencies.

    Attributes:
        toolkit: Optional[VectorRegisterToolkit]
        carrier_validator: Optional[VectorRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorRegisterToolkit] |
                       None = VectorRegisterToolkit(),
            carrier_validator: Optional[VectorRegisterRootCertifier] |
                            None = VectorRegisterRootCertifier(),
    ):
        """
        Args:
            toolkit: Optional[VectorRegisterToolkit]
            carrier_validator: Optional[VectorRegisterRootCertifier]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)
        
    @property
    def toolkit(self) -> VectorRegisterToolkit:
        return cast(VectorRegisterToolkit, super().toolkit)
    
    @property
    def carrier_validator(self) -> VectorRegisterRootCertifier:
        return cast(VectorRegisterRootCertifier, super().carrier_validator)
    
