# src/assurance/manifest/bundle/manifest.py

"""
Module: assurance.manifest.bundle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar

from assurance import NullRoster, PrimingValidator, TypesManifest
from microservice import IdentityService
from model import Model

T = TypeVar("T", bound="Model")

@dataclass
class ValidationBundle(ABC, Generic[T]):
    types: TypesManifest[T]
    nulls: NullRoster[T]
    resources: Dict[str, Any]
    
    @property
    def identity_service(self) -> IdentityService:
        return self.resources["identity_service"]
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self.resources["priming_validator"]