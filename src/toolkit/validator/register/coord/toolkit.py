# src/toolkit/validator/register/coord/toolkit.py

"""
Module: toolkit.validator.register.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from toolkit import CoordRegisterToolkit
from register import CoordRegister
from root import CoordRegisterRootCertifier
from toolkit import RegisterValidatorToolkit


class CoordRegisterValidatorToolkit(RegisterValidatorToolkit[CoordRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles CoordRegisterRegisterRootCertifier dependencies.

    Attributes:
        toolkit: Optional[CoordRegisterToolkit]
        carrier_validator: Optional[CoordRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: Optional[CoordRegisterToolkit] |
                       None = CoordRegisterToolkit(),
            carrier_validator: Optional[CoordRegisterRootCertifier] |
                            None = CoordRegisterRootCertifier(),
    ):
        """
        Args:
            toolkit: Optional[CoordRegisterToolkit]
            carrier_validator: Optional[CoordRegisterRootCertifier]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)
        
    @property
    def toolkit(self) -> CoordRegisterToolkit:
        return cast(CoordRegisterToolkit, super().toolkit)
    
    @property
    def carrier_validator(self) -> CoordRegisterRootCertifier:
        return cast(CoordRegisterRootCertifier, super().carrier_validator)
    
