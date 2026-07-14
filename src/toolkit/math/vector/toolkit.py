# src/toolkit/math/vector.toolit.py

"""
Module: toolkit.math.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from operation import AddVector, EuclideanDistance, ScalarProduct, VectorTransform
from suite import CoordOperationSuite, ScalarOperationSuite, VectorOperationSuite
from toolkit import Toolkit
from validator import NumberValidator


@dataclass
class MathToolkit(Toolkit):
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
         
    Notes:
        -   VectorAlgebraToolkit does not extend ModelOperationSuite because an OperationSuite needs a Type.
     """
    coord: CoordOperationSuite = CoordOperationSuite()
    scalar: ScalarOperationSuite = ScalarOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()
    number_validator: NumberValidator = NumberValidator()
    add_vector: AddVector = AddVector()
    scalar_product: ScalarProduct = ScalarProduct()
    transform: VectorTransform = VectorTransform()
    euclidean_distance: EuclideanDistance = EuclideanDistance()

