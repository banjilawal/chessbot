# src/assurance/bundle/structure/bundle.py

"""
Module: assurance.bundle.structure.bundle
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar

from assurance import ValidationBundle
from domain import  NullExceptionRoster, DomainObjectTypeUnions
from domain import Structure


T = TypeVar("T", bound="Structure")


@dataclass
class StructureValidationBundle(ValidationBundle[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities IntegrityChecker
            needs to run safety checks on a validation candidate.

    Attributes:
        identity_service: IdentityService
        primin_validator: PrimingValidator
        
        types: DomainObjectUnions[T]
        nulls: NullExceptionRoster[T]
        
        resources: Dict[str, Any]

    Provides:

    Super Class:
        ValidationBundle
    """
    types: DomainObjectTypeUnions[T]
    nulls: NullExceptionRoster[T]
    resources: Dict[str, Any]