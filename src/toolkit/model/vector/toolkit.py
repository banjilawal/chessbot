# src/toolkit/model/vector/toolkit.py

"""
Module: toolkit.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from err import VectorNullException
from model import Vector
from toolkit import ModelToolkit
from validation import NumberValidator


@dataclass
class VectorToolkit(ModelToolkit):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Vector tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        number_validator: NumberValidator
        null_exception: VectorNullException
        model: Vector = Vector

    Provides:

    Super Class:
       ModelToolkit
    """
    number_validator: NumberValidator = NumberValidator()
    null_exception: VectorNullException = VectorNullException()
    model: Vector = Type[Vector]


    