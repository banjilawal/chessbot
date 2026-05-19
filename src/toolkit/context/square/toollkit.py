# src/toolkit/context/square/toolkit.py

"""
Module: toolkit.context.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import SquareContextNullException
from model import Square, SquareContext
from toolkit import ContextToolkit, SquareToolkit
from validation import NumberValidator


class SquareContextToolkit(ContextToolkit[Square]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Collection of workers and services that are required for Square tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: SquareContext
        null_context_exception: SquareContextNullException
        context_validation_primer: ValidationBootstrapper
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = SquareContext
    square_toolkit: SquareToolkit = SquareToolkit()
    null_context_exception =  SquareContextNullException()
    number_validator: NumberValidator = NumberValidator()