# src/assurance/depend/toolkit/toolkit.py

"""
Module: assurance.depend.toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import CommonToolkit, ServiceDependency, NumberValidator, PrimingValidator
from domain import DomainManifest, Layer, NullWarningSet
from microservice import BlueprintIdExtractor, IdentityService

T = TypeVar("T")


class LayerToolkit(ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Toolkits types, null-exceptions, attribute-validators, and utilities IntegrityChecker
            needs to run safety checks on a validation candidate.

    Attributes:
        manifest: DomainManifest[T]
        helper: AttributeDependency[T]
        common: CommonToolkit

    Provides:

    Super Class:
    """
    _manifest: DomainManifest[T]
    _dependency: ServiceDependency[T]
    _common: CommonToolkit
    
    def __init__(
            self,
            dependency: ServiceDependency[T],
            manifest: DomainManifest[T],
            common: Optional[CommonToolkit] | None = None,
    ):
        """
        Args:
            dependency: Dependency[T]
            manifest: DomainManifest[T]
            common: Optional[CommonToolkit]
        """
        self._dependency = dependency
        self._manifest = manifest
        self._common = common or CommonToolkit()
    
    @property
    def dependency(self) -> ServiceDependency[T]:
        return self._dependency
    
    @property
    def manifest(self) -> DomainManifest[T]:
        return self._manifest
    
    @property
    def identity_service(self) -> IdentityService:
        return self._common.identity_service
    
    @property
    def number_validator(self) -> NumberValidator:
        return self._common.number_validator
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._common.priming_validator
    
    @property
    def blueprint_id_extractor(self) -> BlueprintIdExtractor:
        return self._common.blueprint_id_extractor
    
    @property
    def nulls(self) -> NullWarningSet[T]:
        return self._manifest.nulls
    
    @property
    def types(self) -> Layer[T]:
        return self._manifest.types
    

    
