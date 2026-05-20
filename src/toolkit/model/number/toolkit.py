# src/toolkit/model/number/toolkit.py

"""
Module: toolkit.model.number.toolkit
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from toolkit import Toolkit
from validation import NumberValidator

@dataclass
class NumberToolkit(Toolkit[int]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
            number_validator: NumberValidator
    Provides:

     Super Class:
         Toolkit
     """
    number_validator: NumberValidator = NumberValidator()
