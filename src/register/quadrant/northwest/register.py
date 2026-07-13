# src/register/quadrant/northwest/register.py

"""
Module: register.quadrant.northwest.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector

from register.quadrant import Quadrant


class NorthwestQuadrant(Quadrant):
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Defines the delta_x/delta_y and bounds of a quadrant relative to a
            token's position.

    Attributes:
        x_step: int
        slope: int
        terminal_vector: Vector

    Provides:

    Super Class:
        Quadrant
    """
    
    def __init__(
            self,
            x_step: int = -1,
            slope: int = -1,
            terminal_vector = Vector(x=0, y=0)
    ):
        """
        Args:
            x_step: int
            slope: int
            terminal_vector: Vector
        """
        super().__init__(
            x_step=x_step,
            slope=slope,
            terminal_vector=terminal_vector
        )
        
    