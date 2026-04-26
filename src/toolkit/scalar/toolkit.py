# src/toolkit/scalar/toolkit.py

"""
Module: toolkit.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Scalar
from toolkit import Toolkit
from operation import NumberValidator

class ScalarToolkit(Toolkit[Scalar]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Scalar tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
            number_validator: NumberValidator
    Provides:

     Super Class:
         Toolkit
     """
    
    def __init__(
            self,
            number_validator: NumberValidator | None = None,
    ):
        """
        Args:
            number_validator: NumberValidator
        """
        super().__init__()
        self._number_validator = number_validator or NumberValidator()

    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
