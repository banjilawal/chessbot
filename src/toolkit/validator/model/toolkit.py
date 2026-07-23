# src/toolkit/validator/model/toolkit.py

"""
Module: toolkit.validator.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from toolkit import ModelToolkit
from root import ModelRootCertifier
from toolkit import ValidatorToolkit

T = TypeVar("T", bound="Model")

class ModelValidatorToolkit(ValidatorToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles ModelRootCertifier dependencies.

    Attributes:
        toolkit: [ModelToolkit[T]],
        carrier_validator: [ModelRootCertifier[T]]
        
    Provides:
    
    Super Class:
        ValidatorToolkit
    """
    
    def __init__(
            self,
            toolkit: [ModelToolkit[T]],
            carrier_validator: [ModelRootCertifier[T]],
    ):
        """
        Args:
            toolkit: [ModelToolkit[T]],
            carrier_validator: [ModelRootCertifier[T]
        """
        super().__init__(toolkit=toolkit, carrier_validator=carrier_validator)

        
    @property
    def toolkit(self) -> [ModelToolkit[T]]:
        return cast([ModelToolkit[T]], super()._toolkit)
        
    @property
    def carrier_validator(self) -> [ModelRootCertifier[T]]:
        return cast([ModelRootCertifier[T]], super()._carrier_validator)