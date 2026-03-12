# src/logic/span/coord/ray/diagonal/provider/factor.py

"""
Module: logic.span.coord.ray.diagonal.provider.factor
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict


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
            end_x: int
            x_step: int
            end_y: int
            slope: int
            
    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
            start_x: int
            end_x: int
            x_step: int
            end_y: int
            slope: int

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _start_x: int
    _end_x: int
    _x_step: int
    _end_y: int
    _slope: int
    
    def __init__(self, start_x: int, end_x: int, x_step: int, end_y: int, slope: int):
        """
        Args:
            start_x: int
            end_x: int
            x_step: int
            end_y: int
            slope: int
        """
        self._start_x = start_x
        self._end_x = end_x
        self._x_step = x_step
        self._end_y = end_y
        self._slope = slope
        
    @property
    def start_x(self) -> int:
        return self._start_x
    
    @property
    def end_x(self) -> int:
        return self._end_x
    
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def end_y(self) -> int:
        return self._end_y
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def hash(self) -> Dict[str, int]:
        """
        Puts factors in a dictionary.
        """
        return {
            "start_x": self.start_x,
            "end_x": self._end_x,
            "x_step": self._x_step,
            "end_y": self._end_y,
            "slope": self._slope,
        }