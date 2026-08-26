# src/operation/toolkit/request/ruleset.py

"""
Module: operation.toolkit.request/ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, Type, TypeVar

from artifcat import CrudResult
from assurance import PrimingValidator
from err import RequestNullException
from microservice import IdentityService


T = TypeVar("T", bound="CrudResult")

@dataclass
class PermissionRuleset(ABC, Generic[T]):
    """
    Role:
        -  Dependency Management
        
    Responsibilities:
        1.  Aggregates workers and services a model requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        request_type: Type[T]
        request_null_exception: RequestNullException
        
    Provides:
        
    Super Class:
    """
    request_type: Type[T] = T
    request_null_exception: RequestNullException = RequestNullException
    
    identity_service: Optional[IdentityService] = IdentityService
    priming_validator: Optional[PrimingValidator] = PrimingValidator
    
    integrity_checker: CrudChecker[T]
    

    #
    # @property
    # def priming_validator(self) -> PrimingValidator:
    #     return self._priming_validator
    #
    # @property
    # def identity_service(self) -> IdentityService:
    #     return self._identity_service
    
    
    


