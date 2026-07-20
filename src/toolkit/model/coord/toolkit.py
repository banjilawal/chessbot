# src/toolkit/model/coord/toolkit.py

"""
Module: toolkit.model.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import CoordBlueprint
from toggle.carrier import CoordCarrier
from err import CoordBlueprintNullException, CoordCarrierNullException, CoordNullException
from model import Coord
from toolkit import ModelToolkit
from validator import NumberValidator


@dataclass
class CoordToolkit(ModelToolkit[Coord]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Coord tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model: Type[Coord]
        carrier_model: Type[CoordCarrier]
        blueprint_model: Type[CoordBlueprint]
        
        null_exception: CoordNullException
        carrier_null_exception: CoordCarrierNullException
        blueprint_null_exception: CoordBlueprintNullException
    
        number_validator: NumberValidator

    Provides:

    Super Class:
       ModelToolkit
    """
    model: Type[Coord] = Coord
    carrier_model: Type[CoordCarrier] = CoordCarrier
    blueprint_model: Type[CoordBlueprint] = CoordBlueprint
    
    null_exception: CoordNullException = CoordNullException()
    carrier_null_exception: CoordCarrierNullException = CoordCarrierNullException()
    blueprint_null_exception: CoordBlueprintNullException = CoordBlueprintNullException()

    number_validator: NumberValidator = NumberValidator()

    