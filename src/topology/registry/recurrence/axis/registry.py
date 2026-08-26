# src/recurrence/topology/registry/axis/registry.py

"""
Module: topology.registry.recurrence.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Type, cast

from topology import (
    Axis, AxisMappingFunctionStream, AxisRecurrence, EastAxisRecurrence, NorthAxisRecurrence,
    RecurrenceRegistry, SouthAxisRecurrence, WestAxisRecurrence
)
from domain.model import Vector


class AxisRecurrenceRegistry(RecurrenceRegistry[Axis]):
    """
    Role:
        -  Data Holder
        -  Factory
        -  Switcher

    Responsibilities:
        1.  Create an immuregistry set of recurrence relations for batch vector transformations across all axes.

    Attributes:
        recurrences_exist: bool
        no_recurrences_exist: bool
        number_of_recurrences: int
        
        east_axis_recurrence: EastAxisRecurrence
        north_axis_recurrence: NorthAxisRecurrence
        south_axis_recurrence: SouthAxisRecurrence
        west_axis_recurrence: WestAxisRecurrence
        
        type_recurrence_dict: Dict[Type[Axis], AxisRecurrence]
        space_mapping_function_stream: AxisMappingFunctionStream

    Provides:

    Super Class:
        RecurrenceRegistry
    """
    _space_mapping_function_stream: AxisMappingFunctionStream
    _registry: Dict[str, AxisRecurrence]
    
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
        
        # Make an independent copy for filing the recurrence registry.
        map_stream = cast(AxisMappingFunctionStream, space_mapping_function_stream)
        
        # Add the eastern recurrence entry.
        space, space_mapping_function = map_stream.east_axis_map_tuple
        self._registry["east"] = EastAxisRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the northern recurrence entry.
        space, space_mapping_function = map_stream.north_axis_map_tuple
        self._registry["north"] = NorthAxisRecurrence(
                space=space,
                space_mapping_function=space_mapping_function
        )
        # Add the southern recurrence entry.
        space, space_mapping_function = map_stream.south_axis_map_tuple
        self._registry["south"] = SouthAxisRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
        # Add the western recurrence entry.
        space, space_mapping_function = map_stream.west_axis_map_tuple
        self._registry["north"] = WestAxisRecurrence(
            space=space,
            space_mapping_function=space_mapping_function
        )
        
    @property
    def origin(self) -> Vector:
        return self.north_axis_recurrence.space.origin
    
    @property
    def space_mapping_function_stream(self) -> AxisMappingFunctionStream:
        return cast(
            AxisMappingFunctionStream,
            self._space_mapping_function_stream
        )
    
    @property
    def number_of_recurrences(self) -> int:
        return len(self._registry)
    
    @property
    def no_recurrences_exist(self) -> bool:
        return self.number_of_recurrences == 0
    
    @property
    def recurrences_exist(self) -> bool:
        return not self.no_recurrences_exist
    
    @property
    def east_axis_recurrence(self) -> EastAxisRecurrence:
        return cast(
            EastAxisRecurrence,
            self._registry["east"]
        )
    
    @property
    def north_axis_recurrence(self) -> NorthAxisRecurrence:
        return cast(
            NorthAxisRecurrence,
            self._registry["north"]
        )
    
    @property
    def south_axis_recurrence(self) -> SouthAxisRecurrence:
        return cast(
            SouthAxisRecurrence,
            self._registry["south"]
        )
    
    @property
    def west_axis_recurrence(self) -> WestAxisRecurrence:
        return cast(
            WestAxisRecurrence,
            self._registry["west"]
        )
    
    @property
    def type_recurrence_dict(self) -> Dict[Type[Axis], AxisRecurrence]:
        """
        Simple iteration through the quadrant mapping functions is not useful because the need down-casting
        Using type as the iterator key surmount can automate casting without requiring isinstance calls.
        """
        return {
            Type[EastAxisRecurrence]: self.east_axis_recurrence,
            Type[NorthAxisRecurrence]: self.north_axis_recurrence,
            Type[WestAxisRecurrence]: self.west_axis_recurrence,
            Type[SouthAxisRecurrence]: self.south_axis_recurrence,
        }

