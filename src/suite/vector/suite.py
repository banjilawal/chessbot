# src/suite/bootstrapper/toolkit.py

"""
Module: suite.bootstrapper.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from builder import VectorBuilder
from model import Vector
from suite import ModelOperationSuite
from toolkit import VectorToolkit


class VectorOperationSuite(ModelOperationSuite[Vector]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Vector.

    Attributes:
        toolkit: VectorToolkit
        builder: VectorBuilder
        validator: VectorValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: VectorToolkit = VectorToolkit()
    builder: VectorBuilder = VectorBuilder()
    validator: VectorValidator = VectorValidator()

