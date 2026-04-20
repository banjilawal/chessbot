# src/model/context/vector/model.py

"""
Module: model.context.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from toolkit import Toolkit
from integrity import NumberValidator
from operation import ValidationBootstrapper



class MathToolkit(Toolkit):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
            number_validator: NumberValidator
            validation_bootstrap: ValidationBootstrapper
    Provides:

     Super Class:
         Toolkit
     """
    _number_validator: NumberValidator
    _validation_bootstrapper: ValidationBootstrapper
    
    def __init__(
            self,
            number_validator: NumberValidator | None = None,
            validation_bootstrap: ValidationBootstrapper | None = None,
    ):
        """
        Args:
            number_validator: NumberValidator
            validation_bootstrap: ValidationBootstrapper
        """
        super().__init__()
        self._number_validator = number_validator or NumberValidator()
        self._validation_bootstrapper = validation_bootstrap or ValidationBootstrapper()

    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    
    @property
    def validation_bootstrap(self) -> ValidationBootstrapper:
        return self._validation_bootstrapper
