# src/toolkit/context/toolkit/__init__.py

"""
Module: toolkit.context.toolkit.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from bootstrapper import PrimingContextValidator
from context import Context
from err import ContextNullException
from toolkit import Toolkit


T = TypeVar("T")

@dataclass
class ContextToolkit(Toolkit, Generic[T]):
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
        
        context_model: Context
        null_exception: ContextNullException
        priming_validator: PrimingContextValidator
        
    Provides:
    
    Super Class:
        Toolkit
    """
    context_model: Context[T]
    context_null_exception: ContextNullException
    model_toolkit: Optional[Toolkit[T]] | None = None
    context_priming_validator: PrimingContextValidator = PrimingContextValidator()
