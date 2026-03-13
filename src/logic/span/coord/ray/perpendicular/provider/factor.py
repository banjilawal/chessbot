# src/logic/span/coord/ray/perpendicular/provider/factor.py

"""
Module: logic.span.coord.ray.perpendicular.provider.factor
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.vector import Vector


class PerpendicularRayFactors:
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
            start_y: int
            end_y: int
            y_step: int

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
            start_x: int
            end_x: int
            x_step: int
            start_y: int
            end_y: int
            y_step: int

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _start_vector: Vector
    _end_vector: Vector
    _delta: Vector
    
    def __init__(
            self,
            start_vector: Vector,
            end_vector: Vector,
            delta: Vector,
    ):
        """
        Args:
            start_vector: Vector
            end_vector: Vector
            delta: Vector
        """
        self._start_vector = start_vector
        self._end_vector = end_vector
        self._delta = delta
        
    @property
    def start_vector(self) -> Vector:
        return self._start_vector
    
    @property
    def end_vector(self) -> Vector:
        return self._end_vector
    
    @property
    def delta(self) -> Vector:
        return self._delta
    
    @property
    def hash(self) -> Dict[str, Vector]:
        """
        Puts factors in a dictionary.
        """
        return {
            "start_vector": self._start_vector,
            "end_vector": self._end_vector,
            "delta": self._delta,

        }
