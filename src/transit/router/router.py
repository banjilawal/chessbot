# src/transit/route/router.py

"""
Module: transit.route.route
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import Result
from assurance import PrimingValidator

T = TypeVar("T", bound="Result")

class Router(ABC, Generic[T]):
    """
    Role
        - Transaction Worker
        - Routing

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.

    Attributes:
        priming_validator: PrimingValidator
        
    Provides:

    Super Class:
    """
    
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        self._priming_validator = priming_validator or PrimingValidator()
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    