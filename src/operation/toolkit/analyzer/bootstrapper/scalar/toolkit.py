# src/operation/toolkit/analyzer/scalar/toolkit.py

"""
Module: operation.toolkit.analyzer.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from sensor.analyzer import Scalar
from operation.toolkit.analyzer.bootstrapper.scalar.toolkit import AnalyzerBootstrapperToolkit
from assurance.validator import NumberValidator


@dataclass
class ScalarToolkit(AnalyzerBootstrapperToolkit[Scalar]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Scalar tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
            number_validator: NumberValidator
    Provides:

     Super Class:
         Toolkit
     """
    number_validator = NumberValidator()
