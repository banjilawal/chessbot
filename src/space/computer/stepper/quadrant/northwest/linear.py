# src/space/linear/stepper/quadrant/space.py

"""
Module: space.linear.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import QuadrantStepperException
from model import Vector
from register import NumberRegister
from result import ComputationResult, MethodResultType
from schema.stepper.schema import QuadrantStepFunction
from space import LinearStepper, Quadrant
from util import LoggingLevelRouter


class NorthwestQuadrantStepper(QuadrantStepper):
    """
    Role:
        -   Computation Worker
        
    Background:
    1.  Consider the diagonal series: p_1(0,0), p_2(1,1), p_3(2,2), ., p_n(n,n). For any
            p_i, y_i = x_i.
        We want to find some invariant only in terms of x that will gives us all the ys.
    2.  Let us consider x in non-negative integers, {0, 1, 2,3,.,n}
        we now that
            x_i <= x_j < x_n.
    3.  The start of the X sequence is
            X_0 = 0,
            X_1 = 1,
            x_2 = 2
            x_3 = 3
       Which reveals: x_j = x_i + (j-i) But we want to express only in terms of x and restrict that i < j
            when i = 0, xo = x
            x_i = x_(i-1) + 1
    5. Since x_i = y_i, we can express the series in terms of x_(i-i)
            y_i = (x_(i-1) + delta_x) + x_(i-1)
            y_i = 2x_(i-1)
    6. In the quadrant(x<0, y>0) delta_x = -1.
    7. For thr quadrant (x<0, y>0) delta_x = 1.
    8. So for each quadrant we change the slope.
    
    Gives us
        abs(x_step) = 1,
        f = x + c where c is the step.
        g = 2bx + b where b is the slope.
        so
        v = ((u.x + c), ((2b)u.x + b)

    Responsibilities:
        1.  Produce y from the  range of x in a seres projected from the quadrant's origin.

    Attributes:
        ENTRY: Dict[str, NumberRegister]
        
        x_step: int
        slope: int

    Provides:
        -   def next(current: Vector) -> ComputationResult[Vector]
        -   def northeast() -> QuadrantStepper
        -   def northwest() -> QuadrantStepper
        -   def southwest() -> QuadrantStepper
        -   def southeast() -> QuadrantStepper

    Super Class:
        Stepper

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """
    """
    QuadrantStepper for going northeast toward top right corner (num_rows - 1, 0)
        -   x_step = 1,
        -   slope = 1
    """
    
    def __init__(
            self,
            x_step: int = QuadrantStepFunction.NORTHWEST.x_step,
            slope: int = QuadrantStepFunction.NORTHWEST.slope,
    ):
        super().__init__(x_step=x_step, slope=slope)
