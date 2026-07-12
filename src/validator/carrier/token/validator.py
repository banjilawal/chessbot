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
    _toolkit: TokenToolkit
    _bootstrapper: TokenRootCertifier
    
    def __init__(
            self,
            toolkit: TokenToolkit | None = TokenToolkit(),
            root_certifier: TokenRootCertifier | None = TokenRootCertifier(),
    ):
        """
        Args:
            root_certifier: TokenRootCertifier
        """
        super().__init__(root_certifier=root_certifier)

    
    def root_certifier(self) -> TokenRootCertifier:
        return cast(TokenRootCertifier, self.root_certifier)
    
    
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        method = f"{self.__class__.__name__}.execute"
        
        priming = self._toolkit.priming_validator.execute(candidate)
        if priming.is_failure:
        
    
    
        
        
