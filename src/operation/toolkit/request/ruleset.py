# src/operation/toolkit/request/ruleset.py

"""
Module: operation.toolkit.request/ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar

from artifcat import Result
from assurance import PrimingValidator
from err import RequestNullException
from microservice import IdentityService


T = TypeVar("T", bound="Result")

class PermissionRuleset(ABC, Generic[T]):
    """
    Role:
        -   Dependency Management
        
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
    _request_type: Type[T]
    _request_null_exception: RequestNullException
    
    _identity_service: Optional[IdentityService]
    _priming_validator: Optional[PrimingValidator]
    
    
    
    def __init__(
            self,
            request_type: Type[T],
            request_null_exception: RequestNullException,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        self._request_type = request_type
        self._request_null_exception = request_null_exception
        
    @property
    def request_type(self) -> Type[T]:
        return self._request_type
    
    @property
    def request_null_exception(self) -> RequestNullException:
        return self._request_null_exception
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    
    


