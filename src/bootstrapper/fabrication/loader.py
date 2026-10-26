# src/bootstrap/fabrication/loader.py

"""
Module: bootstrap.fabrication.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import BuildResult
from assurance import PrimingValidator
from bootstrapper import Loader
from domain import Blueprint
from exchange import BuildRequest, ValidationService
from microservice import IdentityService
from util import LoggingLevelRouter

T = TypeVar("T")


class BuildLoader(Loader[T], ABC, Generic[T]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Bootstraps the Build process by assuring the request is valid and its
            inspecting the job's requirements.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        validator: ValidationServer[T]

    Provides:
            -   def execute(request: BuildRequest[T]) -> BuildResult[Blueprint[T]]

    Super Class:
    """
    _validator: ValidationService[T]
    _identity_service: IdentityService
    _priming_validator: PrimingValidator

    
    def __init__(
            self,
            validator: ValidationService[T],
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            validator: ValidationServer[T]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        self._validator = validator
        self._identity_service = identity_service
        self._priming_validator = priming_validator
    
    @property
    def validator(self) -> ValidationService[T]:
        return self._validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: BuildRequest[T]) -> BuildResult[Blueprint[T]]:
        """
        Prepare a Blueprint which is used to build a safe product.

        Args:
            request: BuildRequest[T]
        Returns:
            BuildResult[Blueprint[T]]
        Raises:
            BuildLoaderException
        """
        pass