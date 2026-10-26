# src/domain/metadata/unions/model/alert/types.py

"""
Module: domain.metadata.unions.model.alert.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Alert, ModelLayer
from transit import AlertCarrier


class AlertLayer(ModelLayer[Alert]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Alert.

    Attributes:
        model: Type[Alert]
        carrier: Type[AlertCarrier]
        blueprint: Type[AlertBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Alert]] | None = None,
            carrier: Optional[Type[AlertCarrier]] | None = None, 
            blueprint: Optional[Type[AlertBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Alert]]
            carrier: Optional[Type[AlertCarrier]
            blueprint: Optional[Type[AlertBlueprint] 
        """
        super().__init__(
            model=model or Alert,
            carrier=carrier or AlertCarrier, 
            blueprint=blueprint or AlertBlueprint
        )
    
    @property
    def model(self) -> Type[Alert]:
        return cast(Type[Alert], super().model)
    
    @property
    def carrier(self) -> Type[AlertCarrier]:
        return cast(Type[AlertCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[AlertBlueprint]:
        return cast(Type[AlertBlueprint], super().blueprint)