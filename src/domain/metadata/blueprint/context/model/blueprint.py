# src/domain/metadata/blueprint/context/model/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import ContextBlueprint, ModelContext
from err import ModelContextNullException

T = TypeVar("T", bound="ModelContext")


class ModelContextBlueprint(ContextBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a ModelSearchContext.
         
     Attributes:
        domain_class: Type[T]
        domain_null_exception: ModelContextNullException

     Provides:

     Super Class:
        ContextBlueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: ModelContextNullException,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_size: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ModelContextNullException
            id: Optional[int]
            name: Optional[str]
            max_size: Optional[int]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
            id=id,
            name=name,
            max_size=max_size,
        )
        
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ModelContextNullException:
        return  cast(ModelContextNullException, super()._domain_null_exception)


