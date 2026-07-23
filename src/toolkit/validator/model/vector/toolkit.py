# src/toolkit/validator/model/vector/toolkit.py

"""
Module: toolkit.validator.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from toolkit import VectorToolkit
from model import Vector
from root import VectorRootCertifier
from toolkit import ModelValidatorToolkit


class VectorValidatorToolkit(ModelValidatorToolkit[Vector]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorModelRootCertifier dependencies.

    Attributes:
        toolkit: Optional[VectorToolkit]
        carrier_validator: Optional[VectorRootCertifier]
            
    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorToolkit] | None = VectorToolkit(),
            carrier_validator: Optional[VectorRootCertifier] |
                            None = VectorRootCertifier(),
    ):
        """
        Args:
            toolkit: Optional[VectorToolkit]
            carrier_validator: Optional[VectorRootCertifier]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)
        
    @property
    def toolkit(self) -> VectorToolkit:
        return cast(VectorToolkit, super().toolkit)
    
    @property
    def carrier_validator(self) -> VectorRootCertifier:
        return cast(VectorRootCertifier, super().carrier_validator)
    
