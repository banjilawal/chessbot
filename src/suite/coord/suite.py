# src/suite/coord/suite.py

"""
Module: suite.coord.suite
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from fabrication.builder import CoordBuilder
from model import Coord
from suite import Suite
from toolkit import CoordToolkit
from assurance.validator import CoordValidator


class CoordOperationSuite(Suite[Coord]):
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

