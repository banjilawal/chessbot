# src/mapping/stream/quadrant/mapper.py

"""
Module: mapping.stream.quadrant.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple, Type, cast

from mapper import (
    NortheastQuadrantMapFunction, NorthwestQuadrantMapFunction, QuadrantMappingFunction,
    SoutheastQuadrantMapFunction, SouthwestQuadrantMapFunction, SpaceMapFunctionStream
)
from space import (
    Quadrant, QuadrantReservoir, NortheastQuadrant, NorthwestQuadrant, SoutheastQuadrant, SouthwestQuadrant
)


class QuadrantMappingFunctionStream(SpaceMapFunctionStream[Quadrant]):
    """
    Role:
        -   Computation
        -   Factory
        -   Switcher

    Responsibilities:
        1.  QuadrantMappingFunction factory whose products don't need down-casting before use.
        2.  Binding a Quadrant to the appropriate mapping function.


    Attributes:
        space_reservoir: Quadrant
    
        stream_size: int
        streams_are_empty: bool
        streams_are_not_empty: bool
        
        northeast_mapping_function: Optional[NortheastQuadrantMapFunction]:
        northwest_mapping_function: Optional[NorthwestQuadrantMapFunction]:
        southwest_mapping_function: Optional[SouthwestQuadrantMapFunction]:
        southeast_mapping_function:  Optional[SoutheastQuadrantMapFunction]:
        
        northeast_quadrant_map_tuple: Tuple[NortheastQuadrant, NortheastQuadrantMapFunction]:
        northwest_quadrant_map_tuple: Tuple[NorthwestQuadrant, NorthwestQuadrantMapFunction]:
        southeast_quadrant_map_tuple: Tuple[SoutheastQuadrant, SoutheastQuadrantMapFunction]:
        southwest_quadrant_map_tuple: Tuple[SouthwestQuadrant, SouthwestQuadrantMapFunction]:
        type_mapper_dict: Dict[Type[QuadrantMappingFunction], QuadrantMappingFunctionStream]:

    Provides:

    Super Class:
        SpaceMapFunctionStream
    """
    _function_stream: Dict[Quadrant, QuadrantMappingFunction]
 
    
    def __init__(self, space_reservoir: QuadrantReservoir):
        """
        Args:
            space_reservoir: QuadrantReservoir
        """
        super().__init__(space_reservoir=space_reservoir)
        
        self._function_stream = {
            space_reservoir.northeast: NortheastQuadrantMapFunction(),
            space_reservoir.northwest: NorthwestQuadrantMapFunction(),
            space_reservoir.southeast: SoutheastQuadrantMapFunction(),
            space_reservoir.southwest: SouthwestQuadrantMapFunction(),
        }
        
    @property
    def space_reservoir(self) -> QuadrantReservoir:
        return cast(QuadrantReservoir, super().space_reservoir())
    
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
    def northeast_mapping_function(self) -> NortheastQuadrantMapFunction:
        return cast(
            NortheastQuadrantMapFunction,
            self._function_stream[self.space_reservoir.northeast]
        )
    
    @property
    def northwest_mapping_function(self) -> Optional[NorthwestQuadrantMapFunction]:
        return cast(
            NorthwestQuadrantMapFunction,
            self._function_stream[self.space_reservoir.northwest]
        )
    
    @property
    def southwest_mapping_function(self) -> Optional[SouthwestQuadrantMapFunction]:
        return cast(
            SouthwestQuadrantMapFunction,
            self._function_stream[self.space_reservoir.southwest]
        )
    
    @property
    def southeast_mapping_function(self) -> Optional[SoutheastQuadrantMapFunction]:
        return cast(
            SoutheastQuadrantMapFunction,
            self._function_stream[self.space_reservoir.southeast]
        )
    
    @property
    def northeast_quadrant_map_tuple(self) -> Tuple[NortheastQuadrant, NortheastQuadrantMapFunction]:
        return (
            self.space_reservoir.northeast,
            self.northeast_mapping_function,
        )
    
    @property
    def northwest_quadrant_map_tuple(self) -> Tuple[NorthwestQuadrant, NorthwestQuadrantMapFunction]:
        return (
            self.space_reservoir.northwest,
            self.northwest_mapping_function,
        )
    
    @property
    def southeast_quadrant_map_tuple(self) -> Tuple[SoutheastQuadrant, SoutheastQuadrantMapFunction]:
        return (
            self.space_reservoir.southeast,
            self.southeast_mapping_function,
        )
    
    @property
    def southwest_quadrant_map_tuple(self) -> Tuple[SouthwestQuadrant, SouthwestQuadrantMapFunction]:
        return (
            self.space_reservoir.southwest,
            self.southwest_mapping_function,
        )

    
    @property
    def type_mapper_dict(self) -> Dict[Type[QuadrantMappingFunction], QuadrantMappingFunctionStream]:
        """
        Simple iteration through the quadrant mapping functions is not useful because the need down-casting
        Using type as the iterator key surmount can automate casting without requiring isinstance calls.
        """
        return {
            Type[NortheastQuadrantMapFunction]: self.northeast_mapping_function,
            Type[NorthwestQuadrantMapFunction]: self.northwest_mapping_function,
            Type[SoutheastQuadrantMapFunction]: self.southeast_mapping_function,
            Type[SouthwestQuadrant]: self.southwest_mapping_function,
        }

        