# src/toolkit/model/either/toolkit.py

"""
Module: toolkit.model.either.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import CartesianPointBlueprint
from err import CartesianPointNullException
from chooser import CartesianPoint

from suite import  CoordOperationSuite, VectorOperationSuite
from toolkit import Toolkit


@dataclass
@dataclass
class CartesianPointToolkit(Toolkit[CartesianPoint]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianEither tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        coord: CoordOperationSuite
        cartesian: CartesianOperationSuite
        null_exception: CartesianEitherNullException
        model: CartesianEither

    Provides:

    Super Class:
        Toolkit
    """
    model: Type[CartesianPoint] = CartesianPoint
    blueprint_model: CartesianPointBlueprint = CartesianPointBlueprint
    
    null_exception: CartesianPointNullException = CartesianPointNullException()
    blueprint_null_exception: CartesianBlueprintNullException = CartesianBlueprintNullException()
    
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()

