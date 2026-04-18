# src/toolkit/vector/toolkit.py

"""
Module: toolkit.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import NumberValidator
from model import Vector
from operation import ValidationBootstrapper
from toolkit import Toolkit


class VectorToolkit(Toolkit[Vector]):
    """
    Role:
        -   Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        number_validator: NumberValidator
        validation_bootstrapper: ValidationBootstrapper
        
    Provides:

     Super Class:
         Toolkit
     """
    _number_validator: NumberValidator
    _validation_bootstrapper: ValidationBootstrapper
    
    def __init__(
            self,
            number_validator: NumberValidator | None = None,
            validation_bootstrapper: ValidationBootstrapper | None = None,
    ):
        """
        Args:
            number_validator: NumberValidator
            validation_bootstrapper: ValidationBootstrapper
        """
        super().__init__()
        self._number_validator = number_validator or NumberValidator()
        self._validation_bootstrapper = validation_bootstrapper or ValidationBootstrapper()

    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    
    @property
    def validation_bootstrapper(self) -> ValidationBootstrapper:
        return self._validation_bootstrapper