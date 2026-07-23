# src/toolkit/validator/toolkit.py

"""
Module: toolkit.validator.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from bootstrapper import EntityCarrierValidator
from toolkit import Toolkit

T = TypeVar("T")

class ValidatorToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles RootCertifier dependencies.

    Attributes:
        toolkit: Toolkit
        carrier_validator: EntityCarrierValidator
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _toolkit: Toolkit
    _carrier_validator: EntityCarrierValidator
    
    def __init__(
            self,
            toolkit: Toolkit,
            carrier_validator: EntityCarrierValidator,
    ):
        """
        Args:
            toolkit: Toolkit[T],
            carrier_validator: EntityCarrierValidator[T]
        """
        super().__init__()
        self._toolkit = toolkit
        self._carrier_validator = carrier_validator
        
    @property
    def toolkit(self) -> Toolkit:
        return self._toolkit
    
    @property
    def carrier_validator(self) -> EntityCarrierValidator:
        return self._carrier_validator