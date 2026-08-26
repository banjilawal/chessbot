# src/operation/toolkit/validator/toolkit.py

"""
Module: operation.toolkit.validator.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, Type, TypeVar

from assurance import PrimingValidator
from err import BlueprintNullException, EntityCarrierNullException, ModelNullException
from fabrication import Blueprint
from microservice import IdentityService
from domain.model import DataModel
from transit.carrier import EntityCarrier

T = TypeVar("T", bound="DataModel")


class ModelManifest(ABC, Generic[T]):
    """
    Role:
        -   Dependency Manager

    Responsibilities:
        1.  Bundles a Model's validation dependencies.
        2.  Unify ModelValidation method signatures.

    Attributes:
        identity_service: Optional[IdentityService]
        priming_validator: Optional[PrimingValidator]
        
        model_type: Type[T]
        blueprint_type: Type[Blueprint[T]]
        carrier_type: Type[EntityCarrier[T]]
        
        model__null_exception: ModelNullException
        blueprint_null_exception: BlueprintNullException
        carrier_null_exception: EntityCarrierNullException

    Provides:

    Super
    """
    _defaults: Dict[str, Any] = {}
    _resources: Dict[str, Any] = {}
    
    def __init__(
            self,
            resources: Dict[str, Any],
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            types: Dict[str, Type[Any]],
            nulls: Dict[str, NullException],
            resources: Dict[str, Any],
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        self._defaults["identity_service"] = identity_service or IdentityService()
        self._defaults["priming_validator"] = priming_validator or PrimingValidator()
        
        self._resources = resources
        
    @property
    def identity_service(self) -> IdentityService:
        return self._defaults["identity_service"]
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._defaults["priming_validator"]
    
    @property
    def resources(self) -> Dict[str, Any]:
        return self._resources
    
    @property
    @abstractmethod
    def model_type(self) -> Type[T]:
        pass
    
    @property
    @abstractmethod
    def blueprint_type(self) -> Type[Blueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def carrier_type(self) -> Type[EntityCarrier[T]]:
        pass
    
    @property
    @abstractmethod
    def model__null_exception(self) -> ModelNullException:
        pass
    
    @property
    @abstractmethod
    def blueprint_null_exception(self) -> BlueprintNullException:
        pass
    
    @property
    @abstractmethod
    def carrier_null_exception(self) -> EntityCarrierNullException:
        pass
