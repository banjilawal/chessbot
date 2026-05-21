# src/suite/math/suite.py

"""
Module: suite.math.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operation import AddVector, EuclideanDistance, ScalarProduct, VectorTransform
from toolkit import MathToolkit


@dataclass
class MathSuite:
    math_toolkit: MathToolkit = MathToolkit()
    add_vector: AddVector = AddVector()
    scalar_product: ScalarProduct = ScalarProduct()
    vector_transform: VectorTransform = VectorTransform()
    euclidean_distance: EuclideanDistance = EuclideanDistance()