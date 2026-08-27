# src/operation/toolkit/space/axis/toolkit.py

"""
Module: operation.toolkit.space.axis.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from carrier import EntityCarrier
from err import (
    AxisBlueprintNullException, AxisCarrierNullException, AxisNullException
)
from operation.toolkit.geometry.space.axis.toolkit import SpaceToolkit

T = TypeVar("T", bound="Axis")


class AxisToolkit(SpaceToolkit, Generic[T]):
    """
    Role:
        - Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianSpace tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[T]
        carrier_model: Type[EntityCarrier[T]]
        blueprint_model: Type[Blueprint[T]]
        
        null_exception: Optional[AxisNullException]
        carrier_null_exception: Optional[AxisCarrierNullException]
        blueprint_null_exception: Optional[AxisBlueprintNullException]

    Provides:

    Super Class:
        Toolkit
    """
    def __init__(
            self,
            model: Type[T],
            carrier_model: Type[EntityCarrier[T]],
            blueprint_model: Type[Blueprint[T]],
         
            null_exception: Optional[AxisNullException] |
                            None = AxisNullException(),
            carrier_null_exception: Optional[AxisCarrierNullException] |
                                    None = AxisCarrierNullException(),
            blueprint_null_exception: Optional[AxisBlueprintNullException] |
                                      None = AxisBlueprintNullException(),
    ):
        """
        Args:
            model: Type[T]
            carrier_model: Type[EntityCarrier[T]]
            blueprint_model: Type[Blueprint[T]]
            
            null_exception: Optional[AxisNullException]
            carrier_null_exception: Optional[AxisCarrierNullException]
            blueprint_null_exception: Optional[AxisBlueprintNullException]
        """
        super().__init__(
            model=model,
            carrier_model=carrier_model,
            blueprint_model=blueprint_model,
            
            null_exception=null_exception,
            carrier_null_exception=carrier_null_exception,
            blueprint_null_exception=blueprint_null_exception,
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier_model(self) -> Type[EntityCarrier[T]]:
        return cast(Type[EntityCarrier[T]], super().carrier_model)
    
    @property
    def blueprint_model(self) -> Type[Blueprint[T]]:
        return cast(Type[Blueprint[T]], super().blueprint_model)
    
    @property
    def null_exception(self) -> AxisNullException:
        return cast(AxisNullException, super().request_null_exception)
    
    @property
    def carrier_null_exception(self) -> AxisCarrierNullException:
        return cast(AxisCarrierNullException, super().carrier_null_exception)
    
    @property
    def blueprint_null_exception(self) -> AxisBlueprintNullException:
        return cast(AxisBlueprintNullException, super().blueprint_null_exception)



