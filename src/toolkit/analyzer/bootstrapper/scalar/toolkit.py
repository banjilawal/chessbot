# src/toolkit/analyzer/scalar/toolkit.py

"""
Module: toolkit.analyzer.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from analyzer import Scalar
from toolkit import AnalyzerBootstrapperToolkit
from validation import NumberValidator


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
