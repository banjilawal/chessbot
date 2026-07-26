# src/recurrence/table/quadrant/space.py

"""
Module: recurrence.table.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, Type, cast

from mapper import QuadrantMappingFunctionStream
from recurrence import (
    NorthwestQuadrantRecurrence, QuadrantRecurrence, NortheastQuadrantRecurrence,
    SoutheastQuadrantRecurrence, RecurrenceTable, SouthwestQuadrantRecurrence
)
from space import Quadrant


class QuadrantRecurrenceTable(RecurrenceTable[Quadrant]):
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
    _space_mapping_function_stream: QuadrantMappingFunctionStream
    _recurrence_table: Dict[str, QuadrantRecurrence]
    
    def __init__(
            self,
            space_mapping_function_stream: QuadrantMappingFunctionStream
    ):
        """
        Args:
            space_mapping_function_stream: QuadrantMappingFunctionStream[T]
        """
        super().__init__(space_mapping_function_stream=space_mapping_function_stream)
        self._space_mapping_function_stream = space_mapping_function_stream
        
        # Make an independent copy for filing the recurrence table.
        map_stream = cast(QuadrantMappingFunctionStream, space_mapping_function_stream)
        
        # Add the northeastern recurrence entry.
        space, space_mapping_function = map_stream.northeast_quadrant_map_tuple
        self._recurrence_table["northeast"] = NortheastQuadrantRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the northern recurrence entry.
        space, space_mapping_function = map_stream.northwest_quadrant_map_tuple
        self._recurrence_table["northwest"] = NorthwestQuadrantRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the southern recurrence entry.
        space, space_mapping_function = map_stream.southeast_quadrant_map_tuple
        self._recurrence_table["southeast"] = SoutheastQuadrantRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
        # Add the southwestern recurrence entry.
        space, space_mapping_function = map_stream.southwest_quadrant_map_tuple
        self._recurrence_table["north"] = SouthwestQuadrantRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
    
    @property
    def space_mapping_function_stream(self) -> QuadrantMappingFunctionStream:
        return cast(
            QuadrantMappingFunctionStream,
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
        recurrences: List[QuadrantRecurrence] = []
        
        for key in self._recurrence_table.keys():
            recurrences.append(self._recurrence_table[key])
        return recurrences.__iter__()
    
    @property
    def northeast_quadrant_recurrence(self) -> NortheastQuadrantRecurrence:
        return cast(
            NortheastQuadrantRecurrence,
            self._recurrence_table["northeast"]
        )
    
    @property
    def northwest_quadrant_recurrence(self) -> NorthwestQuadrantRecurrence:
        return cast(
            NorthwestQuadrantRecurrence,
            self._recurrence_table["northwest"]
        )
    
    @property
    def southeast_quadrant_recurrence(self) -> SoutheastQuadrantRecurrence:
        return cast(
            SoutheastQuadrantRecurrence,
            self._recurrence_table["southeast"]
        )
    
    @property
    def southwest_quadrant_recurrence(self) -> SouthwestQuadrantRecurrence:
        return cast(
            SouthwestQuadrantRecurrence,
            self._recurrence_table["southwest"]
        )
    
    @property
    def type_recurrence_dict(self) -> Dict[Type[QuadrantRecurrence], QuadrantRecurrence]:
        return {
            Type[NortheastQuadrantRecurrence]: self.northeast_quadrant_recurrence,
            Type[NorthwestQuadrantRecurrence]: self.northwest_quadrant_recurrence,
            Type[SouthwestQuadrantRecurrence]: self.southwest_quadrant_recurrence,
            Type[SoutheastQuadrantRecurrence]: self.southeast_quadrant_recurrence,
            
        }
