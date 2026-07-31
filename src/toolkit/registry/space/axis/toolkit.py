# src/toolkit/space/reservoir/axis/toolkit.py

"""
Module: toolkit.space.reservoir.axis.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import AxisReservoirBlueprint
from carrier import AxisReservoirCarrier
from err import AxisReservoirNullException, SpaceReservoirNullException
from registry import AxisReservoir
from geometry.space import Axis
from toolkit import MathToolkit, SpaceReservoirToolkit


class AxisReservoirToolkit(SpaceReservoirToolkit[Axis]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianSpace tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        space: Type[T]
        blueprint_space: Blueprint[T]
        
        null_exception: SpaceNullException
        blueprint_null_exception: SpaceBlueprintNullException

    Provides:

    Super Class:
        SpaceReservoirToolkit
    """

    
    def __init__(
            self,
            model: Type[AxisReservoir] = AxisReservoir,
            carrier_model: Type[AxisReservoirCarrier] = AxisReservoirCarrier,
            blueprint_model: Type[AxisReservoirBlueprint] = AxisReservoirBlueprint,
            
            null_exception: AxisReservoirNullException = AxisReservoirNullException(),
            carrier_null_exception: AxisReservoirCarrierNullException = AxisReservoirCarrierNullException(),
            blueprint_null_exception: AxisReservoirBlueprintNullException = AxisReservoirBlueprintNullException(),
            
            math_toolkit: Optional[MathToolkit] | None = None,
    ):
        """
        Args:
            model: Type[AxisReservoir] = AxisReservoir,
            carrier_model: Type[AxisReservoirCarrier] = AxisReservoirCarrier,
            blueprint_model: Type[AxisReservoirBlueprint] = AxisReservoirBlueprint,
            
            null_exception: AxisReservoirNullException = AxisReservoirNullException(),
            carrier_null_exception: AxisReservoirCarrierNullException = AxisReservoirCarrierNullException(),
            blueprint_null_exception: AxisReservoirBlueprintNullException = AxisReservoirBlueprintNullException(),
            
            math_toolkit: Optional[MathToolkit]
        """
        super().__init__(
            model=model,
            carrier_model=carrier_model,
            blueprint_model=blueprint_model,
            null_exception = null_exception,
            carrier_null_exception=carrier_null_exception,
            blueprint_null_exception=blueprint_null_exception,
            math_toolkit = math_toolkit,
        )
    @property
    def model(self) -> Type[AxisReservoir]:
        return cast(Type[AxisReservoir], super().model)
    
    @property
    def carrier_model(self) -> Type[AxisReservoirCarrier]:
        return cast(Type[AxisReservoirCarrier], super().carrier_model)
    
    @property
    def blueprint_model(self) -> Type[AxisReservoirBlueprint]:
        return cast(Type[AxisReservoirBlueprint], super().blueprint_model)
    
    @property
    def null_exception(self) -> SpaceReservoirNullException:
        return cast(SpaceReservoirNullException, super().null_exception)
    
    @property
    def carrier_null_exception(self) -> SpaceReservoirCarrierNullException:
        return cast(SpaceReservoirCarrierNullException, super().carrier_null_exception)
    
    @property
    def blueprint_null_exception(self) -> SpaceReservoirBlueprintNullException:
        return cast(SpaceReservoirBlueprintNullException, super().blueprint_null_exception)

