# src/domain/metadata/blueprint/container/blueprint.py

"""
Module: domain.metadata.blueprint.container.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Tuple, Type, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from collection import Container
from err import ContainerNullException, TupleNullException


class ContainerBlueprint(Blueprint[Container]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Container object
 

     Attributes:
        container_class: Type[Container]
        domain_null_exception: ContainerNullException
        tuple_domain_null_exception: Optional[TupleNullException]
         
     Provides:

     Super Class:
        Blueprint
     """
    
    T = TypeVar("T", bound="Container")
    
    _entries: Tuple[T, ...]
    _tuple_domain_null_exception: TupleNullException
    
    def __init__(
            self,
            entries: Tuple[T, ...],
            container_class: Type[Container[T]] = Container,
            domain_null_exception: ContainerNullException | None = ContainerNullException(),
            tuple_domain_null_exception: Optional[TupleNullException] | None = TupleNullException(),
    ):
        """
        Args:
            container_class: Type[Container[T]]
            domain_null_exception: ContainerNullException
            tuple_domain_null_exception: Optional[TupleNullException]
        """
        super().__init__(
            domain_class=container_class,
            domain_null_exception=domain_null_exception,
        )
        self._entries = entries
        self._tuple_domain_null_exception = tuple_domain_null_exception
        
    
    @property
    def container_class(self) -> Type[Container]:
        return cast(Type[Container], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ContainerNullException:
        return cast(ContainerNullException, super().domain_null_exception)
    
    @property
    def entries(self) -> Tuple[T, ...]:
        return self._entries
    
    @property
    def tuple_domain_null_exception(self) -> TupleNullException:
        return self.tuple_domain_null_exception
