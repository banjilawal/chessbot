# src/toolkit/model/toolkit.py

"""
Module: toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar

from pluggy import Result

from err import RequestNullException
from toolkit import Toolkit

T = TypeVar("T", bound="Result")



class RequestToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Aggregates workers and services a model requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Type[T]
        carrier_model: Type[EntityCarrier[T]]
        blueprint_model: Type[Blueprint[T]]
        
        null_exception: ModelNullException
        blueprint_null_exception: BlueprintNullException
        carrier_null_exception: EntityCarrierNullException
        
    Provides:
        
    Super Class:
       Toolkit
    """
    _request_type: Type[T]
    _request_null_exception: RequestNullException
    
    
    def __init__(self, request_type: Type[T], request_null_exception: RequestNullException):
        super().__init__()
        self._request_type = request_type
        self._request_null_exception = request_null_exception
        
    @property
    def request_type(self) -> Type[T]:
        return self._request_type
    
    @property
    def request_null_exception(self) -> RequestNullException:
        return self._request_null_exception
    


