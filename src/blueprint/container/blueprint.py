# src/blueprint/container/blueprint.py

"""
Module: blueprint.container.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Tuple, Type, TypeVar, cast

from blueprint import Blueprint
from container import Container
from err import ContainerNullException, TupleNullException


class ContainerBlueprint(Blueprint[Container]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Container object
         2.  DTO

     Attributes:
        container_class: Type[Container]
        null_exception: ContainerNullException
        tuple_null_exception: Optional[TupleNullException]
         
     Provides:

     Super Class:
        Blueprint
     """
    
    T = TypeVar("T", bound="Container")
    
    _entries: Tuple[T, ...]
    _tuple_null_exception: TupleNullException
    
    def __init__(
            self,
            entries: Tuple[T, ...],
            container_class: Type[Container[T]] = Container,
            null_exception: ContainerNullException | None = ContainerNullException(),
            tuple_null_exception: Optional[TupleNullException] | None = TupleNullException(),
    ):
        """
        Args:
            container_class: Type[Container[T]]
            null_exception: ContainerNullException
            tuple_null_exception: Optional[TupleNullException]
        """
        super().__init__(
            model_class=container_class,
            null_exception=null_exception,
        )
        self._entries = entries
        self._tuple_null_exception = tuple_null_exception
        
    
    @property
    def container_class(self) -> Type[Container]:
        return cast(Type[Container], super().model_class)
    
    @property
    def null_exception(self) -> ContainerNullException:
        return cast(ContainerNullException, super().null_exception)
    
    @property
    def entries(self) -> Tuple[T, ...]:
        return self._entries
    
    @property
    def tuple_null_exception(self) -> TupleNullException:
        return self.tuple_null_exception
