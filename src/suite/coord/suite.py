# src/suite/bootstrapper/toolkit.py

"""
Module: suite.bootstrapper.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from builder import CoordBuilder
from model import Coord
from toolkit import ModelOperationSuite, CoordToolkit
from validation import CoordValidator


class CoordOperationSuite(ModelOperationSuite[Coord]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Coord.

    Attributes:
        toolkit: CoordToolkit
        builder: CoordBuilder
        validator: CoordValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: CoordToolkit = CoordToolkit()
    builder: CoordBuilder = CoordBuilder()
    validator: CoordValidator = CoordValidator()

