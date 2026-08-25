# src/domain/metadata/blueprint/model/blueprint.py

"""
Module: domain.metadata.blueprint.model.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Optional, Type, cast

from domain.metadata.blueprint import Blueprint
from err import ModelNullException
from domain.model import DataModelObject


class ModelBlueprint(Blueprint[DataModelObject]):
    """
     Role:
         -   Metadata

     Responsibilities:
         1.  Provide attribute-value tuples for hydrating a Model.

     Attributes:
         model_class: Type[T]
         null_exception: StructureNullException
         model_class_name: str

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            model_class: Type[DataModelObject],
            null_exception: Optional[ModelNullException] | None = ModelNullException(),
    ):
        """
        Args:
            model_class: Type[Model[T]]
            null_exception: Optional[ModelNullException]
        """
        super().__init__(
            model_class=model_class,
            null_exception=null_exception
        )
    
    @property
    def model_class(self) -> Type[DataModelObject]:
        return cast(Type[DataModelObject], super().model_class)
    
    @property
    def null_exception(self) -> ModelNullException:
        return cast(ModelNullException, super().null_exception)
    
    
