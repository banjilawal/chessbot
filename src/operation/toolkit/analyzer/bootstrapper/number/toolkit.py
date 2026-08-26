# src/operation/toolkit/analyzer/number/toolkit.py

"""
Module: operation.toolkit.analyzer.number.toolkit
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from dataclasses import dataclass

from operation.toolkit.analyzer.bootstrapper.number.toolkit import AnalyzerBootstrapperToolkit
from transit.dispatcher.validator import NumberValidator

@dataclass
class NumberToolkit(AnalyzerBootstrapperToolkit[int]):
    """
    Role:
        -  Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorToggle tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
            number_validator: NumberValidator
    Provides:

     Super Class:
         Toolkit
     """
    number_validator: NumberValidator = NumberValidator()
