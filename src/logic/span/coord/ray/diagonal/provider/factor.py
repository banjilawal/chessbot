# src/logic/span/coord/ray/diagonal/provider/factor.py

"""
Module: logic.span.coord.ray.diagonal.provider.factor
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.vector import Vector


class DiagonalRayFactors:
    """
    # ROLE: Data-HOlder
    # TASK: Computation arguments.

    # RESPONSIBILITIES:
    1.  Provide arguments for
            *   priming the ray projection's codomain from the origin
            *   The invariant.
            *   The additive factor for advancing the series.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
            start_x: int
            x_step: int
            slope: int
            end_vector: Vector
            
    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
            start_x: int
            x_step: int
            slope: int
            end_vector: Vector

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _start_x: int
    _x_step: int
    _slope: int
    _end_vector: Vector
    
    def __init__(self, start_x: int,x_step: int, slope: int, end_vector: Vector):
        """
        Args:
            start_x: int
            x_step: int
            slope: int
            end_vector: Vector
        """
        self._start_x = start_x
        self._slope = slope
        self._x_step = x_step
        self._end_vector = end_vector

        
    @property
    def start_x(self) -> int:
        return self._start_x
    
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def end_vector(self) -> Vector:
        return self._end_vector
    
    @property
    def hash(self) -> Dict[str, Any]:
        """
        Puts factors in a dictionary.
        """
        return {
            "start_x": self.start_x,
            "x_step": self._x_step,
            "slope": self._slope,
            "end_vector": self._end_vector
        }