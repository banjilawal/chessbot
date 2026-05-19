# src/toolkit/context/toolkit/__init__.py

"""
Module: toolkit.context.toolkit.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import ContextNullException
from model import Context
from toolkit import Toolkit
from validation import ContextValidatorBootstrapper


@dataclass
class ContextToolkit(Toolkit[Context]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Aggregates workers and services required for Context build and validation tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.


    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
        context_model_type: Context
        null_context_exception: ContextNullException
        context_validation_primer: ValidationPrimer
        
    Provides:
    
    Super Class:
        Toolkit
    """
    context_model_type: Context = Context
    null_context_exception: ContextNullException = ContextNullException()
    context_validation_primer: ContextValidatorBootstrapper = ContextValidatorBootstrapper()
