# src/toolkit/model/scalar/toolkit.py

"""
Module: toolkit.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import ScalarNullException
from model import Scalar
from toolkit import ModelToolkit
from validator import NumberValidator


@dataclass
class ScalarToolkit(ModelToolkit):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Scalar tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        number_validator: NumberValidator
        null_exception: ScalarNullException
        model: Scalar = Scalar

    Provides:

    Super Class:
       ModelToolkit
    """
    number_validator: NumberValidator = NumberValidator()
    null_exception: ScalarNullException = ScalarNullException()
    model: Scalar = Scalar


    