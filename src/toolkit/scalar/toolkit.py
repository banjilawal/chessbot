# src/toolkit/scalar/toolkit.py

"""
Module: toolkit.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from integrity import NumberValidator
from system import Toolkit, ToolkitResult, LoggingLevelRouter
from toolkit.scalar import Scalar, ScalarToolkitException, ScalarValidator


class ScalarToolkit(Toolkit[Scalar]):
    """
    Role:
        -   Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
    
    Provides:
    
    Super Class:
         Toolkit
    """
    _number_validator: NumberValidator
    
    def __init__(self, number_validator: NumberValidator | None = None,):
        """
        Args:
            number_validator: NumberValidator
        """
        self._number_validator = number_validator or NumberValidator()
        
    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
