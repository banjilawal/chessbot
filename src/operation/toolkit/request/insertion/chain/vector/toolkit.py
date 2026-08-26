# src/operation/toolkit/request/insertion/node/vector/toolkit.py

"""
Module: operation.toolkit.request.insertion.node.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from assurance import VectorValidator
from collection import VectorChain
from err import AddVectorNodeRequestNullException, VectorNodeNullException, VectorChainNullException
from domain.structure.node import VectorNode
from domain.exchange.request import AddVectorNodeRequest
from operation.toolkit import AddNodeRequestToolkit


class AddVectorNodeRequestToolkit(AddNodeRequestToolkit[VectorNode]):
    """
    Role:
        -  Dependency Management
        
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
    _vector_validator: VectorValidator = VectorValidator()
    
    def __init__(
            self,
            node_type: Type[VectorNode] = VectorNode,
            collection_type: Type[VectorChain] = VectorChain,
            request_type: Type[AddVectorNodeRequest] = AddVectorNodeRequest,
            request_null_exception: Optional[RequestNullException]
                                    | None = None,
            collection_null_exception: Optional[NullException]
                                       | None = None,
            node_null_exception: Optional[VectorNodeNullException]
                                 | None = None,
            vector_validator: Optional[VectorValidator]
                              | None = None,
    ):
        super().__init__(
            node_type=node_type,
            request_type=request_type,
            collection_type=collection_type,
            request_null_exception=(
                    request_null_exception or AddVectorNodeRequestNullException()
            ),
            collection_null_exception=(
                    collection_null_exception or VectorChainNullException()
            ),
            node_null_exception=(
                    node_null_exception or VectorNodeNullException()
            ),
        )
        self._vector_validator = vector_validator or VectorValidator()
        
    @property
    def vector_validator(self) -> VectorValidator:
        return self._vector_validator
    
    @property
    def collection_type(self) -> Type[VectorChain]:
        return cast(
            Type[VectorChain], super().collection_type
        )
    
    @property
    def request_type(self) -> Type[AddVectorNodeRequest]:
        return cast(
            Type[AddVectorNodeRequest], super().request_type
        )
    
    @property
    def node_null_exception(self) -> VectorNodeNullException:
        return cast(
            VectorNodeNullException, super().node_null_exception
        )
    
    @property
    def collection_null_exception(self) -> VectorChainNullException:
        return cast(
            VectorChainNullException, super().collection_null_exception
        )
    
    @property
    def request_null_exception(self) -> AddVectorNodeRequestNullException:
        return cast(
            AddVectorNodeRequestNullException, super().request_null_exception
        )