# src/authorization/reviewer/reviewer.py

"""
Module: authorization.reviewer.reviewer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import PrimingValidator

T = TypeVar("T")

class Reviewer(ABC, Generic[T]):
    """
    Role:
        - Permission Authorization
        - Checklist Runner
        - Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a .

    Attributes:

    Provides:

    Super Class:
    """
    
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        self._priming_validator = priming_validator or PrimingValidator()
        
    @property
    def priming_validator(self) -> PrimingValidator:
        self._priming_validator
        