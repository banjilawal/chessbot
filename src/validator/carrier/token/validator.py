# src/validator/carrier/token/validator.py

"""
Module: validator.carrier.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, cast

from carrier import TokenCarrier
from primary import RootCertifier, TokenRootCertifier
from result import ValidationResult
from toolkit import TokenToolkit
from validator.carrier import CarrierValidator


class TokenCarrierValidator(CarrierValidator[TokenCarrier]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: TokenRootCertifier
        
    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: TokenToolkit | None = TokenToolkit(),
            root_certifier: TokenRootCertifier | None = TokenRootCertifier(),
    ):
        """
        Args:
            root_certifier: TokenRootCertifier
        """
        super().__init__(toolkit=toolkit, root_certifier=root_certifier)

    @property
    def toolkit(self) -> TokenToolkit:
        return cast(TokenToolkit, self.toolkit)
    
    @property
    def root_certifier(self) -> TokenRootCertifier:
        return cast(TokenRootCertifier, self.root_certifier)
    
    
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        method = f"{self.__class__.__name__}.execute"
        
        priming = self.toolkit.priming_validator.execute(
            candiate=candidate,
            target_model=self.toolkit.carrier_model,
            null_exception=self.toolkit.
        )
        if priming.is_failure:
        
    
    
        
        
