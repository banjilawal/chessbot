# src/operation/toolkit/request/insertion/node/toolkit.py

"""
Module: operation.toolkit.request.insertion.node.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar, cast

from collection import Chain
from err import ChainNullException, NodeNullException, RequestNullException
from domain.structure.node import Node
from domain.exchange.request import AddNodeRequest

from operation.toolkit import InsertPermissionRuleset

T = TypeVar("T", bound="Node")


class AddNodeRequestToolkit(InsertPermissionRuleset[Chain], Generic[T]):
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
    _node_type: Type[T]
    _node_null_exception: NodeNullException
    
    def __init__(
            self,
            node_type: Type[T],
            collection_type: Type[Chain] = Chain,
            request_type: Type[AddNodeRequest] = AddNodeRequest,
            request_null_exception: RequestNullException = RequestNullException(),
            collection_null_exception: ChainNullException = ChainNullException(),
            node_null_exception: NodeNullException = NodeNullException(),
    ):
        super().__init__(
            request_type=request_type,
            collection_type=collection_type,
            request_null_exception=request_null_exception,
            collection_null_exception=collection_null_exception
        )
        self._node_type = node_type
        self._node_null_exception = node_null_exception
        
    @property
    def node_type(self) -> Type[T]:
        return self._node_type
    
    @property
    def collection_type(self) -> Type[Chain]:
        return cast(Type[Chain], super().collection_type)
        
    @property
    def request_type(self) -> Type[T]:
        return cast(Type[AddNodeRequest], super().request_type)
    
    @property
    def node_null_exception(self) -> NodeNullException:
        return self._node_null_exception

    @property
    def collection_null_exception(self) -> CollectionNullException:
        return cast(ChainNullException, super().collection_null_exception)
    
    @property
    def request_null_exception(self) -> RequestNullException:
        return cast(RequestNullException, super().request_null_exception)