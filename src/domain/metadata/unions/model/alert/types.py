# src/domain/metadata/unions/model/alert/types.py

"""
Module: domain.metadata.unions.model.alert.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import AlertTable, ModelTypeUnion
from transit import AlertTableCarrier


class AlertTableTypeUnion(ModelTypeUnion[AlertTable]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an AlertTable.

    Attributes:
        model: Type[AlertTable]
        carrier: Type[AlertTableCarrier]
        blueprint: Type[AlertTableBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[AlertTable]] | None = None,
            carrier: Optional[Type[AlertTableCarrier]] | None = None, 
            blueprint: Optional[Type[AlertTableBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[AlertTable]]
            carrier: Optional[Type[AlertTableCarrier]
            blueprint: Optional[Type[AlertTableBlueprint] 
        """
        super().__init__(
            model=model or AlertTable, 
            carrier=carrier or AlertTableCarrier, 
            blueprint=blueprint or AlertTableBlueprint
        )
    
    @property
    def model(self) -> Type[AlertTable]:
        return cast(Type[AlertTable], super().model)
    
    @property
    def carrier(self) -> Type[AlertTableCarrier]:
        return cast(Type[AlertTableCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[AlertTableBlueprint]:
        return cast(Type[AlertTableBlueprint], super().blueprint)