# src/toolkit/space/reservoir/toolkit.py

"""
Module: toolkit.space.reservoir.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Generic, Optional, Type, TypeVar, cast

from fabrication.blueprint import SpaceReservoirBlueprint
from carrier import SpaceReservoirCarrier
from err.null.carrier.space.reservoir import SpaceReservoirNullException
from toolkit.registry.space.toolkit import MathToolkit, Toolkit

T = TypeVar("T", bound="SpaceReservoir")

@dataclass
class SpaceReservoirToolkit(Toolkit, Generic[T]):
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
        Toolkit
    """
    _model: Type[T]
    _carrier_model: Type[SpaceReservoirCarrier[T]]
    _blueprint_model: Type[SpaceReservoirBlueprint[T]]
    
    _null_exception: Optional[SpaceReservoirNullException]
    _carrier_null_exception: Optional[SpaceReservoirCarrierNullException]
    _blueprint_null_exception: Optional[SpaceReservoirBlueprintNullException]
    
    _math_toolkit: Optional[MathToolkit]

    def __init__(
            self,
            model: Type[T],
            carrier_model: Type[SpaceReservoirCarrier[T]],
            blueprint_model: Type[SpaceReservoirBlueprint[T]],
            
            null_exception: Optional[SpaceReservoirNullException] |
                            None = SpaceReservoirNullException(),
            carrier_null_exception: Optional[SpaceReservoirCarrierNullException] |
                                    None = SpaceEReservoirCarrierNullException(),
            blueprint_null_exception: Optional[SpaceReservoirBlueprintNullException] |
                                      None = SpaceReservoirBlueprintNullException(),
            
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            model: Type[T]
            carrier_model: Type[EntityCarrier[T]]
            blueprint_model: Type[Blueprint[T]]
    
            null_exception: Optional[SpaceNullException]
            carrier_null_exception: Optional[SpaceCarrierNullException]
            blueprint_null_exception: Optional[SpaceBlueprintNullException]
    
            math_toolkit: Optional[MathToolkit]
        """
        super().__init__()
        self._model = model
        self._carrier_model = carrier_model
        self._blueprint_model = blueprint_model
        
        self._null_exception = null_exception
        self._carrier_null_exception = carrier_null_exception
        self._blueprint_null_exception = blueprint_null_exception
        
        self._math_toolkit = math_toolkit
    
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], self._model)
    
    @property
    def carrier_model(self) -> Type[SpaceReservoirCarrier[T]]:
        return cast(Type[T], self._carrier_model)
    
    @property
    def blueprint_model(self) -> Type[SpaceReservoirBlueprint[T]]:
        return cast(Type[SpaceReservoirBlueprint[T]], self().blueprint_model)
    
    
    @property
    def null_exception(self) -> SpaceReservoirNullException:
        return cast(SpaceReservoirNullException, super().request_null_exception)
    
    
    @property
    def carrier_null_exception(self) -> SpaceReservoirCarrierNullException:
        return cast(SpaceReservoirCarrierNullException, super().carrier_null_exception)
    
    
    @property
    def blueprint_null_exception(self) -> SpaceReservoirBlueprintNullException:
        return cast(SpaceReservoirBlueprintNullException, super().blueprint_null_exception)
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    



