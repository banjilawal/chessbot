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
from validator import NumberValidator


class SquareContextToolkit(ContextToolkit[Square]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Aggregates workers and services required for SquareContext build and validation tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.


    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: SquareContext
        null_context_exception: SquareContextNullException
        context_priming_validator: PrimingValidator
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = SquareContext
    square_toolkit: SquareToolkit = SquareToolkit()
    null_context_exception =  SquareContextNullException()