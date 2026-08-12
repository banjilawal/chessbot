# src/toolkit/space/toolkit.py

"""
Module: toolkit.space.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



from typing import Generic, Optional, Type, TypeVar

from fabrication.blueprint import Blueprint
from carrier import EntityCarrier
from err import SpaceBlueprintNullException, SpaceCarrierNullException, SpaceNullException
from toolkit.geometry.space.toolkit import MathToolkit, Toolkit

T = TypeVar("T", bound="Space")


class SpaceToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianSpace tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[T]
        carrier_model: Type[EntityCarrier[T]]
        blueprint_model: Type[Blueprint[T]]
        
        null_exception: Optional[SpaceNullException]
        carrier_null_exception: Optional[SpaceCarrierNullException]
        blueprint_null_exception: Optional[SpaceBlueprintNullException]
        
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
        Toolkit
    """
    _model: Type[T]
    _carrier_model: Type[EntityCarrier[T]]
    _blueprint_model: Type[Blueprint[T]]
    
    _null_exception: Optional[SpaceNullException]
    _carrier_null_exception: Optional[SpaceCarrierNullException]
    _blueprint_null_exception: Optional[SpaceBlueprintNullException]
    
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            model: Type[T],
            carrier_model: Type[EntityCarrier[T]],
            blueprint_model: Type[Blueprint[T]],
            
            null_exception: Optional[SpaceNullException] |
                            None = SpaceNullException(),
            carrier_null_exception: Optional[SpaceCarrierNullException] |
                                    None = SpaceCarrierNullException(),
            blueprint_null_exception: Optional[SpaceBlueprintNullException] |
                                      None = SpaceBlueprintNullException(),
            
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
        self._model=model
        self._carrier_model = carrier_model
        self._blueprint_model =blueprint_model
        
        self._null_exception = null_exception
        self._carrier_null_exception = carrier_null_exception
        self._blueprint_null_exception = blueprint_null_exception
        
        self._math_toolkit = math_toolkit
        
    @property
    def model(self) -> Type[T]:
        return self._model
    
    @property
    def carrier_model(self) -> Type[EntityCarrier[T]]:
        return self._carrier_model
    
    @property
    def blueprint_model(self) -> Type[Blueprint[T]]:
        return self._blueprint_model
    
    @property
    def null_exception(self) -> SpaceNullException:
        return self._null_exception
    
    @property
    def carrier_null_exception(self) ->SpaceCarrierNullException:
        return self._carrier_null_exception
    
    @property
    def blueprint_null_exception(self) -> SpaceBlueprintNullException:
        return self._blueprint_null_exception
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit

