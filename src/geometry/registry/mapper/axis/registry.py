# src/mapping/stream/axis/mapper.py

"""
Module: mapping.stream.axis.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Optional, Tuple, Type, cast

from geometry.mapper import (
    AxisMappingFunction, EastAxisMapFunction, SpaceMapFunctionStream, NorthAxisMapFunction,
    SouthAxisMapFunction, WestAxisMapFunction
)
from geometry.space import Axis, AxisReservoir, EastAxis, NorthAxis, SouthAxis, WestAxis


class AxisMappingFunctionStream(SpaceMapFunctionStream[Axis]):
    """
    Role:
        -   Data Holder
        -   Factory
        -   Switcher

    Responsibilities:
        1.  AxisMappingFunction factory whose products don't need down-casting before use.
        2.  Binding a Axis to the appropriate mapping function.


    Attributes:
        space_reservoir: Axis

        stream_size: int
        streams_are_empty: bool
        streams_are_not_empty: bool

        east_mapping_function: Optional[EastAxisMapFunction]:
        north_mapping_function: Optional[NorthAxisMapFunction]:
        east_mapping_function: Optional[EastAxisMapFunction]:
        west_mapping_function:  Optional[WestAxisMapFunction]:

        east_axis_map_tuple: Tuple[EastAxis, EastAxisMapFunction]:
        north_axis_map_tuple: Tuple[NorthAxis, NorthAxisMapFunction]:
        west_axis_map_tuple: Tuple[WestAxis, WestAxisMapFunction]:
        east_axis_map_tuple: Tuple[EastAxis, EastAxisMapFunction]:
        type_mapper_dict: Dict[Type[AxisMappingFunction], AxisMappingFunctionStream]:

    Provides:

    Super Class:
        SpaceMapFunctionStream
    """
    
    _function_stream: Dict[Axis, AxisMappingFunction]
 
    
    def __init__(self, space_reservoir: AxisReservoir):
        """
        Args:
            space_reservoir: AxisReservoir
        """
        super().__init__(space_reservoir=space_reservoir)
        
        self._function_stream = {
            space_reservoir.east: EastAxisMapFunction(),
            space_reservoir.north: NorthAxisMapFunction(),
            space_reservoir.south: SouthAxisMapFunction(),
            space_reservoir.west: WestAxisMapFunction(),
        }
        
    @property
    def space_reservoir(self) -> AxisReservoir:
        return cast(AxisReservoir, super().space_reservoir())
    
    @property
    def stream_size(self) -> int:
        return len(self._function_stream)
    
    @property
    def streams_are_empty(self) -> bool:
        return self.stream_size == 0
    
    @property
    def streams_are_not_empty(self) -> bool:
        return not self.streams_are_empty
    
    @property
    def east_mapping_function(self) -> EastAxisMapFunction:
        return cast(
            EastAxisMapFunction,
            self._function_stream[self.space_reservoir.east]
        )
    
    @property
    def north_mapping_function(self) -> Optional[NorthAxisMapFunction]:
        return cast(
            NorthAxisMapFunction,
            self._function_stream[self.space_reservoir.north]
        )
    
    @property
    def west_mapping_function(self) -> Optional[WestAxisMapFunction]:
        return cast(
            WestAxisMapFunction,
            self._function_stream[self.space_reservoir.west]
        )
    
    @property
    def south_mapping_function(self) -> Optional[SouthAxisMapFunction]:
        return cast(
            SouthAxisMapFunction,
            self._function_stream[self.space_reservoir.south]
        )
    
    @property
    def east_axis_map_tuple(self) -> Tuple[EastAxis, EastAxisMapFunction]:
        return (
            self.space_reservoir.east,
            self.east_mapping_function,
        )
    
    @property
    def north_axis_map_tuple(self) -> Tuple[NorthAxis, NorthAxisMapFunction]:
        return (
            self.space_reservoir.north,
            self.north_mapping_function,
        )
    
    @property
    def west_axis_map_tuple(self) -> Tuple[WestAxis, WestAxisMapFunction]:
        return (
            self.space_reservoir.west,
            self.west_mapping_function,
        )
    
    @property
    def south_axis_map_tuple(self) -> Tuple[SouthAxis, SouthAxisMapFunction]:
        return (
            self.space_reservoir.south,
            self.south_mapping_function,
        )
    
    @property
    def type_mapper_dict(self) -> Dict[Type[AxisMappingFunction], AxisMappingFunctionStream]:
        """
        Simple iteration through the axis mapping functions is not useful because the need down-casting
        Using type as the iterator key surmount can automate casting without requiring isinstance calls.
        """
        return {
            Type[EastAxisMapFunction]: self.east_mapping_function,
            Type[NorthAxisMapFunction]: self.north_mapping_function,
            Type[SouthAxisMapFunction]: self.south_mapping_function,
            Type[WestAxisMapFunction]: self.west_mapping_function,
        }
        