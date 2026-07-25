# src/recurrence/table/axis/space.py

"""
Module: recurrence.table.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, cast

from mapper import AxisMappingFunctionStream
from recurrence import (
    AxisRecurrence, EastAxisRecurrence, NorthAxisRecurrence, SouthAxisRecurrence,
    SpaceRecurrenceTable, WestAxisRecurrence
)
from space import Axis


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
    _recurrence_table: Dict[str, AxisRecurrence]
    
    def __init__(
            self,
            space_mapping_function_stream: AxisMappingFunctionStream
    ):
        """
        Args:
            space_mapping_function_stream: AxisMappingFunctionStream[T]
        """
        super().__init__(space_mapping_function_stream=space_mapping_function_stream)
        self._space_mapping_function_stream = space_mapping_function_stream
        
        # Make an independent copy for filing the recurrence table.
        map_stream = cast(AxisMappingFunctionStream, space_mapping_function_stream)
        
        # Add the eastern recurrence entry.
        space, space_mapping_function = map_stream.east_axis_map_tuple
        self._recurrence_table["east"] = EastAxisRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the northern recurrence entry.
        space, space_mapping_function = map_stream.north_axis_map_tuple
        self._recurrence_table["north"] = NorthAxisRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the southern recurrence entry.
        space, space_mapping_function = map_stream.south_axis_map_tuple
        self._recurrence_table["south"] = SouthAxisRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
        # Add the western recurrence entry.
        space, space_mapping_function = map_stream.west_axis_map_tuple
        self._recurrence_table["north"] = WestAxisRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
    
    @property
    def space_mapping_function_stream(self) -> AxisMappingFunctionStream[T]:
        return cast(
            AxisMappingFunctionStream[T],
            self._space_mapping_function_stream
        )
    
    @property
    def number_of_recurrences(self) -> int:
        return len(self._recurrence_table)
    
    @property
    def are_no_recurrences(self) -> bool:
        return self.number_of_recurrences == 0
    
    @property
    def recurrences_exist(self) -> bool:
        return not self.are_no_recurrences
    
    @property
    def iterator(self) -> iter:
        recurrences: List[AxisRecurrence] = []
        
        for key in self._recurrence_table.keys():
            recurrences.append(self._recurrence_table[key])
        return recurrences.__iter__()
    
    @property
    def east_axis_recurrence(self) -> EastAxisRecurrence:
        return cast(
            EastAxisRecurrence,
            self._recurrence_table["east"]
        )
    
    @property
    def north_axis_recurrence(self) -> NorthAxisRecurrence:
        return cast(
            NorthAxisRecurrence,
            self._recurrence_table["north"]
        )
    
    @property
    def south_axis_recurrence(self) -> SouthAxisRecurrence:
        return cast(
            SouthAxisRecurrence,
            self._recurrence_table["south"]
        )
    
    @property
    def west_axis_recurrence(self) -> WestAxisRecurrence:
        return cast(
            WestAxisRecurrence,
            self._recurrence_table["west"]
        )

