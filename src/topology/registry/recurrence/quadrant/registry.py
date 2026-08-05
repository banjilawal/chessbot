# src/recurrence/topology/registry/quadrant/registry.py

"""
Module: topology.registry.recurrence.quadrant.registry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Type, cast

from topology import (
    NortheastQuadrantRecurrence, NorthwestQuadrantRecurrence, Quadrant, QuadrantMappingFunctionStream,
    QuadrantRecurrence,
    RecurrenceRegistry, SoutheastQuadrantRecurrence, SouthwestQuadrantRecurrence
)
from model import Vector


class QuadrantRecurrenceRegistry(RecurrenceRegistry[Quadrant]):
    """
    Role:
        -   Data Holder
        -   Factory
        -   Switcher

    Responsibilities:
        1.  Create an immuregistry set of recurrence relations for batch vector transformations across all axes.

    Attributes:
        recurrences_exist: bool
        no_recurrences_exist: bool
        number_of_recurrences: int

        northeast_quadrant_recurrence: NorthEastQuadrantRecurrence
        northwest_quadrant_recurrence: NorthwestQuadrantRecurrence
        southeast_quadrant_recurrence: SoutheastQuadrantRecurrence
        southwest_quadrant_recurrence: SouthwestQuadrantRecurrence

        type_recurrence_dict: Dict[Type[Quadrant], QuadrantRecurrence]
        space_mapping_function_stream: QuadrantMappingFunctionStream

    Provides:

    Super Class:
        RecurrenceRegistry
    """
    _space_mapping_function_stream: QuadrantMappingFunctionStream
    _recurrence_registry: Dict[str, QuadrantRecurrence]
    
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
        
        # Make an independent copy for filing the recurrence registry.
        map_stream = cast(QuadrantMappingFunctionStream, space_mapping_function_stream)
        
        # Add the northeastern recurrence entry.
        space, space_mapping_function = map_stream.northeast_quadrant_map_tuple
        self._recurrence_registry["northeast"] = NortheastQuadrantRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the northwestern recurrence entry.
        space, space_mapping_function = map_stream.northwest_quadrant_map_tuple
        self._recurrence_registry["northwest"] = NorthwestQuadrantRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the southeastern recurrence entry.
        space, space_mapping_function = map_stream.southeast_quadrant_map_tuple
        self._recurrence_registry["southeast"] = SoutheastQuadrantRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
        # Add the southwestern recurrence entry.
        space, space_mapping_function = map_stream.southwest_quadrant_map_tuple
        self._recurrence_registry["north"] = SouthwestQuadrantRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
    
    @property
    def origin(self) -> Vector:
        return self.northeaset_quadrant_recurrence.space.origin
    
    @property
    def space_mapping_function_stream(self) -> QuadrantMappingFunctionStream:
        return cast(
            QuadrantMappingFunctionStream,
            self._space_mapping_function_stream
        )
    
    @property
    def number_of_recurrences(self) -> int:
        return len(self._recurrence_registry)
    
    @property
    def no_recurrences_exist(self) -> bool:
        return self.number_of_recurrences == 0
    
    @property
    def recurrences_exist(self) -> bool:
        return not self.no_recurrences_exist
    
    @property
    def northeast_quadrant_recurrence(self) -> NortheastQuadrantRecurrence:
        return cast(
            NortheastQuadrantRecurrence,
            self._recurrence_registry["northeast"]
        )
    
    @property
    def northwest_quadrant_recurrence(self) -> NorthwestQuadrantRecurrence:
        return cast(
            NorthwestQuadrantRecurrence,
            self._recurrence_registry["northwest"]
        )
    
    @property
    def southeast_quadrant_recurrence(self) -> SoutheastQuadrantRecurrence:
        return cast(
            SoutheastQuadrantRecurrence,
            self._recurrence_registry["southeast"]
        )
    
    @property
    def southwest_quadrant_recurrence(self) -> SouthwestQuadrantRecurrence:
        return cast(
            SouthwestQuadrantRecurrence,
            self._recurrence_registry["southwest"]
        )
    
    @property
    def type_recurrence_dict(self) -> Dict[Type[QuadrantRecurrence], QuadrantRecurrence]:
        """
        Simple iteration through the quadrant mapping functions is not useful because the need down-casting
        Using type as the iterator key surmount can automate casting without requiring isinstance calls.
        """
        return {
            Type[NortheastQuadrantRecurrence]: self.northeast_quadrant_recurrence,
            Type[NorthwestQuadrantRecurrence]: self.northwest_quadrant_recurrence,
            Type[SouthwestQuadrantRecurrence]: self.southwest_quadrant_recurrence,
            Type[SoutheastQuadrantRecurrence]: self.southeast_quadrant_recurrence,
        }
