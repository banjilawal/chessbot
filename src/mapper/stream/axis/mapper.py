# src/mapping/stream/axis/mapper.py

"""
Module: mapping.stream.axis.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple, cast

from mapper import (
    AxisMappingFunction, EastAxisMapFunction, SpaceMapFunctionStream, NorthAxisMapFunction,
    SouthAxisMapFunction, WestAxisMapFunction
)
from space import Axis, AxisReservoir, EastAxis, NorthAxis, SouthAxis, WestAxis


class AxisMappingFunctionStream(SpaceMapFunctionStream[Axis]):

    
    _function_stream: Dict[Axis, AxisMappingFunction]
 
    
    def __init__(self, space_reservoir: AxisReservoir):
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
    def stream_iterator(self) -> iter:
        """
        Using thr iterator means you have to check types and cast.
        """
        map_functions: List[AxisMappingFunction] = []
        
        for key in self._function_stream:
            map_functions.append(self._function_stream[key])
        return map_functions

        