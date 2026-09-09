# src/assurance/bundle/bundle.py

"""
Module: assurance.bundle.bundle
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Generic, Optional, TypeVar

from assurance import HelperTable, PrimingValidator
from domain import Model, ObjectManifest
from microservice import IdentityService

T = TypeVar("T", bound="Model")


class ModelValidationBundle(ABC, Generic[T]):
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
    """
    _metadata: ObjectManifest[T]
    _helper: HelperTable[T]

    
    def __init__(
            self,
            helper: HelperTable[T],
            metadata: ObjectManifest[T],
    ):
        """
        Args:
            helper: HelperTable[T]
            metadata: ObjectManifest[T]
        """
        self._helper = helper
        self._metadata = metadata
    
    
    @property
    def helper(self) -> HelperTable[T]:
        return self._helper
    
    @property
    def metadata(self) -> ObjectManifest[T]:
        return self._metadata