# src/assurance/bundle/bundle.py

"""
Module: assurance.bundle.bundle
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar

from assurance import PrimingValidator
from domain import DomainObject, NullExceptionRoster, DomainObjectAssociationManifest
from microservice import IdentityService

T = TypeVar("T", bound="DomainObject")

@dataclass
class ValidationBundle(ABC, Generic[T]):
    types: DomainObjectAssociationManifest[T]
    nulls: NullExceptionRoster[T]
    resources: Dict[str, Any]
    
    @property
    def identity_service(self) -> IdentityService:
        return self.resources["identity_service"]
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self.resources["priming_validator"]