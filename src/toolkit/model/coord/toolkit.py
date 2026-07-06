# src/toolkit/model/coord/toolkit.py

"""
Module: toolkit.model.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import CoordNullException
from model import Coord
from toolkit import ModelToolkit
from validator import NumberValidator


@dataclass
class CoordToolkit(ModelToolkit):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Coord tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        number_validator: NumberValidator
        null_exception: CoordNullException
        model: Coord = Coord

    Provides:

    Super Class:
       ModelToolkit
    """
    number_validator: NumberValidator = NumberValidator()
    null_exception: CoordNullException = CoordNullException()
    model: Coord = Coord


    