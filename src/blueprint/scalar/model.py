# src/blueprint/scalar/model.py

"""
Module: blueprint.scalar.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from err import ScalarNullException
from model import Blueprint, Scalar

@dataclass
class ScalarBlueprint(Blueprint[Scalar]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides magnitude value for instantiating a Scalar object.

    Attributes:
        magnitude: int
        model_type: Scalar
        null_exception: ScalarNullException
    Provides:

     Super Class:
        Blueprint
     """
    magnitude: int
    model_type: Scalar = Scalar
    null_exception: ScalarNullException = ScalarNullException()
