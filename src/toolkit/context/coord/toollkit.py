# src/toolkit/context/coord/toolkit.py

"""
Module: toolkit.context.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import CoordContextNullException
from model import Coord, CoordContext
from toolkit import ContextToolkit, CoordToolkit
from validation import NumberValidator


class CoordContextToolkit(ContextToolkit[Coord]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Aggregates workers and services required for CoordContext build and validation tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: CoordContext
        null_context_exception: CoordContextNullException
        context_validation_primer: ValidationPrimer
        number_validator: NumberValidator
        
    Provides:
    
    Super Class:
        ContextToolkit
    """
    context_model_type = CoordContext
    coord_toolkit: CoordToolkit = CoordToolkit()
    null_context_exception =  CoordContextNullException()