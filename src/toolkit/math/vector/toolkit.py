# src/toolkit/math/vector.toolit.py

"""
Module: toolkit.math.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from toolkit import CoordOperationSuite, ScalarOperationSuite, Toolkit, VectorOperationSuite
from validation import NumberValidator


@dataclass
class VectorAlgebraToolkit(Toolkit):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of suites and operations for vector algebra.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        coord: CoordOperationSuite
        scalar: ScalarOperationSuite
        vector: VectorOperationSuite
        number_validator: NumberValidator
    Provides:

     Super Class:
         Toolkit
     """
    coord: CoordOperationSuite = CoordOperationSuite()
    scalar: ScalarOperationSuite = ScalarOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()
    number_validator: NumberValidator = NumberValidator()

