# src/operation/toolkit/request/insertion/toolkit.py

"""
Module: operation.toolkit.request.insertion.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar, cast

from collection import DomainObjectCollection
from err import CollectionNullException, RequestNullException
from artifcat.result import InsertionResult
from operation.toolkit import PermissionRuleset

T = TypeVar("T", bound="DomainObjectCollection")


class InsertPermissionRuleset(PermissionRuleset[InsertionResult], Generic[T]):
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
    _collection_type: Type[DomainObjectCollection]
    _request_null_exception: RequestNullException
    _collection_null_exception: CollectionNullException
    
    
    def __init__(
            self,
            request_type: Type[T],
            collection_type: Type[DomainObjectCollection],
            request_null_exception: RequestNullException,
            collection_null_exception: CollectionNullException,
    ):
        super().__init__(request_type=request_type, request_null_exception=request_null_exception)
        self._collection_type = collection_type
        self._collection_null_exception = collection_null_exception
        
    @property
    def request_type(self) -> Type[T]:
        return self._request_type
    
    @property
    def collection_type(self) -> Type[DomainObjectCollection]:
        return self._collection_type
    
    @property
    def request_null_exception(self) -> RequestNullException:
        return cast(RequestNullException, super().request_null_exception)

    @property
    def collection_null_exception(self) -> CollectionNullException:
        return self._collection_null_exception