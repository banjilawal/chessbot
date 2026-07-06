# src/suite/bootstrapper/toolkit.py

"""
Module: suite.bootstrapper.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from builder import ScalarBuilder
from model import Scalar
from toolkit import ModelOperationSuite, ScalarToolkit
from validation import ScalarValidator


class ScalarOperationSuite(ModelOperationSuite[Scalar]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Scalar.

    Attributes:
        toolkit: ScalarToolkit
        builder: ScalarBuilder
        validator: ScalarValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: ScalarToolkit = ScalarToolkit()
    builder: ScalarBuilder = ScalarBuilder()
    validator: ScalarValidator = ScalarValidator()

