# src/toolkit/space/reservoir/quadrant/toolkit.py

"""
Module: toolkit.space.reservoir.quadrant.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from fabrication.blueprint import QuadrantReservoirBlueprint
from carrier import QuadrantReservoirCarrier
from err import QuadrantReservoirNullException, SpaceReservoirNullException
from space import Quadrant, QuadrantReservoir
from toolkit import MathToolkit, SpaceReservoirToolkit


class QuadrantReservoirToolkit(SpaceReservoirToolkit[Quadrant]):
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
            model: Type[QuadrantReservoir] = QuadrantReservoir,
            carrier_model: Type[QuadrantReservoirCarrier] = QuadrantReservoirCarrier,
            blueprint_model: Type[QuadrantReservoirBlueprint] = QuadrantReservoirBlueprint,
            
            null_exception: QuadrantReservoirNullException = QuadrantReservoirNullException(),
            carrier_null_exception: QuadrantReservoirCarrierNullException = QuadrantReservoirCarrierNullException(),
            blueprint_null_exception: QuadrantReservoirBlueprintNullException = QuadrantReservoirBlueprintNullException(),
            
            math_toolkit: Optional[MathToolkit] | None = None,
    ):
        """
        Args:
            model: Type[QuadrantReservoir] = QuadrantReservoir,
            carrier_model: Type[QuadrantReservoirCarrier] = QuadrantReservoirCarrier,
            blueprint_model: Type[QuadrantReservoirBlueprint] = QuadrantReservoirBlueprint,
            
            null_exception: QuadrantReservoirNullException = QuadrantReservoirNullException(),
            carrier_null_exception: QuadrantReservoirCarrierNullException = QuadrantReservoirCarrierNullException(),
            blueprint_null_exception: QuadrantReservoirBlueprintNullException = QuadrantReservoirBlueprintNullException(),
            
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
    def model(self) -> Type[QuadrantReservoir]:
        return cast(Type[QuadrantReservoir], super().model)
    
    @property
    def carrier_model(self) -> Type[QuadrantReservoirCarrier]:
        return cast(Type[QuadrantReservoirCarrier], super().carrier_model)
    
    @property
    def blueprint_model(self) -> Type[QuadrantReservoirBlueprint]:
        return cast(Type[QuadrantReservoirBlueprint], super().blueprint_model)
    
    @property
    def null_exception(self) -> SpaceReservoirNullException:
        return cast(SpaceReservoirNullException, super().null_exception)
    
    @property
    def carrier_null_exception(self) -> SpaceReservoirCarrierNullException:
        return cast(SpaceReservoirCarrierNullException, super().carrier_null_exception)
    
    @property
    def blueprint_null_exception(self) -> SpaceReservoirBlueprintNullException:
        return cast(SpaceReservoirBlueprintNullException, super().blueprint_null_exception)

