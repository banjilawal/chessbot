# src/recurrence/table/axis/space.py

"""
Module: recurrence.table.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, cast

from mapper import AxisMappingFunction, AxisMappingFunctionStream
from recurrence import EastAxisRecurrence, NorthAxisRecurrence, SpaceRecurrenceTable
from space import Axis, AxisReservoir



class AxisRecurrenceTable(SpaceRecurrenceTable[Axis]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store a set of space relations to run as a job.

    Attributes:
        space_set: Tuple[Space, ...]

    Provides:

    Super Class:
    """
    _space_mapping_function_stream: AxisMappingFunctionStream
    _recurrence_table: Dict[str, AxisReservoir]
    
    def __init__(
            self,
            space_mapping_function_stream: AxisMappingFunctionStream[T]
    ):
        """
        Args:
            space_mapping_function_stream: AxisMappingFunctionStream[T]
        """
        super().__init__(space_mapping_function_stream=space_mapping_function_stream)
        
        map_stream = cast(AxisMappingFunctionStream, space_mapping_function_stream)
        self._space_mapping_function_stream = space_mapping_function_stream
        
        east_axis = map_stream.space_reservoir.east
        north_axis = map_stream.space_reservoir.north
        south_axis = map_stream.space_reservoir.south
        west_axis = map_stream.space_reservoir.west
        
        east_tuple = map_stream.east_axis_map_tuple
        north_tuple = map_stream.north_axis_map_tuple
        west_tuple = map_stream.west_axis_map_tuple
        south_tuple = map_stream.south_axis_map_tuple
        
        
        self._recurrence_table{
            "east": EastAxisRecurrence(
                space=east_tuple[0],
                space_mapping_function=east_tuple[1]
            )
            
        }
    
    @property
    def space_mapping_function_stream(self) -> AxisMappingFunctionStream[T]:
        return cast(
            AxisMappingFunctionStream[T],
            self._space_mapping_function_stream
        )
    
    @property
    @abstractmethod
    def table_size(self) -> int:
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_not_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def iterator(self) -> iter:
        pass

