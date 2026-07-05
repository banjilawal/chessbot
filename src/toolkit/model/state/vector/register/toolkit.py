# src/toolkit/model/vector/register/toolkit.py

"""
Module: toolkit.model.vector.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import VectorOperandRegister
from toolkit import ModelToolkit
from validation import PrimingValidator, VectorOperandValidator

@dataclass
class VectorRegisterToolkit(ModelToolkit[VectorOperandRegister]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Coord requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        vector_operand_validator: VectorOperandValidator
        priming_validator: ValidationPrimer

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:
        
    Super Class:
        Toolkit
    """
    vector_operand_validator: VectorOperandValidator = VectorOperandValidator()
    priming_validator: PrimingValidator = PrimingValidator()
