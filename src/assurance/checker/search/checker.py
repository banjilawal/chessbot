# src/assurance/checker/search/checker.py

"""
Module: assurance.checker.search.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from assurance import IntegrityChecker
from domain import SearchContext


T = TypeVar("T", bound="SearchContext")


class SearchContextChecker(IntegrityChecker, ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null SearchContext.
        2.  Run safety checks on any SearchContex attributes that are enabled.

    Attributes:
        bundle: SearchValidationBundle[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[T]:

    Super Class:
        IntegrityChecker
    """
    
    
