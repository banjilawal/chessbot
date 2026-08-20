# src/toolkit/space/axis/north/toolkit.py

"""
Module: toolkit.space.axis.north.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Type, cast

from fabrication.blueprint.space.axis.north import NorthAxisBlueprint
from carrier import NorthAxisCarrier
from err import (
    AxisBlueprintNullException, AxisCarrierNullException, NorthAxisBlueprintNullException,
    NorthAxisCarrierNullException,
    NorthAxisNullException
)
from space import NorthAxis
from toolkit.geometry.space.axis.north.toolkit import AxisToolkit



class NorthAxisToolkit(AxisToolkit[NorthAxis]):
    """
    Role:
        -   Dependency Management

    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

    Attributes:
        model: Type[NorthAxis] = NorthAxis
        carrier_model: Type[NorthAxisCarrier] = NorthAxisCarrier
        blueprint_model: Type[NorthAxisBlueprint] =  NorthAxisBlueprint
        
        null_exception: NorthAxisNullException)
        carrier_null_exception: NorthAxisCarrierNullException
        blueprint_null_exception: NorthAxisBlueprintNullException
        
    Provides:

    Super Class:
        AxisToolkit
    """
    
    def __init__(
            self,
            model: Type[NorthAxis] = NorthAxis,
            carrier_model: Type[NorthAxisCarrier] = NorthAxisCarrier,
            blueprint_model: Type[NorthAxisBlueprint] = NorthAxisBlueprint,
            null_exception: NorthAxisNullException |
                            None = NorthAxisNullException(),
            carrier_null_exception: NorthAxisCarrierNullException |
                                    None = NorthAxisCarrierNullException(),
            blueprint_null_exception: (NorthAxisBlueprintNullException |
                                       None) = NorthAxisBlueprintNullException(),
    ):
        """
        Args:
            model: Type[NorthAxis] = NorthAxis
            carrier_model: Type[NorthAxisCarrier] = NorthAxisCarrier
            blueprint_model: Type[NorthAxisBlueprint] =  NorthAxisBlueprint
            
            null_exception: NorthAxisNullException)
            carrier_null_exception: NorthAxisCarrierNullException
            blueprint_null_exception: NorthAxisBlueprintNullException
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
    def model(self) -> Type[NorthAxis]:
        return cast(Type[NorthAxis], super().model)
    
    
    @property
    def carrier_model(self) -> Type[NorthAxisCarrier]:
        return cast(Type[NorthAxisCarrier], super().carrier_model)
    
    
    @property
    def blueprint_model(self) -> Type[NorthAxisBlueprint]:
        return cast(Type[NorthAxisBlueprint], super().blueprint_model)
    
    
    @property
    def null_exception(self) -> NorthAxisNullException:
        return cast(NorthAxisNullException, super().request_null_exception)

    @property
    def carrier_null_exception(self) -> AxisCarrierNullException:
        return cast(AxisCarrierNullException, super().carrier_null_exception)
    
    @property
    def blueprint_null_exception(self) -> AxisBlueprintNullException:
        return cast(AxisBlueprintNullException, super().blueprint_null_exception)
    


